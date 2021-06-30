from logging import *

class PythagorasException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class CheckRightAngle:
    """:::Check RightAngle By Pythagoras theorem:::"""

    def __init__(self, x, y, z):
        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)

    @property
    def showresult(self):
        if self.__x > self.__y and self.__x > self.__z:
            if self.__y**2 + self.__z**2 == self.__x:
                return f"{True} It's Right Angle"
            else:
                if self.__y ** 2 + self.__z ** 2 >= self.__x:
                    warning("It's Obtuse Angle")
                    return False
                elif self.__y ** 2 + self.__z ** 2 <= self.__x:
                    warning("It's Acute Angle")
                    return False

        elif self.__y > self.__x and self.__y > self.__z:
            if self.__z**2 + self.__x**2 == self.__y:
                return f"{True} It's Right Angle"
            else:
                if self.__z ** 2 + self.__x ** 2 >= self.__y:
                    warning("It's Obtuse Angle")
                    return False
                elif self.__z ** 2 + self.__x ** 2 <= self.__y:
                    warning("It's Acute Angle")
                    return False

        elif self.__z > self.__y and self.__z > self.__x:
            if self.__y**2 + self.__x**2 == self.__z:
                return f"{True} It's Right Angle"
            else:
                if self.__y**2 + self.__x**2 >= self.__z:
                    warning("It's Obtuse Angle")
                    return False
                elif self.__y**2 + self.__x**2 <= self.__z:
                    warning("It's Acute Angle")
                    return False
        else:
            raise PythagorasException("ERROR Maybe Invalid Number to calculate")


#n = CheckRightAngle(2,2,8)
#print(n.showresult)