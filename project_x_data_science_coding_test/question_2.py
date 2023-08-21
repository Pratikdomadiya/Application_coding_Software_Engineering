class CustomClass:
    def __init__(self, first = None, second = None, third = None, fourth = None, fifth = None):
        self.first = first
        self.second =second
        self.third = third
        self.fourth = fourth
        self.fifth = fifth

    def __len__(self):
        return len([attr for attr in [self.first,self.second,self.third,self.fourth,self.fifth] if attr is not None])

    def __getattr__(self, command):
        if command not in ['first','second','third','fourth', 'fifth']:
            raise AttributeError()

#below code was given
# Create an instance of CustomClass using named arguments
obj = CustomClass(first="value1", second="value2", third="value3", fourth="value4", fifth="value5")

# Using built-in methods
print("Length:", len(obj))  # Output: Length: 5

try:
    print(obj.first)  # Accessing existing attribute
    print(obj.six)  # Accessing non-existing attribute
except AttributeError:
    print("AttributeError")