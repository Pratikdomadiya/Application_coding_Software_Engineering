from __future__ import annotations
from abc import abstractmethod, ABC
from typing import Any

class Builder(ABC): # REMEMBER : YOU CAN NOT CRTERE AN OBJECT OF INTERFACE DIRECTLY.
    """
        The Builder interface specifies methods for creating the different parts of
        the Product objects.
    """
    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def product_part_a(self):
        """
        first step to create product
        :return:
        """
        pass

    @abstractmethod
    def product_part_b(self):
        """
        Second step to create product; must be perform after first step
        :return:
        """
        pass

    @abstractmethod
    def product_part_c(self):
        pass


class ConcreteBuilder1(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product1()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def product_part_a(self):
        self._product.add("PartA1")

    def product_part_b(self):
        self._product.add("PartB1")

    def product_part_c(self):
        self._product.add("PartC1")


class Product1():
    def __init__(self):
        self.parts = []

    def add(self, part:Any):
        self.parts.append(part)

    def list_parts(self):
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """
        The Director is only responsible for executing the building steps in a
        particular sequence. It is helpful when producing products according to a
        specific order or configuration. Strictly speaking, the Director class is
        optional, since the client can control builders directly.
    """

    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder : Builder):
        """
                The Director works with any builder instance that the client code passes
                to it. This way, the client code may alter the final type of the newly
                assembled product.
        """
        self._builder = builder

    """
        The Director can construct several product variations using the same building steps.
    """

    def build_minimal_viable_product(self):
        self.builder.product_part_a()

    def build_full_viable_product(self):
        self.builder.product_part_a()
        self.builder.product_part_b()
        self.builder.product_part_c()


if __name__ == "__main__":
    """
        The client code creates a builder object, passes it to the director and then
        initiates the construction process. The end result is retrieved from the
        builder object.
    """

    director = Director()
    builder = ConcreteBuilder1() # The client code creates a builder object
    director.builder = builder # passes it to the director

    print("standard basic product : ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print(" \n =====================")

    print("standard FULL product : ")
    director.build_full_viable_product()
    builder.product.list_parts()

    print(" \n =====================")


    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.product_part_a()
    builder.product_part_b()
    builder.product.list_parts()
