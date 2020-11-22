import pygame

pygame.init()

size = (300,100)
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
#H
pygame.draw.rect(screen, (255, 255, 0), (0, 0, 34, 100))
pygame.draw.rect(screen, (255,255,0), (33,33,33,33))
pygame.draw.rect(screen, (255,255,0), (66,0,34,100))

#C
pygame.draw.circle(screen, (0,0,255), (154,50), 54)
pygame.draw.polygon(screen, (255,255,255), [(150, 50), (200, 20), (200, 80)])
pygame.draw.circle(screen, (255,255,255), (154,50), 17)

#H
pygame.draw.rect(screen, (255, 0, 0), (200, 0, 33, 100))
pygame.draw.rect(screen, (255,0,0), (233,33,33,33))
pygame.draw.rect(screen, (255,0,0), (266,0,34,100))



pygame.display.flip()

#pygame.quit()
