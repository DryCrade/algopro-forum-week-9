import sys
import pygame

class RocketGame:
    def __init__(self):
        pygame.init()

        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Rocket Game")

        self.rocket_image = pygame.image.load('rocket.png')  # Replace 'rocket.png' with the path to your rocket image
        self.rocket_rect = self.rocket_image.get_rect()
        self.rocket_rect.center = (self.screen_width // 2, self.screen_height // 2)

        self.speed = 5

    def run_game(self):
        while True:
            self._check_events()
            self._update_rocket()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rocket_rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rocket_rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rocket_rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rocket_rect.x += self.speed

        # Ensure the rocket stays within the screen boundaries
        self.rocket_rect.x = max(0, min(self.rocket_rect.x, self.screen_width - self.rocket_rect.width))
        self.rocket_rect.y = max(0, min(self.rocket_rect.y, self.screen_height - self.rocket_rect.height))

    def _update_rocket(self):
        pass  # In a more complex game, you might want to update the rocket's state here

    def _update_screen(self):
        self.screen.fill((255, 255, 255))  # White background
        self.screen.blit(self.rocket_image, self.rocket_rect)
        pygame.display.flip()

if __name__ == '__main__':
    game = RocketGame()
    game.run_game()
