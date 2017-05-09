from copy import copy


class Tree:
    """ drzewo biarne, konstruktor przyjmuje klucz i wartosc w sumie nic nadzwyczajnego """

    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.right = None
        self.left = None

    def getKey(self):
        return copy(self.key)

    def getValue(self):
        return copy(self.value)

    def getRight(self):
        """zwraca kopie prawego elementu """
        return copy(self.right)

    def getLeft(self):
        """zwraca kopie lewego elementu """
        return copy(self.left)

    def putRight(self, key, value=None):
        """ wstawienie elementu na prawo """
        self.right = Tree(key, value)

    def putLeft(self, key, value=None):
        """ wstawienie elementu na lewo """
        self.left = Tree(key, value)

    def checkRight(self):
        """ jezeli wezel ma element na prawo zwroci true w przeciwnym  wypadku false"""
        if self.getRight() == None:
            return False
        else:
            return True

    def checkLeft(self):
        """ jezeli wezel ma element na lewo zwroci true w przeciwnym  wypadku false"""
        if self.getLeft() == None:
            return False
        else:
            return True


    def display(self, level=1):
        """ wyswietlanie  w konsoli drzewa"""
        print '-'*level + str(self.getValue())

        if self.checkLeft()==True:
            
            self.getLeft().display(level+1)
        if self.checkRight()==True:
            
            self.getRight().display(level+1)

    def insert(self, key, value):
        """ wstawianie nowego wezla do dorzewa, jezeli taki wezel juz istnieje to wstawiany jest na lewo """


        done = False
        tmp = self

        while(done == False):
            if tmp.key >= key:
                #to the left
                if tmp.checkLeft() == True:
                    tmp = tmp.left
                else:
                    tmp.putLeft(key, value)
                    done = True

            else:
                #to the right
                if tmp.checkRight()==True:
                    tmp = tmp.right
                else:
                    tmp.putRight(key, value)
                    done=True




'''
drzewo = Tree(100, 'a')
drzewo.insert(100,'c')
drzewo.insert(102, 'f')
drzewo.insert(2, 'k')
drzewo.display()


a=3
b = copy(a)
b = 2
print a


drzewo.putLeft(99,'c')
drzewo.putRight(111,'f')
drzewo.display()        
'''