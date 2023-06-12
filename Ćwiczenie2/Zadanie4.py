from collections import namedtuple

Wezel = namedtuple("wezel", ["wartosc", "lewo", "prawo"])

class DrzewoBinarne:

    def __init__(self):
        self.korzen = None

    def wstaw(self, wartosc):

        if self.korzen is None:
            self.korzen = Wezel(wartosc, None, None)

        else:
            self._wstaw_rekekurencyjny_(wartosc, self.korzen)

    def _wstaw_rekekurencyjny_(self, wartosc, wezel):
        if wartosc < wezel.wartosc:

            if wezel.lewo is None:
                wezel.lewo = Wezel(wartosc, None, None)

            else:
                self._wstaw_rekekurencyjny_(wartosc, wezel.lewo)

        else:
            if wezel.prawo is None:
                wezel.prawo = Wezel(wartosc, None, None)

            else:
                self._wstaw_rekekurencyjny_(wartosc, wezel.prawo)

    def uporzadkowane(self):
        self._rekurencyjny(self.korzen)

    def _rekurencyjny(self, wezel):

        if wezel is not None:
            self._rekurencyjny(wezel.lewo)
            print(wezel.wartosc, end=" ")
            self._rekurencyjny(wezel.prawo)


drzewo = DrzewoBinarne()
drzewo.wstaw(5)
drzewo.uporzadkowane()