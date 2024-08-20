import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Space Invaders")

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
verde = (0, 255, 0)
azul = (0, 0, 255)

# Configurações do jogador
nave_img = pygame.image.load('imagem/marijuana (1).png')  # Adicione a imagem da nave aqui
nave_img = pygame.transform.scale(nave_img, (64, 64))
nave_x = largura_tela // 2
nave_y = altura_tela - 70
nave_velocidade = 5

# Configurações dos inimigos
inimigo_img = pygame.image.load('imagem/coracao.png')  # Adicione a imagem dos inimigos aqui
inimigo_img = pygame.transform.scale(inimigo_img, (64, 64))
inimigos = []
inimigo_velocidade = 2
num_inimigos = 6

for i in range(num_inimigos):
    inimigos.append(pygame.Rect(random.randint(0, largura_tela - 64), random.randint(0, altura_tela // 2 - 64), 64, 64))

# Configurações dos tiros
tiros = []
tiro_velocidade = 7
tiro_img = pygame.Surface((5, 10))
tiro_img.fill(branco)

# Função para desenhar o jogador
def desenhar_nave():
    tela.blit(nave_img, (nave_x, nave_y))

# Função para desenhar os inimigos
def desenhar_inimigos():
    for inimigo in inimigos:
        tela.blit(inimigo_img, inimigo.topleft)

# Função para desenhar os tiros
def desenhar_tiros():
    for tiro in tiros:
        tela.blit(tiro_img, tiro.topleft)

# Função para mover a nave
def mover_nave(teclas):
    global nave_x
    if teclas[pygame.K_LEFT] and nave_x > 0:
        nave_x -= nave_velocidade
    if teclas[pygame.K_RIGHT] and nave_x < largura_tela - 64:
        nave_x += nave_velocidade

# Função para mover os inimigos
def mover_inimigos():
    global inimigos
    for inimigo in inimigos:
        inimigo.y += inimigo_velocidade
        if inimigo.y > altura_tela:
            inimigo.x = random.randint(0, largura_tela - 64)
            inimigo.y = random.randint(-100, -10)

# Função para mover os tiros
def mover_tiros():
    global tiros
    novos_tiros = []
    for tiro in tiros:
        tiro.y -= tiro_velocidade
        if tiro.y > 0:
            novos_tiros.append(tiro)
    tiros = novos_tiros

# Função para checar colisões
def checar_colisoes():
    global inimigos, tiros
    novos_inimigos = []
    novos_tiros = []
    for inimigo in inimigos:
        for tiro in tiros:
            if tiro.colliderect(inimigo):
                inimigos.remove(inimigo)
                tiros.remove(tiro)
                break
        else:
            novos_inimigos.append(inimigo)
    inimigos = novos_inimigos

# Loop principal do jogo
rodando = True
clock = pygame.time.Clock()

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                tiro = pygame.Rect(nave_x + 30, nave_y, 5, 10)
                tiros.append(tiro)

    teclas = pygame.key.get_pressed()
    mover_nave(teclas)
    mover_inimigos()
    mover_tiros()
    checar_colisoes()

    tela.fill(preto)
    desenhar_nave()
    desenhar_inimigos()
    desenhar_tiros()
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
