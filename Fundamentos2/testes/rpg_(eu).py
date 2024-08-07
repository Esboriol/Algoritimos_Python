import random
import time

class perso_principal:

    def __init__(self):
        self.health = 100
        self.strenge = 10
        self.speed = 20
        self.inventory = []
        self.experience = 0
        self.lvl = 1
        self.iframe = False

    def attack(self):
        return random.randint(1, self.strenge)

    def defense(self):
        randola = random.randint(1, 4)
        if randola >= 3:
            self.iframe = True
            print("Voce esta Ivuneravel")
        else:
            self.iframe = False
            print("Voce não conseguil defender")

    def heal(self):
        healing = random.randint(5, 25)
        self.health += healing
        print(f"Voce curou {healing} de vida")

    def experience(self, amount):
        self.experience += amount
        print(f"Voce ganhou {amount} de experiencia")

        if self.experience == 60:
            self.lvlup()
            print("Voce subiu de nivel")

    def lvlup(self):
        self.lvl += 1
        self.experience -= 60
        self.strenge += 5
        self.speed += 3
        self.health += 25

class enemy:

    def __init__(self, name, health, speed, strenge):
        self.name = name
        self.health = health
        self.speed = speed
        self.strenge = strenge

    def attack(self):
        return random.randint(1, self.strenge)

def fight(player, enemy):
    while player.health > 0 and enemy.health > 0:
        print("1 para atacar")
        print("2 para denfender")
        print("3 para correr")

        escolha = input("Ecolha uma das opções: ")
        if escolha == "1":

            damage = player.attack()
            enemy.health -= damage
            print(f"Voce causou {damage} de dano")
            if enemy.health < 0:
                player.gain_experience(50)
                print(f"Voce derrotou o {enemy.name}!")
                return True
        elif escolha == "2":
            player.defense()
            if player.iframe:
                print("Voce esta Ivuneravel")
            else:
                print("Voce falhou em defender")
        elif escolha == "3":
            correr = random.randint(1, 2)
            if correr == 1:
                enemy.health = 0
                print(f"Voce conseguil correr do {enemy.name}")
            else:
                print("Voce falhou em correr")

        if not player.iframe:
            damage = enemy.attack
            player.health -= damage
            print(f"{enemy.name} causou {damage} de dano")

            return False

    return True

def explorar(player, enemy):
    loation = [
        "Uma floresta misteriosa.",
        "Uma caverna misteriosa.",
        "Um catelo antigo"
    ]
    encontros = [
        enemy("Globin", 30, 10, 3),
        enemy("Troll", 60, 4, 12),
        enemy("Sans", 1, 1, 1)
    ]
    print("Voce esta explorando o mundo")
    loation = random.choice(loation)
    print(f"Voce encontrou {loation}")

    if random.random() > 0.7:
        enemy = random.choice(encontros)
        return fight(player, enemy)
    else:
        print("Voce encontrou uma fonte de cura")
        player.heal()
        return True

def mostrar_iventario(player):
    if player.items:
        print("Seu inventario: ")
        for item in player.items:
            print(f"- {item}")

    else:
        print("Seu iventario está vazio")

def main():
    player = perso_principal()
    print("Bem vindo ao meu jogo")

    while player.health > 0:
        print("O que voce ira fazer?")
        print("1 Explorar")
        print("2 Ver Iventario")

        print("4 Sair")

        escolher = input("Escolha uma das opções: ")
        if escolher == 1:
            if not explorar(player):
                break
        elif escolher == 2:
            mostrar_iventario(player)

        elif escolher == 3:
            print(f"Saude atual: {player.health} e nivel {player.lvl}")

        elif escolher == 4:
            print("Saindo do jogo")
            break
        else:
            print("Escolha errada")

print("Obrigado por jogar")

if __name__ == "__main__":
    main()