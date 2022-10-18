
import math

class SodaCan(object):
    def __int__(self, wysokosc, promien):
        self.wysokosc = wysokosc
        self.promien = promien

    def get_surface(self) -> float:
        return (2 * math.pi * self.promien * self.promien) + (2 * math.pi * self.wysokosc * self.promien)

    def get_volume(self) -> float:
        return math.pi * self.promien * self.promien * self.wysokosc



