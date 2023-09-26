import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230926/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    KK_img = pg.image.load("ex01-20230926/fig/3.png")
    KK_img = pg.transform.flip(KK_img, True, False)
    KK_img2 = pg.transform.rotate(KK_img, 5)
    KK_img3 = pg.transform.rotate(KK_img, 10)
    KK_img4 = KK_img2
    KK_imgs = [KK_img, KK_img2, KK_img3, KK_img4]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200
        y = tmr%40
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        if y < 10:
            screen.blit(KK_imgs[0], [300, 200])
        elif y < 20:
            screen.blit(KK_imgs[1], [300, 200])
        elif y < 30:
            screen.blit(KK_imgs[2], [300, 200])
        else:
            screen.blit(KK_imgs[3], [300, 200])
        pg.display.update()
        tmr += 1      
        clock.tick(100)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()