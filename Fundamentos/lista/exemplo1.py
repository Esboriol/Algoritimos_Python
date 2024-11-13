
#adicionando na lista
cidades = ['Saltinho']
cidades.append('Piracicaba')
print(cidades)

#adicionando na lista em uma posição expecifica
apps = ['Orkut']
apps.insert(0, 'Mirc')
print(apps)

#removendo quem tiver na posição expecifica da lista
bolos = ['Chocolate', 'Prestígio', 'Morango']
bolos.pop(1)
print(bolos)

#remove quem tiver o nome expecifico da lista
chinelos = ['Havaianas', 'Rider', "Ipanema"]
chinelos.remove('Rider')
print(chinelos)

bairros = [
    'Jaraguá', 'Santa Inês', 'Jupiá', 'Bosque', 'Parque Orlândia', 'Santa Terezinha',
    'Mária Dedini', 'Cantagalo', 'Vida Nova', 'Cecap'
]

print(len(bairros))

#ALtera a lista original
bairros.sort(reverse=True)
print(bairros)
