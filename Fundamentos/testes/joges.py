import random
import pygame
import sys

pygame.init()

# Inicializa a tela
tela = pygame.display.set_mode((800, 600))

# Define a cor de fundo
fundo = (0, 0, 0)

# Posição inicial do personagem
velocidade = 3

# Carrega e redimensiona a imagem do personagem
class Personagem:
    def __init__(self):
        self.image = pygame.image.load("imagem/nave.png")
        self.largura, self.altura = 100, 100
        self.image = pygame.transform.scale(self.image, (self.largura, self.altura))
        self.x = 400
        self.y = 300
        self.vida = 5  # Vida inicial do jogador ajustada para 5
        self.tiro = "Normal"
        self.ultimo_tiro_normal = 0  # Tempo do último tiro normal
        self.ultimo_tiro_power = 0  # Tempo do último tiro power

    def draw(self):
        tela.blit(self.image, (self.x, self.y))

    def take_damage(self, damage):
        self.vida -= damage
        if self.vida <= 0:
            self.die()

    def die(self):
        print("Você morreu!")
        pygame.quit()
        sys.exit()

    def change_shooting_type(self, new_type):
        self.tiro = new_type
        print(f"Tipo de tiro alterado para: {self.tiro}")

    def shoot(self):
        tempo = pygame.time.get_ticks()
        if self.tiro == "Normal":
            # Ajustar cooldown para tiro normal
            if tempo - self.ultimo_tiro_normal >= 250:  # Cooldown de 250ms (0.25 segundos)
                self.ultimo_tiro_normal = tempo
                return Projetil(self.x + self.largura // 2, self.y)
        elif self.tiro == "Power":
            # Ajustar cooldown para tiro power
            if tempo - self.ultimo_tiro_power >= 300:  # Cooldown de 300ms (0.3 segundos)
                self.ultimo_tiro_power = tempo
                projectiles.append(Projetil(self.x + self.largura // 2 - 20, self.y))
                projectiles.append(Projetil(self.x + self.largura // 2 + 20, self.y))
                return None

personagem = Personagem()

# Classe Projetil
class Projetil:
    def __init__(self, x, y, target_x=None, target_y=None):
        self.x = x
        self.y = y
        self.vel = 10
        self.radius = 5

        if target_x is not None and target_y is not None:
            self.dx = target_x - x
            self.dy = target_y - y
            self.length = (self.dx ** 2 + self.dy ** 2) ** 0.5
            self.dx /= self.length
            self.dy /= self.length
        else:
            self.dx = 0
            self.dy = -1

    def move(self):
        self.x += self.dx * self.vel
        self.y += self.dy * self.vel

    def draw(self):
        pygame.draw.circle(tela, (255, 255, 0), (int(self.x), int(self.y)), self.radius)

    def collides_with(self, obj):
        distance = ((self.x - (obj.x + obj.largura // 2)) ** 2 + (self.y - (obj.y + obj.altura // 2)) ** 2) ** 0.5
        return distance < self.radius + (obj.largura // 2)

projectiles = []

# Classe Bala
class Bala:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 10
        self.radius = 5

    def move(self):
        self.y += self.vel

    def draw(self):
        pygame.draw.circle(tela, (255, 255, 0), (self.x, self.y), self.radius)

    def collides_with(self, personagem):
        distance = ((self.x - (personagem.x + personagem.largura // 2)) ** 2 + (self.y - (personagem.y + personagem.altura // 2)) ** 2) ** 0.5
        return distance < self.radius + (personagem.largura // 2)

# Classe Drop
class Drop:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.radius = 10
        self.vel = 2  # Velocidade de descida

    def move(self):
        self.y += self.vel

    def draw(self):
        cor = (0, 255, 0) if self.tipo == "Power" else (0, 0, 255)
        pygame.draw.circle(tela, cor, (self.x, self.y), self.radius)

    def collides_with(self, personagem):
        distance = ((self.x - (personagem.x + personagem.largura // 2)) ** 2 + (self.y - (personagem.y + personagem.altura // 2)) ** 2) ** 0.5
        return distance < self.radius + (personagem.largura // 2)

# Classe Inimigo
class Inimigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 2
        self.largura = 60
        self.altura = 60
        self.image = pygame.image.load("imagem/file.png")
        self.image = pygame.transform.scale(self.image, (self.largura, self.altura))
        self.life = 3
        self.time = pygame.time.get_ticks()
        self.active = True
        self.dano = 0.5  # Dano causado pelos inimigos

    def move(self):
        if self.active:
            self.x += self.vel
            if self.x <= 0 or self.x + self.largura >= 800:
                self.vel = -self.vel

    def shoot(self):
        if self.active:
            tempo = pygame.time.get_ticks()
            if tempo - self.time > 300:
                projectiles.append(Bala(self.x + self.largura // 2, self.y + self.altura))
                self.time = tempo

    def draw(self):
        if self.active:
            tela.blit(self.image, (self.x, self.y))

    def take_damage(self):
        if self.active:
            self.life -= 1
            if self.life <= 0:
                self.die()

    def die(self):
        self.active = False

        # Adiciona um drop ao morrer
        if random.random() < 0.3:  # Ajustado para uma probabilidade de 30%
            drop_type = "Power" if random.random() < 0.5 else "Speed"
            drops.append(Drop(self.x + self.largura // 2, self.y + self.altura, drop_type))

# Classe de Gerenciamento de Ondas
class WaveManager:
    def __init__(self):
        self.current_wave = 0
        self.waves = [
            {"count": 3, "positions": [(100, 100), (300, 100), (500, 100)]},
            {"count": 5, "positions": [(100, 50), (300, 50), (500, 50), (200, 200), (400, 200)]},
            {"count": 7, "positions": [(50, 50), (150, 50), (250, 50), (350, 50), (450, 50), (550, 50), (650, 50)]}
        ]
        self.enemies = []
        self.spawn_wave()

    def spawn_wave(self):
        if self.current_wave < len(self.waves):
            print(f"Você está na {self.current_wave + 1}ª onda")
            wave = self.waves[self.current_wave]
            for pos in wave["positions"]:
                self.enemies.append(Inimigo(pos[0], pos[1]))
            self.current_wave += 1

    def update(self):
        if not self.enemies and self.current_wave < len(self.waves):
            self.spawn_wave()
        for enemy in self.enemies:
            enemy.move()
            enemy.shoot()
            if not enemy.active:
                self.enemies.remove(enemy)

    def draw(self):
        for enemy in self.enemies:
            enemy.draw()

# Inicializa o gerenciador de ondas e lista de drops
wave_manager = WaveManager()
drops = []

# Configura o relógio para controlar o FPS
clock = pygame.time.Clock()

ultimo_tiro = pygame.time.get_ticks()

while True:
    # Processa eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Preenche a tela com a cor de fundo
    tela.fill(fundo)

    # Obtém o estado das teclas
    tecla = pygame.key.get_pressed()

    # Atualiza a posição do personagem com base nas teclas pressionadas
    if tecla[pygame.K_LEFT]:
        personagem.x -= velocidade
    if tecla[pygame.K_RIGHT]:
        personagem.x += velocidade
    if tecla[pygame.K_UP]:
        personagem.y -= velocidade
    if tecla[pygame.K_DOWN]:
        personagem.y += velocidade

    tempo = pygame.time.get_ticks()
    if tecla[pygame.K_x]:
        proj = personagem.shoot()
        if proj:
            projectiles.append(proj)
        ultimo_tiro = tempo

    # Atualiza e desenha os projéteis
    for proj in projectiles[:]:
        proj.move()
        if proj.y < 0 or proj.y > 600 or proj.x < 0 or proj.x > 800:
            projectiles.remove(proj)
        elif isinstance(proj, Projetil):
            for enemy in wave_manager.enemies:
                if proj.collides_with(enemy):
                    projectiles.remove(proj)
                    enemy.take_damage()
                    break

    # Verifica colisões dos tiros dos inimigos com o jogador
    for bala in [bala for bala in projectiles if isinstance(bala, Bala)]:
        bala.move()
        if bala.y > 600:
            projectiles.remove(bala)
        elif bala.collides_with(personagem):
            projectiles.remove(bala)
            personagem.take_damage(0.5)  # Aplicando dano de 0.5

    # Atualiza e desenha a onda de inimigos
    wave_manager.update()
    wave_manager.draw()

    # Atualiza e desenha os drops
    for drop in drops[:]:
        drop.move()  # Move o drop para baixo
        drop.draw()
        if drop.collides_with(personagem):
            personagem.change_shooting_type(drop.tipo)
            drops.remove(drop)

    # Desenha a imagem do personagem na tela
    personagem.draw()

    # Desenha os projéteis na tela
    for proj in projectiles:
        proj.draw()

    # Atualiza a tela
    pygame.display.flip()

    # Controla o FPS
    clock.tick(60)
