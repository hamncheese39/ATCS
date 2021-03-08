import pygame
import math
import random
pygame.init()
friction = 1

#circle that moves and bounces off other items and walls
class Ball:
  def __init__(self, xPos, yPos, xVel, yVel, radius, color):
    self.xPos = xPos
    self.yPos = yPos
    self.xVel = xVel
    self.yVel = yVel
    self.radius = radius
    self.color = color

  def show(self, screen):
    pygame.draw.circle(screen, self.color, (int(self.xPos), int(self.yPos)), self.radius)
#method 1
  def move(self, screen):
    w, h = screen.get_size()
    self.xPos += self.xVel
    self.yPos += self.yVel
    if self.xPos >= w-self.radius or self.xPos <= self.radius:
      self.xPos -= self.xVel
      self.xVel *= -friction
    if self.yPos <= self.radius or self.yPos >= h-self.radius:
      self.yPos -= self.yVel
      self.yVel *= -friction
      
#square that moves and bounces off walls and other items
class Box:
  def __init__(self, xPos, yPos, xVel, yVel, radius, color):
    self.xPos = xPos
    self.yPos = yPos
    self.xVel = xVel
    self.yVel = yVel
    self.radius = radius
    self.color = color

  def show(self, screen):
    pygame.draw.rect(screen, self.color, (int(self.xPos-self.radius), int(self.yPos-self.radius), int(self.radius*2), int(self.radius*2)))
# method 2
  def move(self, screen):
    w, h = screen.get_size()
    self.xPos += self.xVel
    self.yPos += self.yVel
    if self.xPos >= w-self.radius or self.xPos <= self.radius:
      self.xVel *= -friction
    if self.yPos <= self.radius or self.yPos >= h-self.radius:
      self.yVel *= -friction

#makes the background change color and everything pause for a given amount of time
class Distraction:
  def __init__(self, period, color):
    self.period = period
    self.color = color

  def show(self, screen):
    w, h = screen.get_size()
    pygame.time.wait(self.period)
    shape = Box(0,0,0,0,w+h,self.color)
    #Use of inheritance
    shape.show(screen)

# method 3
#Determines when the distraction should be shown
  def showOrNo(self, avgPerSecond, ticks):
    if random.randrange(1000/avgPerSecond) == ticks % (1000/avgPerSecond):
      return True
    return False

def sign(x):
  if x == 0:
    return x
  else:
    return abs(x)/x

size = (700,500)
screen = pygame.display.set_mode(size)

mod = random.randrange(3,40)


balls = []
items = []
for i in range(10):
  ball = Ball(random.randrange(20,680),random.randrange(20,480), random.randrange(1,60)/10, random.randrange(1,150)/10, 12, (200,0,0))
  balls.append(ball)
  items.append(ball)
boxes = []
for i in range(10):
  box = Box(random.randrange(20,680),random.randrange(20,480), random.randrange(1,60)/10, random.randrange(1,150)/10, 12, (200,0,0))
  boxes.append(box)
  items.append(box)

specialItem = random.choice(items)
specialItem.color = (0,0,200)


#boxes = [box1]
clock = pygame.time.Clock()
x = 0
printed = False
running = True
print("follow the blue object after it turns red for 20 seconds")
while running:
  clock.tick(60)
  if "MOUSEBUTTONUP" in pygame.event.get():
    pass
  screen.fill((255, 255, 255))
  # changes the ball to red after 5 seconds
  if pygame.time.get_ticks() >= 5000 and pygame.time.get_ticks() < 5100:
    specialItem.color = (201,0,0)
  # for the next 20 seconds everything moves
  if pygame.time.get_ticks() <= 25000:
    for ball in balls:
      ball.move(screen)
      ball.show(screen)
    for box in boxes:
      box.move(screen)
      box.show(screen)
    for item1 in items:
      for item2 in items[items.index(item1)+1:]:
        distance = math.sqrt((item1.xPos-item2.xPos)**2 + (item1.yPos-item2.yPos)**2)
        if distance <= item1.radius + item2.radius:
          oneX = item1.xVel
          oneY = item1.yVel
          twoX = item2.xVel
          twoY = item2.yVel
          item1.xVel, item1.yVel = item2.xVel*friction, item2.yVel*friction
          item2.xVel, item2.yVel = oneX*friction, oneY*friction
  # after 20 seconds, everything stops moving
  else:
    if not printed:
      print("click on the correct object to win!")
      printed = True
    for item in items:
      item.show(screen)
    if pygame.mouse.get_pressed()[0] == True:
      if math.sqrt((pygame.mouse.get_pos()[0] - specialItem.xPos)**2 + (pygame.mouse.get_pos()[1] - specialItem.yPos)**2) < specialItem.radius:
        print("you won!")
      else:
        print("you lost!")
      specialItem.color = (0,0,200)
      specialItem.show(screen)
      pygame.quit()

  # at random points with given probability, a green rectangle shows up and everyting pauses
  d = Distraction(random.randrange(100,1000),(0,255,0))
  if d.showOrNo(0.5, pygame.time.get_ticks()):
    d.show(screen)
      




  

  pygame.display.flip()
