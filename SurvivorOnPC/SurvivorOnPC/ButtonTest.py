#!/usr/bin/python
 
import pygame
pygame.Colour = pygame.Color # British English, please

import random

import argparse



class App:


  def __init__(self):

    args = self.args()
    self.debug = args.debug
    self.bg = pygame.Colour(args.bg)
    self.fg = pygame.Colour(args.fg)
    self.red = pygame.Colour(args.hl)
    self.flags = pygame.FULLSCREEN
    self.pointer = False
    self.font = [ args.font, args.font_size ]
    self.unicode = args.unicode
    self.dice_font = [ args.dice_font, args.dice_font_size ]
    self.dice_n = args.dice
    self.sound = args.sound
    self.specials = []
    if args.game == 'floundering':
      # special throws for "The Merry Game of Floundering"
      self.specials.append((lambda d: len(set(d)) == 1, 'Double!'))
      self.specials.append((lambda d: set(d) == set((1, 6)), '6 and 1'))

    self.dice = self.dice_n[:]
    self.rolls = 0


 
  def args(self):
    arg = argparse.ArgumentParser(description='Dice Emulator.')
    arg.add_argument('-fg', '--foreground', dest='fg', default=DEFAULTS['fg'], help='foreground colour (default: {d})'.format(d=DEFAULTS['fg']))
    arg.add_argument('-bg', '--background', dest='bg', default=DEFAULTS['bg'], help='background colour (default: {d})'.format(d=DEFAULTS['bg']))
    arg.add_argument('-hl', '--highlight', dest='hl', default=DEFAULTS['hl'], help='highlight colour (default: {d})'.format(d=DEFAULTS['hl']))
    arg.add_argument('-fn', '--font', dest='font', default=DEFAULTS['font'], help='font (default: {d})'.format(d=DEFAULTS['font']))
    arg.add_argument('-fs', '--font-size', dest='font_size', type=int, default=DEFAULTS['font-size'], help='font size (default: {d}'.format(d=DEFAULTS['font-size']))
    arg.add_argument('-u', '--unicode', dest='unicode', action='store_true', default=True, help='enable Unicode dice characters (default: enabled)')
    arg.add_argument('-a', '--ascii', dest='unicode', action='store_false', help='enable numeric dice characters (default: disabled)')
    arg.add_argument('-dfn', '--dice-font', dest='dice_font', default=DEFAULTS['dice-font'], help='dice font (default: {d})'.format(d=DEFAULTS['dice-font']))
    arg.add_argument('-dfs', '--dice-font-size', dest='dice_font_size', type=int, default=DEFAULTS['dice-font-size'], help='dice font size (default: {d})'.format(d=DEFAULTS['dice-font-size']))
    arg.add_argument('-s', '--sound', dest='sound', default=DEFAULTS['sound'], help='roll sound (default: {d})'.format(d=DEFAULTS['sound']))
    arg.add_argument('-g', '--game', dest='game', choices=('floundering', 'none'), default=DEFAULTS['game'], help='dice game (default: {d})'.format(d=DEFAULTS['game']))
    arg.add_argument('-d', '--debug', dest='debug', action='store_true', help='enable debug (default: disabled)')
    arg.add_argument(metavar='N', dest='dice', nargs='*', type=int, default=DEFAULTS['dice'], help='dice number and sides (default: {d})'.format(d=DEFAULTS['dice']))
    return arg.parse_args()



  def init(self):

pygame.init()
    pygame.display.set_caption('Dice')
    info = pygame.display.Info()
    self.width = info.current_w
    self.height = info.current_h
 
 
class GameMenu():
    def __init__(self, screen, items, bg_color=(0,0,0), font=None, font_size=30,
                    font_color=(255, 255, 255)):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
 
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
 
        self.items = items
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
 
        self.items = []
        for index, item in enumerate(items):
            label = self.font.render(item, 1, font_color)
 
            width = label.get_rect().width
            height = label.get_rect().height
 
            posx = (self.scr_width / 2) - (width / 2)
            # t_h: total height of text block
            t_h = len(items) * height
            posy = (self.scr_height / 2) - (t_h / 2) + (index * height)
 
            self.items.append([item, label, (width, height), (posx, posy)])
 
    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)
 
    text = self.dice_font.render(dice, 1, self.fg)
    self.screen.blit(text, [(w - text.get_width()) / 2, h1 + (h - 2*h1 - text.get_height()) / 2])
 
            # Redraw the background
            self.screen.fill(self.bg_color)
 
            for name, label, (width, height), (posx, posy) in self.items:
                self.screen.blit(label, (posx, posy))
 
            pygame.display.flip()
 
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if bs.collidepoint(pos):
                    #run other program
                    print('start game')
                elif bh.collidepoint(pos):
                    pygame.display.set_caption('How to play Menu')
                    hm = HelpMenu(screen)
                    
                elif bc.collidepoint(pos):
                    mainloop = False
                    sys.exit()
 
if __name__ == "__main__":
    # Creating the screen
    screen = pygame.display.set_mode((640, 480), 0, 32)
 
    menu_items = ('Start', 'Quit')
 
    pygame.display.set_caption('Game Menu')
    gm = GameMenu(screen, menu_items)
    gm.run()