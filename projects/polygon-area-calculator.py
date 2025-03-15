class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        pic = ''
        for i in range(self.height):
            if i == 0 or i == self.height - 1:
                pic += '*' * self.width + f'\n'
                continue
            pic += '*' + f"{'*':>{self.width - 1}}\n"

        return pic

    def get_amount_inside(self, shape):
        pass


class Square:
    pass


if __name__ == '__main__':
    rect = Rectangle(5, 6)
    print(rect)
    print(rect.get_picture())
