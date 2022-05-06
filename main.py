import loto_classes


def cont():
    input("\nНажмите любую кнопку для продолжения...")


def main():
    print(" ")
    lotogame = loto_classes.LotoGameVSBot()
    result = lotogame.start()
    print("Спс за игру")

if __name__ == '__main__':
    main()
    cont()
