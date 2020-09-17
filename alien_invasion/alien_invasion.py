import sys
import pygame
from settings import Settings
from ship import Ship
def run_game():
    #初始化游戏
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (106,90,205)
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               sys.exit()
    #创建一搜飞船
    #ship = Ship(screen)
        screen.fill(bg_color)
        pygame.display.flip()
    #设置背景色
    #bg_color = (230,230,230)
    #开始游戏的主循环
    #while True:
        #监视键盘和鼠标事件
        #for event in pygame.event.get():
         #   if event.type == pygame.QUIT:
          #      sys.exit()
        #每次循环时都重绘屏幕
        #screen.fill(ai_settings.bg_color)
        #ship.blitme()
        #让最近绘制的屏幕可见
        #pygame.display.flip()
run_game()