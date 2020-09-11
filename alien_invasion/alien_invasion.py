import sys
import pygame
def run_game():
    #初始化游戏
    pygame.init()
    screen = pyname.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get()