class Rectangle:
    def _init_(self, length: int, width: int):
        self.length = length
        self.width = width

    def _iter_(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage
rect = Rectangle(5, 10)

for dimension in rect:
    print(dimension)