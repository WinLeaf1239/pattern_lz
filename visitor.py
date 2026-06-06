class KeyBord:
    def __init__(self, cost):
        self.cost = cost

    def permissionKey(self,visitor):
        return visitor.permisKeyBord(self) #Для того, кто попросит, дадим наш объект
    
class Mouse:
    def __init__(self, costik):
        self.costik = costik

    def permissionMou(self,visitor):
        return visitor.permisMouse(self)
    
class Visitor:
    def permisKeyBord(self, bord):
        return bord.cost * 2
    
    def permisMouse(self, mouse):
        return mouse.costik * 3
    

def main():
    keybord = KeyBord(100)
    mouse = Mouse(150)
    visitor = Visitor()
    key1 = keybord.permissionKey(visitor)
    mou1 = mouse.permissionMou(visitor)

    print(f'Пользователь купил клавиатур и мышек на сумму: {key1 + mou1} рублей')


if __name__ == "__main__":
    main()