class Wezel:
    def __init__(self, punkt, lewo=None, prawo=None):
        self.punkt = punkt
        self.lewo = lewo
        self.prawo = prawo

class Kd:
    def __init__(self):
        self.ko = None

    def insert(self, punkt):
        self.ko = self._in_rc(punkt, self.ko, 0)

    def _in_rc(self, punkt, wz, dp):
        if wz is None:
            return Wezel(punkt)

        k = len(punkt)
        xa = dp % k

        if punkt[xa] < wz.point[xa]:
            wz.left = self._in_rc(punkt, wz.left, dp + 1)
        else:
            wz.right = self._in_rc(punkt, wz.right, dp + 1)

        return wz

    def search(self, tg):
        return self._se_rc(tg, self.ko, 0)

    def _se_rc(self, tg, wz, dp):
        if wz is None:
            return None

        k = len(tg)
        xa = dp % k

        if tg == wz.point:
            return wz.point

        if tg[xa] < wz.point[xa]:
            return self._se_rc(tg, wz.left, dp + 1)
        else:
            return self._se_rc(tg, wz.right, dp + 1)