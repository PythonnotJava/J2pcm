import json, typing

class Testing:
    def __init__(self,
        name : typing.Optional[str], 
        age : typing.Optional[int], 
        isStudent : typing.Optional[bool], 
        grades : typing.Optional[list], 
        profile : typing.Optional[typing.Any], 
        address : typing.Optional[dict], 
        pos : typing.Optional[typing.Any], 
        z : typing.Optional[typing.Any]
    ):
        self._name = name
        self._age = age
        self._isStudent = isStudent
        self._grades = grades
        self._profile = profile
        self._address = address
        self._pos = pos
        self._z = z
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value : typing.Optional[str]):
        self._name = value

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value : typing.Optional[int]):
        self._age = value

    @property
    def isStudent(self):
        return self._isStudent
    @isStudent.setter
    def isStudent(self, value : typing.Optional[bool]):
        self._isStudent = value

    @property
    def grades(self):
        return self._grades
    @grades.setter
    def grades(self, value : typing.Optional[list]):
        self._grades = value

    @property
    def profile(self):
        return self._profile
    @profile.setter
    def profile(self, value : typing.Optional[typing.Any]):
        self._profile = value

    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, value : typing.Optional[dict]):
        self._address = value

    @property
    def pos(self):
        return self._pos
    @pos.setter
    def pos(self, value : typing.Optional[typing.Any]):
        self._pos = value

    @property
    def z(self):
        return self._z
    @z.setter
    def z(self, value : typing.Optional[typing.Any]):
        self._z = value

    def toJson(self) -> dict:
        target = {}
        for key, value in self.__dict__.items():
            target[key[1:]] = value
        return target

    @classmethod
    def fromJson(cls, fileName : str, encoding : str = "u8") -> "Testing":
        jsonData : dict = json.load(open(fileName, "r", encoding=encoding))
        return Testing(
            name=jsonData.get("name"),
            age=jsonData.get("age"),
            isStudent=jsonData.get("isStudent"),
            grades=jsonData.get("grades"),
            profile=jsonData.get("profile"),
            address=jsonData.get("address"),
            pos=jsonData.get("pos"),
            z=jsonData.get("z"),
        )

print(Testing.fromJson('../mutable_leak.json').toJson())