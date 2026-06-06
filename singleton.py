class Singleton:
    def __new__(self):
        self.static = "static"

def main():
    a = Singleton()
    b = Singleton()
    print(f'Класс является одиночкой? {a is b}')

if __name__ == "__main__":
    main()