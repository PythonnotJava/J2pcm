import typing


class Testing(typing.Protocol):
    @property
    def name(self) -> str: return ''
    @name.setter
    def name(self, value : str) -> None: ...

    @property
    def age(self) -> int: return 0
    @age.setter
    def age(self, value : int) -> None: ...

    @property
    def isStudent(self) -> bool: return True
    @isStudent.setter
    def isStudent(self, value : bool) -> None: ...

    @property
    def grades(self) -> list: return []
    @grades.setter
    def grades(self, value : list) -> None: ...

    @property
    def profile(self) -> typing.Any: return None
    @profile.setter
    def profile(self, value : typing.Any) -> None: ...

    @property
    def address(self) -> dict: return {}
    @address.setter
    def address(self, value : dict) -> None: ...

    @property
    def pos(self) -> typing.Any: return None
    @pos.setter
    def pos(self, value : typing.Any) -> None: ...

    @property
    def z(self) -> typing.Any: return None
    @z.setter
    def z(self, value : typing.Any) -> None: ...

    def toJson(self) -> dict:
        ...

    @classmethod
    def fromJson(cls, fileName : str, encoding : str = "u8") -> "Testing":
        ...
