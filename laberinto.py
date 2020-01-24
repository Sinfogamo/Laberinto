import pygame
import random

greenP = (20, 240, 50)
redP = (230, 0, 20)
BLACK = (0, 0, 0)
white = (255,255,255)
sizeSquare = 40

px = random.randrange(0, 14)
print(px)
xa = px
py = random.randrange(0, 14)
print(py)
ya = py

px2 = random.randrange(0, 14)
print(px2)
py2 = random.randrange(0, 14)
print(py2)

x = 0
y = 0
x2 = 0
y2 = 0
auto = [0,0,0,0]
pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Laberinto")
gameOver = False

def dibujar_texto(screen, texto, pos):
    fuente = pygame.font.SysFont('Barber Street_PersonalUseOnly', 50)
    text = fuente.render(texto, 1, BLACK)
    screen.blit(text, pos)

while not gameOver:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         gameOver = True
   screen.fill(BLACK)
   Fuente = pygame.font.SysFont("comicsansms", 16)
   Tx = 0
   Ty = 0
   for i in range(1, size[0], 40):
      for j in range(1, size[1], 40):
         pygame.draw.rect(screen, white, [i, j, 38, 38], 0)
         if py == 0:
               y = 1
         elif py == Ty:
               y = j
         Ty += 1
      if px == 0:
         x = 1
      elif px == Tx:
         x = i
      Texto = Fuente.render(str(Tx), True, white)
      screen.blit(Texto, [i, 2])
      if Tx != 0:
         screen.blit(Texto, [2, i + 16])
      Tx += 1
      Ty = 0

   Tx2 = 0
   Ty2 = 0
   for i in range(1, size[0], 40):
      for j in range(1, size[1], 40):
         pygame.draw.rect(screen, white, [i, j, 38, 38], 0)
         if py2 == 0:
               y2 = 1
         elif py2 == Ty:
               y2 = j
         Ty2 += 1
      if px2 == 0:
         x2 = 1
      elif px2 == Tx2:
         x2 = i
      Texto = Fuente.render(str(Tx2), True, white)
      screen.blit(Texto, [i, 2])
      if Tx2 != 0:
         screen.blit(Texto, [2, i + 16])
      Tx2 += 1
      Ty2 = 0
   
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_w:
            y -= 0.1
            py = y
         if event.key == pygame.K_a:
            x -= 0.1
            px = x
         if event.key == pygame.K_s:
            y += 0.1
            py = y
         if event.key == pygame.K_d:
            x += 0.1
            px = x

      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            if xa != px and x < 560:
               x += 0.1
      if event.type == pygame.KEYUP:
         if event.key == pygame.K_SPACE:
            if x < 560:
               x += 0.1
               
   if x == x2 and y == y2:
      dibujar_texto(screen, "GAME OVER", [100, 350])

   pygame.draw.rect(screen, greenP, [x, y, 38, 38])
   pygame.draw.rect(screen, redP, [x2, y2, 38, 38])
   
   pygame.display.flip()
pygame.quit()