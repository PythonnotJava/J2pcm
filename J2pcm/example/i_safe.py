import typing


class Testing(typing.Protocol):
    @property
    def name(self) -> typing.Optional[str]: return ''
    @name.setter
    def name(self, value : typing.Optional[str]) -> None: ...

    @property
    def age(self) -> typing.Optional[int]: return 0
    @age.setter
    def age(self, value : typing.Optional[int]) -> None: ...

    @property
    def isStudent(self) -> typing.Optional[bool]: return True
    @isStudent.setter
    def isStudent(self, value : typing.Optional[bool]) -> None: ...

    @property
    def grades(self) -> typing.Optional[list]: return []
    @grades.setter
    def grades(self, value : typing.Optional[list]) -> None: ...

    @property
    def profile(self) -> typing.Optional[typing.Any]: return None
    @profile.setter
    def profile(self, value : typing.Optional[typing.Any]) -> None: ...

    @property
    def address(self) -> typing.Optional[dict]: return {}
    @address.setter
    def address(self, value : typing.Optional[dict]) -> None: ...

    @property
    def pos(self) -> typing.Optional[typing.Any]: return None
    @pos.setter
    def pos(self, value : typing.Optional[typing.Any]) -> None: ...

    @property
    def z(self) -> typing.Optional[typing.Any]: return None
    @z.setter
    def z(self, value : typing.Optional[typing.Any]) -> None: ...

    def toJson(self) -> dict:
        ...

    @classmethod
    def fromJson(cls, fileName : str, encoding : str = "u8") -> "Testing":
        ...
