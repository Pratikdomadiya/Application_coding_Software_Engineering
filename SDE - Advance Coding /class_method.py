# Instance, Class, and Static Methods — An Overview
import math


class MyClass:

    '''
    Through the self parameter, instance methods can freely access attributes and other
    methods on the same object. This gives them a lot of power when it comes to modifying
    an object’s state.

    Not only can they modify object state, instance methods can also access the class
    itself through the self.__class__ attribute. This means instance methods can also
    modify class state.
    '''
    def method(self):
        return 'instance method called'


    """
    - cls parameter that points to the class—and not the object instance
    - Because the class method only has access to this cls argument, it 
    can’t modify object instance state. That would require access to self. 
    However, class methods can still modify class state that applies across 
    all instances of the class.
    """
    @classmethod #decorators
    def class_method(cls):
        return('class method called')


    """
    Therefore a static method can neither modify object state nor class state. 
    Static methods are restricted in what data they can access - 
    and they’re primarily a way to namespace your methods.
    """
    @staticmethod #decorators
    def staticmethod():
        return('static method called')



"""
obj = MyClass()
print(obj.method())
''' By the way, instance methods can also access the class itself through the self.__class__ attribute.'''

print(obj.class_method())
'''Calling classmethod() showed us it doesn’t have access to the <MyClass instance> object, but only to the <class MyClass> object'''

print(obj.staticmethod())

#  let’s take a look at what happens when we attempt to call
#  these methods on the class itself - without creating an object instance beforehand:

print(MyClass.class_method())
print(MyClass.staticmethod())
print(MyClass.method()) # bound to object/instances only not class
# print(MyClass.__method__())

"""

# bare-bones Pizza class

# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     def __repr__(self):
#         return 'Pizza(%r)' % self.ingredients
#
# obj = Pizza(['cheese','tomatoes'])
# print(obj)

# Delicious Pizza Factories With @classmethod
# If you’ve had any exposure to pizza in the real world you’ll know that there are many delicious variations available:
# Pizza(['mozzarella', 'tomatoes'])
# Pizza(['mozzarella', 'tomatoes', 'ham', 'mushrooms'])
# Pizza(['mozzarella'] * 4)

# The Italians figured out their pizza taxonomy centuries ago, and so these delicious types of pizzas all have their own names.
# We’d do well to take advantage of that and give the users of our Pizza class a better interface for creating the pizza objects they crave.
# A nice and clean way to do that is by using class methods as factory functions for the different kinds of pizzas we can create:

#updated Pizza class
class Pizza:
    def __init__(self, ingredients, radius):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self): # a built-in method in Python that returns a string representation of an object
        return f'Pizza({self.ingredients!r})'

    '''
    Note how I’m using the cls argument in the margherita and prosciutto factory 
    methods instead of calling the Pizza constructor directly.
    
    This is a trick you can use to follow the Don’t Repeat Yourself (DRY) principle. 
    If we decide to rename this class at some point we won’t have to remember 
    updating the constructor name in all of the classmethod factory functions.
    
    Python only allows one __init__ method per class. Using class methods it’s 
    possible to add as many alternative constructors as necessary. 
    '''
    @classmethod
    def margherita(cls):
        return cls(['mozzarella','tomatoes'],2) #cls represent Pizza class itself

    @classmethod
    def prociutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'],4) #cls represent Pizza class itself

    # static method
    def area(self):
        return self.circle_area(self.radius)
    @staticmethod
    def circle_area(r):
        return pow(r,2)*math.pi


# Now, what can we do with these factory methods? Let’s try them out:
print(Pizza.margherita()) # Pizza(['mozzarella', 'tomatoes'])
print(Pizza.prociutto()) # Pizza(['mozzarella', 'tomatoes', 'ham'])

m = Pizza.margherita()
p = Pizza.prociutto()

print(m.area())
print(p.area())

#access static method via class itself
print(Pizza.circle_area(4))

