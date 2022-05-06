from loto_classes import LotoBag, LotoCard


def cont():
    input("\nНажмите любую кнопку для продолжения...")


def main():
    lotobag1 = LotoBag()
    #lotobag1.debug_mark_many()

    lotocard1 = LotoCard(lotobag1.barrels[0:15], playername="Kirill")
    lotocard1.print()
    lotobag1.debug_mark_many(start=1, end=10)
    lotocard1.print()
    lotobag1.debug_print_all()
    lotobag1.debug_print_remains()


if __name__ == '__main__':
    main()
    cont()
