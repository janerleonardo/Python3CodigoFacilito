import requests

def get_pokemons(url = 'https://pokeapi.co/api/v2/pokemon-form/', offset=0):
    args = {'offset' : offset} if offset else {}
    print(args)
    response = requests.get(url=url, params=args)
    if response.status_code == 200:
        pyload = response.json()
        results = pyload.get('results', [])
        if results:
            for pokemon in results:
                name = pokemon['name']
                print(name)
        next = input("Continuar Listando [Y/N]").lower()
        if next == 'y':
            get_pokemons(offset=offset+20)


if __name__== '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form/'
    get_pokemons()

