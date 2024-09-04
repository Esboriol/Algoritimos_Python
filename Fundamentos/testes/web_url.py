from googlesearch import search

def buscar_urls_google(query, site):
    urls = []
    try:
        # Busca as URLs relacionadas à consulta
        for url in search(query, num_results=10):
            # Verifica se o domínio do site está presente na URL
            if site in url:
                urls.append(url)
    except Exception as e:
        print(f"Erro ao buscar no Google: {e}")
    return urls

def main():
    produto = input("Digite o nome do produto que deseja pesquisar: ")

    sites = {
        'mercadolivre': 'mercadolivre.com.br',
        'kabum': 'kabum.com.br',
        'pichau': 'pichau.com.br',
        'shopee': 'shopee.com.br'
    }

    print("Escolha uma opção de pesquisa:")
    print("1. Buscar em todos os sites")
    for i, site in enumerate(sites.keys(), 2):
        print(f"{i}. {site.capitalize()}")

    escolha = int(input("Digite o número da opção desejada: "))

    if escolha == 1:
        # Buscar em todos os sites
        print(f"\nBuscando URLs para '{produto}' em todos os sites...")
        for nome_site, dominio in sites.items():
            print(f"\nBuscando em: {nome_site.capitalize()} ({dominio})")
            query = f"{produto} site:{dominio}"
            urls = buscar_urls_google(query, dominio)

            if urls:
                print("URLs encontradas:")
                for url in urls:
                    print(url)
            else:
                print("Nenhuma URL encontrada.")
    elif 2 <= escolha <= len(sites) + 1:
        # Buscar no site específico
        site_escolhido = list(sites.values())[escolha - 2]  # Ajusta índice para seleção específica
        print(f"\nBuscando URLs para '{produto}' no site '{site_escolhido}'...")
        query = f"{produto} site:{site_escolhido}"
        urls = buscar_urls_google(query, site_escolhido)

        if urls:
            print("URLs encontradas:")
            for url in urls:
                print(url)
        else:
            print("Nenhuma URL encontrada.")
    else:
        print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
