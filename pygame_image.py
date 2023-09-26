import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230926/fig/pg_bg.jpg")
    KK_img = pg.image.load("ex01-20230926/fig/3.png")
    KK_img = pg.transform.flip(KK_img, True, False)
    KK_img2 = pg.transform.rotate(KK_img, 10)
    KK_imgs = [KK_img, KK_img2]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img, [1650-x, 0])
        screen.blit(KK_imgs[tmr%2], [300, 200])
        pg.display.update()
        tmr += 1      
        clock.tick(100)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()