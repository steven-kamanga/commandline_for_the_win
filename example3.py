#!/usr/bin/python3
class Base():
    """Base class"""

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances


class User(Base):
    """User class"""

    def __init__(self):
        super().__init__()
        self.id += 89


if __name__ == '__main__':
    """Docs:"""
    # for i in range(4):
    #     u = User()
    # print(u.id)
    for i in range(3):
        b = Base()
    print(b.id)
