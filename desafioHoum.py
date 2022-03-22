from unittest import result
import requests # para trabajar con peticiones http
import string   # para trabajar con cadenas

#Variables Globales
url_base = 'https://pokeapi.co/api/v2/egg-group/'
lista_base = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


#  Valida una cadena bajo los criterios de que en la cadena posean “at” y ademas
#  tengan  2“a” en su nombre,incluyendo la primera del “at”.
def validaPalabra(palabra):

    patron="at"
    letra = "a"

    if palabra.find(patron) >= 0:
        val1=True
    else:
        val1=False

    lst = []

    for pos,string in enumerate(palabra):
        if (string==letra):
            lst.append(pos)

    if len(lst) ==2 and val1==True:
        return True
    else:
        return False
  
#funcion que junta a todos los Pokemon de las egg-group
#de los grupos que se les proporciones en la lista en una lista
def reunirPokemonsDeGrupos(lista):
    
    new_group = []
    for i in lista:
        url_group = url_base+str(i)+"/"
        #print(url_group)
        
        response = requests.get(url_group)
        #print(response.json())

        if response.status_code == 200:
            payload = response.json()
            pokemon_species = payload.get('pokemon_species', [])

            if pokemon_species:
                for pokemon in pokemon_species:
                    new_group.append(pokemon['name'])
    
    return new_group

#Recorre una lista y genera una nueva sin duplicados
def sinDuplicadosLst(lista):
    listaSinDuplicados = []
    for item in lista:
        if item not in listaSinDuplicados:
            listaSinDuplicados.append(item)

    return listaSinDuplicados

#Busca un determinado pokemon en todos los grupos y 
# Guarda el id del grupo en una lista nueva.
def ubicarGrupDePokemon(pokemon_name):
        
    lst_group = []
    for i in range(15):
        url_group = url_base+str(i+1)+"/"
        #print(url_group)
        
        response = requests.get(url_group)
        #print(response.json())

        if response.status_code == 200:
            payload = response.json()
            pokemon_species = payload.get('pokemon_species', [])

            if pokemon_species:
                for pokemon in pokemon_species:
                    name = pokemon['name']
                    if name == pokemon_name:
                        lst_group.append(i+1)
    
    return lst_group


def obtnerGeneracionI(generacion):
    url = "https://pokeapi.co/api/v2/generation/"
    url_base = url + str(generacion) +'/'
    pokemon_genI = []

    response = requests.get(url_base)
        #print(response.json())

    if response.status_code == 200:
        payload = response.json()
        pokemon_species = payload.get('pokemon_species', [])

        if pokemon_species:
            for pokemon in pokemon_species:
                #name = pokemon['name']
                pokemon_genI.append(pokemon['name'])
                #print(name)
    
    return pokemon_genI

def obtenerNombrePeso(lista,tipo):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    pesaje = [] 
    for pok in lista:
        pokemon_data_url = url + pok +'/'
        response = requests.get(pokemon_data_url)
        data = response.json()
        pokemon_type=data['types']
        cadena=(str(pokemon_type))
        if cadena.find(tipo) > 0:
            pesaje.append(data['weight'])
    
    pesado=max(pesaje)

    ligero=min(pesaje)

    print("["+str(pesado)+","+str(ligero)+"]")



# 1. Obtén cuantos pokemones poseen en sus nombres “at” y tienen 2 “a” en su nombre,
# incluyendo la primera del “at”. Tu respuesta debe ser un número.
def desafioUno():
    universoPokemon = []
    cuentaPokemon = 0
    universoPokemon.extend(sinDuplicadosLst(reunirPokemonsDeGrupos(lista_base)))

    for pok in universoPokemon:
        if validaPalabra(pok) ==True:
            ##print(pok) ##habilitar si se desea validar manualmente las palabras
            cuentaPokemon = cuentaPokemon + 1
    
    print(cuentaPokemon)

#  2. ¿Con cuántas especies de pokémon puede procrear raichu? (2 Pokémon pueden
#  procrear si están dentro del mismo egg group). Tu respuesta debe ser un número.
#  Recuerda eliminar los duplicados.
def desafioDos(pokem):
    universoPokemon = []
    universoPokemon.extend(sinDuplicadosLst(reunirPokemonsDeGrupos(ubicarGrupDePokemon(pokem))))
    #print(*universoPokemon,sep='\n') #habilitar si se quiere ver a los pokemon con los que procrearia
    print(len(universoPokemon))


#  3. Entrega el máximo y mínimo peso de los pokémon de tipo ghting de primera
#  generación (cuyo id sea menor o igual a 151). Tu respuesta debe ser una lista con el
#  siguiente formato: [1234, 12], en donde 1234 corresponde al máximo peso y 12 al
#  mínimo
def desafioTres(generacion,tipo_p):
    obtenerNombrePeso(obtnerGeneracionI(generacion),tipo_p)


# &-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&
# &-&-&-&-&-&-&-& CUERPO PRINCIPAL DEL PROGRAMA &-&-&-&-&-&-&-&
# &-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&-&
if __name__ == '__main__':
    
    print("\nRespuesta al desafio 1: Cuenta pokemones cuyos nombres tengan 2'a' y una cadena 'at'")
    desafioUno()
    
    print("\nRespuesta al desafio 2: Cuenta con cuántas especies de pokémon puede procrear raichu")
    #Se requiere un nombre de algun pokemon como parametro
    desafioDos("raichu")

    print("\nRespuesta al desafio 3: Entrega el máximo y mínimo peso de los pokémon de tipo fighting de primera generación")
    # Se ingresa la generacion y el tipo de pokemon como parametros
    desafioTres(1,'fighting')


