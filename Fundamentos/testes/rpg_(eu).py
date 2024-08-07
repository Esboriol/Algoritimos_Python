import random
import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

class Player:
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
            print_slow("Você está Invulnerável")
        else:
            self.iframe = False
            print_slow("Você não conseguiu defender")

    def heal(self):
        healing = random.randint(5, 25)
        self.health += healing
        print_slow(f"Você curou {healing} de vida")

    def gain_experience(self, amount):
        self.experience += amount
        print_slow(f"Você ganhou {amount} de experiência")

        if self.experience >= 60:
            self.lvlup()
            print_slow("Você subiu de nível")

    def lvlup(self):
        self.lvl += 1
        self.experience -= 60
        self.strenge += 5
        self.speed += 3
        self.health += 25

class Enemy:
    def __init__(self, name, health, speed, strenge):
        self.name = name
        self.health = health
        self.speed = speed
        self.strenge = strenge

    def attack(self):
        return random.randint(1, self.strenge)

def fight(player, enemy):
    while player.health > 0 and enemy.health > 0:
        print_slow("1 para atacar")
        print_slow("2 para defender")
        print_slow("3 para correr")

        escolha = input("Escolha uma das opções: ")
        if escolha == "1":
            damage = player.attack()
            enemy.health -= damage
            print_slow(f"Você causou {damage} de dano")
            if enemy.health <= 0:
                player.gain_experience(50)
                print_slow(f"Você derrotou o {enemy.name}!")
                return True
        elif escolha == "2":
            player.defense()
            if player.iframe:
                print_slow("Você está Invulnerável")
            else:
                print_slow("Você falhou em defender")
        elif escolha == "3":
            correr = random.randint(1, 2)
            if correr == 1:
                print_slow(f"Você conseguiu correr do {enemy.name}")
                return True
            else:
                print_slow("Você falhou em correr")
        else:
            print_slow("Escolha inválida!")

        if not player.iframe:
            damage = enemy.attack()
            player.health -= damage
            print_slow(f"{enemy.name} causou {damage} de dano")

            if player.health <= 0:
                print_slow("Você foi derrotado!")
                return False

    return True

def explorar(player):
    locations = [
        "Uma floresta misteriosa.",
        "Uma caverna sombria.",
        "Um castelo antigo."
    ]
    encounters = [
        Enemy("Goblin", 30, 10, 3),
        Enemy("Troll", 60, 4, 12),
        Enemy("Sans", 1, 1, 1)
    ]
    print_slow("Você está explorando o mundo...")
    location = random.choice(locations)
    print_slow(f"Você encontrou {location}")

    # Chance de encontro: 70% monstro, 30% cura
    if random.random() < 0.7:
        enemy = random.choice(encounters)
        return fight(player, enemy)
    else:
        print_slow("Você encontrou uma fonte de cura")
        player.heal()
        return True

def mostrar_inventario(player):
    if player.inventory:
        print_slow("Seu inventário: ")
        for item in player.inventory:
            print_slow(f"- {item}")
    else:
        print_slow("Seu inventário está vazio")

def main():
    player = Player()
    print_slow("Bem-vindo ao meu jogo")

    while player.health > 0:
        print_slow("O que você irá fazer?")
        print_slow("1. Explorar")
        print_slow("2. Ver Inventário")
        print_slow("3. Status")
        print_slow("4. Sair")

        escolher = input("Escolha uma das opções: ")
        if escolher == "1":
            if not explorar(player):
                break
        elif escolher == "2":
            mostrar_inventario(player)
        elif escolher == "3":
            print_slow(f"Saúde atual: {player.health} e nível {player.lvl}")
        elif escolher == "4":
            print_slow("Saindo do jogo")
            break
        else:
            print_slow("Escolha errada")

    print_slow("Obrigado por jogar")

if __name__ == "__main__":
    main()
