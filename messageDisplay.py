import pygame

def message_display(gameDisplay, position =(0,0), text='"insert text"', text_size=20, colour=(255,255,255)):
    large_text = pygame.font.Font('freesansbold.ttf', text_size)
    text_surface = large_text.render(text, True, colour)
    text_rect = text_surface.get_rect()
    text_rect.center = position
    gameDisplay.blit(text_surface, text_rect)
