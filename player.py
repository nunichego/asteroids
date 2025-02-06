from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, shots, x, y, radius = PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.shots = shots
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width = 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.timer <= 0:
            new_shot = Shot(self.position.x, self.position.y)
            new_shot.velocity = pygame.Vector2(0, 1)
            new_shot.velocity = new_shot.velocity.rotate(self.rotation)
            new_shot.velocity *= PLAYER_SHOOT_SPEED
            self.shots.add(new_shot)
            self.timer = PLAYER_SHOOT_COOLDOWN
        self.timer -= dt
