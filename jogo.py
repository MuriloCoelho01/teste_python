import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
largura_tela = 800
altura_tela = 600
cor_fundo = (255, 255, 255)
fps = 60

# Configurações do canhão
canhao_cor = (0, 0, 255)
canhao_largura = 50
canhao_altura = 30
canhao_velocidade = 10

# Configurações do alvo
alvo_cor = (255, 0, 0)
alvo_raio = 20
alvo_velocidade = 5

# Inicialização da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Atire no Alvo')

relogio = pygame.time.Clock()

def desenha_canhao(x, y):
    pygame.draw.rect(tela, canhao_cor, [x, y, canhao_largura, canhao_altura])

def desenha_alvo(x, y):
    pygame.draw.circle(tela, alvo_cor, (x, y), alvo_raio)

def jogo():
    canhao_x = largura_tela // 2 - canhao_largura // 2
    canhao_y = altura_tela - canhao_altura - 10

    alvo_x = random.randint(alvo_raio, largura_tela - alvo_raio)
    alvo_y = alvo_raio

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and canhao_x > 0:
            canhao_x -= canhao_velocidade
        if keys[pygame.K_RIGHT] and canhao_x < largura_tela - canhao_largura:
            canhao_x += canhao_velocidade

        # Movimento do alvo
        alvo_y += alvo_velocidade
        if alvo_y > altura_tela + alvo_raio:
            alvo_x = random.randint(alvo_raio, largura_tela - alvo_raio)
            alvo_y = -alvo_raio

        tela.fill(cor_fundo)
        desenha_canhao(canhao_x, canhao_y)
        desenha_alvo(alvo_x, int(alvo_y))

        # Verifica se o canhão atingiu o alvo
        distancia = ((canhao_x + canhao_largura/2) - alvo_x)**2 + ((canhao_y + canhao_altura/2) - alvo_y)**2
        if distancia < (canhao_largura/2 + alvo_raio)**2:
            alvo_x = random.randint(alvo_raio, largura_tela - alvo_raio)
            alvo_y = -alvo_raio

        pygame.display.flip()
        relogio.tick(fps)

if __name__ == '__main__':
    jogo()
