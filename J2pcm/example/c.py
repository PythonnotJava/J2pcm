import typing
class Testing:
    name : str = 'Alice'
    age : int = 25
    isStudent : bool = False
    grades : list = [90, 85, 82]
    profile : typing.Any = None
    address : dict = {'city': 'Beijing', 'K': {}}
    pos : typing.Any = None
    z : typing.Any = None

    @classmethod
    def toJson(cls) -> dict:
        target = {}
        for key in cls.__annotations__.keys():
            target[key] = getattr(cls, key)
        return target

