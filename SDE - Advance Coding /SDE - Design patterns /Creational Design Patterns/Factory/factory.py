from __future__ import annotations
from abc import ABC, abstractmethod


class Creater(ABC):
    """
    Define the interface first

    """
    @abstractmethod
    def factory_method(self):
        """
        Creator may provide some default implementation of the abstract method
        :return:
        """
        pass

    def some_operation(self):

        #call the factory method to create a Product object
        product = self.factory_method()

        #now use the product
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result



class ConcreteCreator1(Creater):

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creater):

    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    """
    Product Interface
    """

    @abstractmethod
    def operation(self) -> str:
        pass

"""
concrete product provides various implementations of the Product Interface
"""

class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "result of the ConcreteProduct1"

class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "result of the ConcreteProduct2"


def client_code(creator: Creater)-> None:

    """
    :param creator:
    :return:
    """
    print(f"Client: I'm not aware of thr creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the class ConcreteCreator1")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the class ConcreteCreator1")
    client_code(ConcreteCreator1())
    print("\n")
