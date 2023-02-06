# класс тех, кого можно мыть
class Washable:
    def __init__(self) -> None:
        self.dirtLevel = 0

    def setDirtLevel(self, level):
        self.dirtLevel = level

    def getDirtLevel(self):
        return self.dirtLevel


# класс тех, кто может мыть
class Washer:
    def __init__(self) -> None:
        pass

    def wash(self, washable):
        if washable.getDirtLevel() > 0:
            washable.setDirtLevel(0)


# if __name__ == "__main__":
    # программа, в которой Мама моет Машу
    # masha = Washable()
    # masha.setDirtLevel(5)

    # mom = Washer()
    # mom.wash(masha)
    #
    # print(f'Mom washes Masha')
    # print(masha.getDirtLevel())
    # masha.setDirtLevel(10)
    # print(masha.getDirtLevel())
    # mom.wash(masha)
    # print(masha.getDirtLevel())
