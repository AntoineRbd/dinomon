import pygame
import pytmx
import pyscroll
pygame.init()

from src.player import Player

class Game:
    def __init__(self):
        # game board creation
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Dinomon")

        # Load  map
        tmx_data = pytmx.util_pygame.load_pygame('map/map_dinomon.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Generate player
        player_position = tmx_data.get_object_by_name('player spawn')
        self.player = Player(player_position.x, player_position.y)

        # Layers group
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)

    def run(self):
        # Game loop
        running = True

        self.group.update()
        self.group.center(self.player.rect)
        self.group.draw(self.screen)
        pygame.display.flip()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
        pygame.quit()