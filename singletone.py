
class Product:
    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = object.__new__(cls)
        cls._instance.id = args[1]
        cls._instance.name = args[2]
        return cls._instance

prod1 = Product('oil',1)
prod2 = Product('Atta',2)


print(id(prod1))
print(id(prod2))
