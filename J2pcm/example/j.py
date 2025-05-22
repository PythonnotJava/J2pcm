import json

class RootObjectiveScriptsArgsD:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @classmethod
    def from_dict(cls, data: dict) -> "RootObjectiveScriptsArgsD":
        return cls(
            x=data['x'],
            y=data['y']
        )

    @classmethod
    def fromJson(cls, filename: str, encoding: str = 'u8') -> "RootObjectiveScriptsArgsD":
        with open(filename, 'r', encoding=encoding) as f:
            data = json.load(f)
        return cls.from_dict(data)

    def toJson(self) -> dict:
        return {
            "x": self.x,
            "y": self.y,
        }

class RootObjectiveScriptsArgs:
    def __init__(self, a: int, b: bool, c: list[int], d: list[RootObjectiveScriptsArgsD]):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    @classmethod
    def from_dict(cls, data: dict) -> "RootObjectiveScriptsArgs":
        return cls(
            a=data['a'],
            b=data['b'],
            c=data['c'],
            d=data['d']
        )

    @classmethod
    def fromJson(cls, filename: str, encoding: str = 'u8') -> "RootObjectiveScriptsArgs":
        with open(filename, 'r', encoding=encoding) as f:
            data = json.load(f)
        return cls.from_dict(data)

    def toJson(self) -> dict:
        return {
            "a": self.a,
            "b": self.b,
            "c": self.c,
            "d": self.d,
        }

class RootObjectiveScriptsTarget:
    def __init__(self, path: str, count: int):
        self.path = path
        self.count = count

    @classmethod
    def from_dict(cls, data: dict) -> "RootObjectiveScriptsTarget":
        return cls(
            path=data['path'],
            count=data['count']
        )

    @classmethod
    def fromJson(cls, filename: str, encoding: str = 'u8') -> "RootObjectiveScriptsTarget":
        with open(filename, 'r', encoding=encoding) as f:
            data = json.load(f)
        return cls.from_dict(data)

    def toJson(self) -> dict:
        return {
            "path": self.path,
            "count": self.count,
        }

class RootObjectiveScripts:
    def __init__(self, test: str, args: RootObjectiveScriptsArgs, Target: RootObjectiveScriptsTarget):
        self.test = test
        self.args = args
        self.Target = Target

    @classmethod
    def from_dict(cls, data: dict) -> "RootObjectiveScripts":
        return cls(
            test=data['test'],
            args=RootObjectiveScriptsArgs.from_dict(data['args']),
            Target=RootObjectiveScriptsTarget.from_dict(data['Target'])
        )

    @classmethod
    def fromJson(cls, filename: str, encoding: str = 'u8') -> "RootObjectiveScripts":
        with open(filename, 'r', encoding=encoding) as f:
            data = json.load(f)
        return cls.from_dict(data)

    def toJson(self) -> dict:
        return {
            "test": self.test,
            "args": self.args.toJson(),
            "Target": self.Target.toJson(),
        }

class RootObjective:
    def __init__(self, version: str, description: str, main: str, scripts: RootObjectiveScripts, private: bool):
        self.version = version
        self.description = description
        self.main = main
        self.scripts = scripts
        self.private = private

    @classmethod
    def from_dict(cls, data: dict) -> "RootObjective":
        return cls(
            version=data['version'],
            description=data['description'],
            main=data['main'],
            scripts=RootObjectiveScripts.from_dict(data['scripts']),
            private=data['private']
        )

    @classmethod
    def fromJson(cls, filename: str, encoding: str = 'u8') -> "RootObjective":
        with open(filename, 'r', encoding=encoding) as f:
            data = json.load(f)
        return cls.from_dict(data)

    def toJson(self) -> dict:
        return {
            "version": self.version,
            "description": self.description,
            "main": self.main,
            "scripts": self.scripts.toJson(),
            "private": self.private,
        }

class RootTarget:
    def __init__(self, path: str, count: int):
        self.path = path
        self.count = count

    @classmethod
    def from_dict(cls, data: dict) -> "RootTarget":
        return cls(
            path=data['path'],
            count=data['count']
        )

    @classmethod
    def fromJson(cls, filename: str, encoding: str = 'u8') -> "RootTarget":
        with open(filename, 'r', encoding=encoding) as f:
            data = json.load(f)
        return cls.from_dict(data)

    def toJson(self) -> dict:
        return {
            "path": self.path,
            "count": self.count,
        }

class RootTalk:
    @classmethod
    def from_dict(cls, *args) -> "RootTalk":
        return cls()

    @classmethod
    def fromJson(cls, *args) -> "RootTalk":
        return cls()

    def toJson(self, *args) -> dict:
        return {}

class Root:
    def __init__(self, Objective: RootObjective, Target: RootTarget, Plan: str, Talk: RootTalk):
        self.Objective = Objective
        self.Target = Target
        self.Plan = Plan
        self.Talk = Talk

    @classmethod
    def from_dict(cls, data: dict) -> "Root":
        return cls(
            Objective=RootObjective.from_dict(data['Objective']),
            Target=RootTarget.from_dict(data['Target']),
            Plan=data['Plan'],
            Talk=RootTalk.from_dict(data['Talk'])
        )

    @classmethod
    def fromJson(cls, filename: str, encoding: str = 'u8') -> "Root":
        with open(filename, 'r', encoding=encoding) as f:
            data = json.load(f)
        return cls.from_dict(data)

    def toJson(self) -> dict:
        return {
            "Objective": self.Objective.toJson(),
            "Target": self.Target.toJson(),
            "Plan": self.Plan,
            "Talk": self.Talk.toJson(),
        }
