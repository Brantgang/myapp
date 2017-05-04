class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width=value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,values):
        self._height=values

    @property
    def resolution(self):
        return self._width * self._height




s=Screen()
s.height=1024
s.width=10
print(s.resolution)
