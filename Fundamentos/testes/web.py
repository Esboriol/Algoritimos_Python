import requests
from bs4 import BeautifulSoup
from googlesearch import search

def obter_preco_mercadolivre(url):
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
    except requests.RequestException as e:
        return f"Erro ao acessar a página: {e}"

    sopa = BeautifulSoup(resposta.text, 'html.parser')
    preco_elemento = sopa.find('span', {'class': 'price-tag-fraction'})  # Ajuste conforme necessário
    if preco_elemento:
        return preco_elemento.get_text(strip=True)
    return "Preço não encontrado"

def obter_preco_kabum(url):
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
    except requests.RequestException as e:
        return f"Erro ao acessar a página: {e}"

    sopa = BeautifulSoup(resposta.text, 'html.parser')
    preco_elemento = sopa.find('span', {'class': 'price'})  # Ajuste conforme necessário
    if preco_elemento:
        return preco_elemento.get_text(strip=True)
    return "Preço não encontrado"

def obter_preco_pichau(url):
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
    except requests.RequestException as e:
        return f"Erro ao acessar a página: {e}"

    sopa = BeautifulSoup(resposta.text, 'html.parser')
    preco_elemento = sopa.find('span', {'class': 'preco'})  # Ajuste conforme necessário
    if preco_elemento:
        return preco_elemento.get_text(strip=True)
    return "Preço não encontrado"

def obter_preco_google(query, site):
    try:
        urls = list(search(query, num_results=5))
        for url in urls:
            if site in url:
                print(f"Pesquisando em: {url}")
                if 'mercadolivre' in site:
                    return obter_preco_mercadolivre(url)
                elif 'kabum' in site:
                    return obter_preco_kabum(url)
                elif 'pichau' in site:
                    return obter_preco_pichau(url)
        return "Nenhum URL relevante encontrado"
    except Exception as e:
        return f"Erro ao buscar no Google: {e}"

def main():
    produto = input("Digite o nome do produto que deseja pesquisar: ")

    # Pesquisa no Mercado Livre
    query_ml = f"{produto} site:mercadolivre.com.br"
    preco_ml = obter_preco_google(query_ml, 'mercadolivre')

    # Pesquisa na Kabum
    query_kabum = f"{produto} site:kabum.com.br"
    preco_kabum = obter_preco_google(query_kabum, 'kabum')

    # Pesquisa na Pichau
    query_pichau = f"{produto} site:pichau.com.br"
    preco_pichau = obter_preco_google(query_pichau, 'pichau')

    print(f"Preço encontrado no Mercado Livre: {preco_ml}")
    print(f"Preço encontrado na Kabum: {preco_kabum}")
    print(f"Preço encontrado na Pichau: {preco_pichau}")

if __name__ == "__main__":
    main()
