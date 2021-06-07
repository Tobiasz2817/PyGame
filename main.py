import pygame,random,math
from Player import player
class Game:
    def __init__(self):
        # Intialize the pygame
        pygame.init()

        self.player = player(self)

        # create the screen
        self.screen = pygame.display.set_mode((1280, 720))

        # Background
        self.background = pygame.image.load('Niebo.png')

        # Caption and Icon
        pygame.display.set_caption("Sky Invader")
        self.icon = pygame.image.load('wrog.png')
        pygame.display.set_icon(self.icon)

        # Player
        self.player = player(self)

        # Enemy
        self.badguys = []
        self.badguyImg = []
        self.badguy_X_change = []
        self.badguy_Y_change = []
        self.badguy_X = []
        self.badguy_Y = []
        self.num_of_series = 6

        # Badyguy
        self.multiplyenemy()

        # Ready - You can't see the bullet on the screen
        # Fire - The bullet is currently moving
        self.bulletImg = pygame.image.load('superbanan.png')
        self.bulletX = 1200
        self.bulletY = 480
        self.bulletX_change = 10
        self.bulletY_change = 10
        self.bullet_state = "ready"
        self.bullets = []

        # Score
        self.score_value = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        self.testX = 10
        self.testY = 10

        self.over = pygame.font.Font('freesansbold.ttf', 64)

        # Game Loop
        self.running = True
        while self.running:

            # RGB = Red, Green, Blue
            self.screen.fill((0, 0, 0))
            # Background Image
            self.screen.blit(self.background, (0, 0))

            self.move()
            self.player.player_move_speed()

            for i in range(self.num_of_series):
                # Game over
                if self.badguy_X[i] < self.player.playerX + 190 and (self.player.playerY + 60 >= self.badguy_Y[i] and self.player.playerY + 20 <= self.badguy_Y[i]) or \
                        self.badguy_X[i] < 10:
                    for x in range(self.num_of_series):
                        self.badguy_X[x] = -150
                    self.player.playerX = -150
                    self.player.playerY = -150
                    self.bulletX = -150
                    self.bulletY = -150
                    self.game_over()
                    break
                self.badguy_X[i] -= self.badguy_X_change[i]
                if self.badguy_X[i] <= 0:
                    self.badguy_X_change[i] = -5
                elif self.badguy_X[i] >= 1150:
                    self.badguy_X_change[i] = 5

                self.position = self.collsion(self.badguy_X[i], self.badguy_Y[i], self.bulletX, self.bulletY)
                if self.position:
                    self.bulletX = 100
                    self.bullet_state = "ready"
                    self.score_value += 1
                    self.badguy_X[i] = 1150
                    self.badguy_Y[i] = random.randint(50, 616)

                self.badguy(self.badguy_X[i], self.badguy_Y[i], i)

            # Bullet Movement
            if self.bulletX >= 1030:
                self.bulletX = 100
                self.bullet_state = "ready"
            if self.bullet_state == "fire":
                self.fire_bullet(self.bulletX, self.bulletY)
                self.bulletX += self.bulletX_change

            self.player.player1(self.player.playerX, self.player.playerY)
            self.show_score(self.testX, self.testY)
            pygame.display.update()

    def show_score(self,x, y):
        score = self.font.render("Score :" + str(self.score_value), True, (0, 255, 255))
        self.screen.blit(score, (x, y))

    def game_over(self):
        its_over = self.over.render("GAME OVER", True, (0, 255, 255))
        its_over1 = self.over.render("Zakończyłeś gre z wynikiem : " + str(self.score_value), True, (0, 255, 255))
        self.screen.blit(its_over, (420, 200))
        self.screen.blit(its_over1, (120, 300))

    def fire_bullet(self,x, y):
        self.bullet_state = "fire"
        self.screen.blit(self.bulletImg, (x + 200, y + 50))

    def badguy(self,x, y, i):
        self.screen.blit(self.badguyImg[i], (x, y))

    def collsion(self,enemy_X, enemy_Y, bullet_X, bullet_Y):
        self.position = math.sqrt(math.pow(enemy_X - bullet_X, 2) + math.sqrt(math.pow(enemy_Y - bullet_Y, 2)))
        if self.position >=180 and self.position < 210 and (self.bulletY + 60 >= enemy_Y and self.bulletY + 20 <= enemy_Y):
            return True
        else:
            return False

    def move(self):
        self.player.player_move()

    def multiplyenemy(self):
        for i in range(self.num_of_series):
            self.badguyImg.append(pygame.image.load('wrog.png'))
            self.badguy_X_change.append(2)
            self.badguy_Y_change.append(0)
            self.badguy_X.append(random.randint(1000, 1150))
            self.badguy_Y.append(random.randint(50, 616))

g = Game()
