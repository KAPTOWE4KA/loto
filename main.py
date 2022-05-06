import loto_classes


def cont():
    input("\nНажмите любую кнопку для продолжения...")


def main():
    print(" ")
    lotogame = loto_classes.LotoGameVSBot()
    lotogame.start()

if __name__ == '__main__':
    main()
    cont()
