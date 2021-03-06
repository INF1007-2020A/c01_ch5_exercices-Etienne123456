#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    
    return (float(input())**2)**(1/2)


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOPQ', 'ack'
    result=[]
    for letter in prefixes:
        result.append(letter+suffixes)
    return result


def prime_integer_summation() -> int:
    return 0


def factorial(number: int) -> int:
    return 0


def use_continue() -> None:
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
