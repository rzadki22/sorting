from abc import ABC, abstractmethod
import json

import algorithms as alg

REVERSED = "reversed"
ORDERED = "ordered"
RANDOM = "random"

class SortingAlgorithm(ABC):
   def __init__(self):
        self.comparisons = 0

   def gt(self, value_1, value_2) -> bool:
       self.comparisons += 1
       return value_1 > value_2

   def gte(self, value_1, value_2) -> bool:
       self.comparisons += 1
       return value_1 >= value_2

   def lt(self, value_1, value_2) -> bool:
       self.comparisons += 1
       return value_1 < value_2

   def lte(self, value_1, value_2) -> bool:
       self.comparisons += 1
       return value_1 <= value_2

   def eq(self, value_1, value_2) -> bool:
       self.comparisons += 1
       return value_1 == value_2

   @abstractmethod
   def sort(self, values):
       pass


class BubbleSortNaive(SortingAlgorithm):
    def sort(self, values):
        self.comparisons = 0
        length = len(values)
        n = 0
        while n < length :
            for index in range(0, length - 1):
                if self.gt( values[index], values[index + 1] ):
                    values[index], values[index + 1] = values[index + 1], values[index]
            n += 1

class BubbleSort(SortingAlgorithm):
    def sort(self, values):
        self.comparisons = 0
        length = len(values)
        n = 0
        swapped_occured = True
        while n < length and swapped_occured:
            swapped_occured = False
            for index in range(0, length - 1):
                if self.gt( values[index], values[index + 1] ):
                    values[index], values[index + 1] = values[index + 1], values[index]
                    swapped_occured = True
            n += 1

class InsertSort(SortingAlgorithm):
    def sort(self, values):
        self.comparisons = 0
        length = len(values)
        for index in range(1, length):
            value = values[index]
            j = index - 1
            while j >= 0 and self.lt(value, values[j]):
                values[j + 1], values[j] = values[j], values[j + 1]
                j = j - 1

def simulate(algorithm: SortingAlgorithm, max_length):
    """
    Przyjmuje algorytm, za pomocą którego zostanie wykonane sortowanie
    list: uporządkowanej, odwrotnie uporządkowanej i losowo uporządkowanej o długościach
    od 1 do max_lenght.
​
    {'ordered': {1: y, 2: x, ..., 1000: z}
     'reversed': {1: y, 2: x, ..., 1000: z}
     'random': {1: y, 2: x, ..., 1000: z}
    }
​
    Kroki do wykonania:
    - utwórz słownik wynikowy o formacie:
      {'ordered': {}
      'reversed': {}
      'random': {}}
    - Pętla for length in range(10, max_length, 10)
      - wygeneruj trzy listy wykorzystując wcześniej zdefiniowane funkcje dla aktualnej wartości length:
        * ordered_list
        * reversed_list
        * random_list
      - dla każde z nich wykonaj sortowanie algorytmem przekazanym jako argument: algorithm
      - do słownika wynikowego pod odpowiedni klucz (losowa, uporządkowane, odwrotnie uporządkowana)
        dodaj nowy wynik gdzie klucz będzie długością aktualnie sortowanej listy  a wartością liczba wykonanych porównań w czasie sortowania.
​
    Zapisz słownik do obiektu pickle o nazwie: f'{algorithm.__class__.__name__}_max_length.pickle'
    Przykładowa zapisana nazwa pliku to: BubbleSort_1000.pickle
​   """

    result = {
        ORDERED: {},
        RANDOM: {},
        REVERSED: {},

    }

    for length in range(1, max_length + 1):
        ordered_list = alg.generate_ordered_list(length)
        algorithm.sort(ordered_list)
        result[ORDERED][length] = algorithm.comparisons
        reversed_list = alg.generate_reversed_list(length)
        algorithm.sort(reversed_list)
        result[REVERSED][length] = algorithm.comparisons
        random_list = alg.generate_random_list(length, 0, 10)
        algorithm.sort(random_list)
        result[RANDOM][length] = algorithm.comparisons


    filename = f"{algorithm.__class__.__name__}_{max_length}.json"
    with open(filename, "w") as f:
        json.dump(result, f, indent=2, sort_keys=True)

if __name__ == "__main__":

    a = BubbleSortNaive()
    simulate(a, 300)

    b = BubbleSort()
    simulate(b, 300)

    c = InsertSort()
    simulate(c, 300)

