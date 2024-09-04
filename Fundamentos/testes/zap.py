import webbrowser
import pyautogui
import time


def enviar_mensagens(mensagens, intervalo):
    # Abre o WhatsApp Web com o número fornecido
    telefone = "5519981418757"  # Número de telefone no formato internacional, sem +
    link = f"https://web.whatsapp.com/send?phone={telefone}"
    webbrowser.open(link)

    # Aguarda o site carregar completamente
    time.sleep(10)  # Ajuste o tempo conforme necessário

    for mensagem in mensagens:
        # Digita a mensagem
        pyautogui.typewrite(mensagem)
        pyautogui.press('enter')

        # Aguarda o intervalo entre mensagens
        time.sleep(intervalo)


def main():
    # Lista de mensagens a serem enviadas
    mensagens = [
        "SHREK",

        "Escrito por",

        "William Steig & Ted Elliott",




        "SHREK",
        "Era uma vez uma linda",
        "Princesa.Mas ela tinha um encantamento",
        "sobre ela de um tipo terrível que poderia",
        "só ser quebrado pelo primeiro beijo do amor.",
        "Ela foi trancada em um castelo guardado",
        "por um terrível dragão cuspidor de fogo.",
        "Muitos bravos cavaleiros tentaram",
        "libertá - la desta terrível prisão,",
        "mas não prevaleceu.Ela esperou no",
        "fortaleza do dragão na sala mais alta de",
        "a torre mais alta para seu verdadeiro amor",
        "e o primeiro beijo do amor verdadeiro.(risos)",
        "Como se isso fosse acontecer.o que",
        "uma carga de - (descarga do vaso sanitário)",

        "Allstar - por Smashmouth começa a tocar.Shrek continua sua",
        "dia.Enquanto em uma cidade próxima, os moradores se reúnem para ir",
        "depois do ogro.",

                "NOITE - PERTO DA CASA DE SHREK",

        "MAN1",
        "Acha que está lá?",

    "MAN2",
    "Tudo",
    "bem.Vamos",
    "obtê - lo!",

    "MAN1",
    "Uau.Aguentar.Você",
    "sabe",
    "o",
    "que",
    "isso",
    "coisa",
    "pode",
    "fazer",
    "com",
    "você?",
        "MAN3",
        "Sim, vai moer seus ossos por isso",
        "pão.",

        "Shrek se esgueira por trás deles e ri.",

        "SHREK",
        "Sim, bem, na verdade, isso seria um",
        "gigante.Agora, ogros, oh, eles são muito piores.",
        "Eles vão fazer um terno de seu recém -",
                                       "pele descascada.",

        "HOMENS",
        "Não!",

    "SHREK",
    "Eles",
    "vão",
    "raspar",
    "seu",
    "fígado.Aperte",
    "o",
    "geléia",
    "de",
    "seus",
    "olhos! Na",
    "verdade, é",
    "muito",
    "bom",
    "em",
    "torradas.",

    "MAN1",
    "De",
    "volta! De",
    "volta, fera! De",
    "volta! Eu",
    "te",
    "aviso!",
    "(acena a tocha para Shrek.)",

    "Shrek",
    "calmamente",
    "lambe",
    "os",
    "dedos",
    "e",
    "apaga",
    "a",
    "tocha.o",
    "os",
    "homens",
    "se",
    "afastam",
    "dele.Shrek",
    "ruge",
    "muito",
    "alto",
    "e",
    "longo",
    "e",
    "sua",
    "respiração",
    "extingue",
    "todas as tochas",
    "restantes",
    "até",
    "que",
    "o",
    "os",
    "homens",
    "estão",
    "no",
    "escuro.",

    "SHREK",
    "Esta",
    "é",
    "a",
    "parte",
    "em",
    "que",
    "você",
    "foge.",
    "(Os",
    "homens",
    "correm",
    "para",
    "fugir.Ele",
    "ri.)",
    "E",
    "fique",
    "de",
    "fora! (olha para baixo e pega",
    "até um pedaço de papel.Lê.)",
    "Procurado.",
    "Criaturas",
    "de",
    "contos",
    "de",
    "fadas.",
    " (Ele suspira e",
    "joga",
    "o",
    "papel",
    "por",
    "cima",
    "do",
    "ombro.)",


    "O",
    "PRÓXIMO",
    "DIA",

    "Há",
    "uma",
    "linha",
    "de",
    "criaturas",
    "de",
    "contos",
    "de",
    "fadas.O",
    "chefe",
    "da",
    "guarda",
    "senta",
    "em",
    "uma",
    "mesa",
    "pagando as pessoas",
    "por",
    "trazerem as criaturas",
    "dos",
    "contos",
    "de",
    "fadas",
    "para",
    "ele.Há",
    "gaiolas",
    "ao",
    "redor.Algumas",
    "das",
    "pessoas",
    "na",
    "fila",
    "são",
    "Peter",
    "Pan, que",
    "está",
    "carregando",
    "Sininho",
    "em",
    "uma",
    "gaiola, Gipetto",
    "que",
    "está",
    "carregando",
    "Pinóquio, e",
    "um",
    "fazendeiro",
    "que",
    "está",
    "carregando",
    "os",
    "três",
    "pequenos",
    "porcos.",

    "GUARDA",
    "Tudo",
    "bem.Este",
    "está",
    "cheio.Pegue",
    "um",
    "jeito! Mova - o",
    "junto.Vamos! Levante - se!",


    "PROTETOR",
    "DE",
    "CABEÇA",
    "Próximo!",

    "GUARDA",
    "(pegando a vassoura de bruxa)",
    "Dá - me",
    "isso!",
    "Seus",
    "dias",
    "de",
    "vôo",
    "acabaram.(quebra",
    "o",
    "vassoura",
    "ao",
    "meio)",

    "PROTETOR",
    "DE",
    "CABEÇA",
    "São",
    "20",
    "moedas",
    "de",
    "prata",
    "para",
    "a",
    "bruxa.",
    "Próximo!",

    "GUARDA",
    "Levante - se! Vamos!",

    "PROTETOR",
    "DE",
    "CABEÇA",
    "Vinte",
    "peças.",

    "URSINHO",
    "(chorando)",
    "Esta",
    "gaiola",
    "é",
    "muito",
    "pequena.",

    "BURRO",
    "Por",
    "favor, não",
    "me",
    "entregue.Eu",
    "nunca",
    "vou",
    "ser",
    "teimoso",
    "novamente.Eu",
    "posso",
    "mudar.Por",
    "favor!",
    "Me",
    "dê",
    "outra",
    "chance!",

    "VELHA",
    "Ah, cale",
    "a",
    "boca.(empurra",
    "a",
    "corda)",

    "BURRO",
    "Oh!",
    ]

    # Intervalo entre cada mensagem (em segundos)
    intervalo = 0.2  # Ajuste conforme necessário

    enviar_mensagens(mensagens, intervalo)


if __name__ == "__main__":
    main()
