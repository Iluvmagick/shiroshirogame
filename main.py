#if __name__ == "__main__":
import tdl
import game
import gmap

tdl.set_font('terminal16x16_gs_ro.png', greyscale=True, altLayout=False)

main = game.Game(tdl.init(20, 20, 'Game title'),  gmap.Game_map())

main.game_loop()

exit()
