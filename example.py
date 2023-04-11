#!/usr/bin/python3
class Base():
    """Base class"""
    __nb_instances = 0

    def __init__(self):
        """Init"""
        Base.__nb_instances += 1
        self.id = Base.__nb_instances


class User(Base):
    """User class"""

    def __init__(self):
        super().__init__()
        self.id.__init__
        self.id = 89


if __name__ == '__main__':
    u = User()
    print(u.id)
