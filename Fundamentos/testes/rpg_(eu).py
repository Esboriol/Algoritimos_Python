import random
import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def potion(player):
    cura = random.randint(10, 25)
    player.health += cura
    print_slow(f"Você curou {cura} de vida")

def generate_item(player):
    sorte = random.randint(1, 2)
    if sorte == 1:
        player.add_item("Potion")
        print_slow("Você ganhou uma poção")
    elif sorte == 2:
        possi = [
            Weapon("Chicken Knife", 5, 10),
            Weapon("Stick", 1, 20)
        ]
        chosen_weapon = random.choice(possi)
        player.add_item(chosen_weapon)
        print_slow(f"Você ganhou {chosen_weapon}")

class Weapon:
    def __init__(self, name, strenge, speed):
        self.name = name
        self.strenge = strenge
        self.speed = speed

    def __repr__(self):
        return f"{self.name} (Dano: {self.strenge}, Velocidade: {self.speed})"

class Player:
    def __init__(self):
        self.health = 100
        self.strenge = 10
        self.weapon = None
        self.speed = 20
        self.inventory = []
        self.experience = 0
        self.lvl = 1
        self.iframe = False


    def add_item(self, item):
        self.inventory.append(item)

    def equip_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.weapon = weapon
            self.strenge = weapon.strenge
            self.speed = weapon.speed
            print_slow(f"Você equipou a arma: {weapon.name}")
        else:
            print_slow("Item não é uma arma")

    def attack(self):
        if self.weapon:
            return random.randint(1, self.weapon.strenge)
        return random.randint(1, self.strenge)

    def defense(self):
        randola = random.randint(1, 4)
        if randola >= 3:
            self.iframe = True

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

                if random.random() < 1.0:
                    generate_item(player)

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

        player.iframe = False

    return True

def explorar(player):
    locations = [
        "Uma floresta misteriosa.",
        "Uma caverna sombria.",
        "Um castelo antigo."
    ]
    encounters = [
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
        for index, item in enumerate(player.inventory, 1):
            print(f"{index}. {item}")
        escolha = input("Você quer usar algum item (S/N): ")
        if escolha.upper() == "S":
            item_index = int(input("Digite o número do item: ")) - 1
            if 0 <= item_index < len(player.inventory):
                item = player.inventory[item_index]
                if item == "Potion":
                    potion(player)
                    player.inventory.remove("Potion")
                elif isinstance(item, Weapon):
                    player.equip_weapon(item)
                    player.inventory.remove(item)
            else:
                print_slow("Número de item inválido")
        elif escolha.upper() == "N":
            print_slow("Ok, voltando")
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
            weapon_info = f"{player.weapon}" if player.weapon else "Nenhuma arma equipada"
            print_slow(f"Saúde atual: {player.health}, Arma: {weapon_info}, Nível: {player.lvl}")
        elif escolher == "4":
            print_slow("Saindo do jogo")
            break
        else:
            print_slow("Escolha errada")

    print_slow("Obrigado por jogar")

if __name__ == "__main__":
    main()
