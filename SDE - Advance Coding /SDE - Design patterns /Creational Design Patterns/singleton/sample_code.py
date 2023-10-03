class Singleton:
    __instance = None

    def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self


    @staticmethod
    def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance


if __name__ == "__main__":
    s = Singleton()
    print (s)

    s1 = Singleton.getInstance()
    print (s1)

    s2 = Singleton.getInstance()
    print (s2)
