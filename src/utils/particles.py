import pygame

class Particles:
    def __init__(self):
        self.particles = []

    def emit(self, canvas):
        self.delete_particle()
        if self.particles:
            for particle in self.particles:
                particle[0][1] += particle[2]
                particle[1] -= 0.5
                pygame.draw.circle(canvas, (0, 0, 0), particle[0], int(particle[1]))

    def add_particle(self, object):
        x = object.rect.center[0]
        y = object.rect.center[1]
        radius = 10
        direction = 0
        particle_circle = [[x, y], radius, direction]
        self.particles.append(particle_circle)

    def delete_particle(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy