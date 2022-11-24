from random import choice
import pyfiglet

class CGGraphics:

        def __init__(self):
            self.random_font = choice(pyfiglet.FigletFont.getFonts())

        def random_graphics(self):
            return pyfiglet.Figlet(font=self.random_font).renderText('''  SpyGlAss  ''')