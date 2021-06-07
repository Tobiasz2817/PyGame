import pygame

class player:
    def __init__(self,game):
        self.game = game
        pygame.init()
        # Player
        self.playerImg = pygame.image.load('space.png')
        self.playerX = 100
        self.playerY = 300
        self.playerX_change = 0
        self.playerY_change = 0

    def player1(self, x, y):
        self.game.screen.blit(self.playerImg, (x, y))

    def player_move_speed(self):
        self.playerX += self.playerX_change
        if self.playerX <= 0:
            self.playerX = 0
        elif self.playerX >= 1089:
            self.playerX = 1089

        self.playerY += self.playerY_change
        if self.playerY <= 0:
            self.playerY = 0
        elif self.playerY >= 616:
            self.playerY = 616

    def player_move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    self.playerX_change = 5
                if event.key == pygame.K_UP:
                    self.playerY_change = -5
                if event.key == pygame.K_DOWN:
                    self.playerY_change = 5
                if event.key == pygame.K_SPACE:
                    if self.game.bullet_state == "ready":
                        self.game.bulletX = self.playerX
                        self.game.bulletY = self.playerY
                        self.game.fire_bullet(self.game.bulletX, self.game.bulletY)

            if event.type == pygame.KEYUP or event.type == pygame.K_DOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.playerX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.playerY_change = 0