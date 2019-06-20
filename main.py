import pygame 
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
	pygame.init()
	bullets = Group()
	ai_settings = Settings()
	bg_color = (230, 230, 230)
	screen = pygame.display.set_mode((ai_settings.screen_width, 
	ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(ai_settings, screen)
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		bullets.update()
		gf.update_bullets(ai_settings, screen, ship, bullets)
		
run_game()				
	
