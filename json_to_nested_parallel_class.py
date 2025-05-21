# When child-json is nested in parent-json or multiple json in parallel.
from typing import *

from _global import TAB, _loadJson

def _base_class_no_file(
    jsonData: dict,
    clsName: str,
    clsAttr: bool = False,
    nullSafety : bool = False
) -> str:
    lines = []
    if not jsonData:
        lines.append(f"class {clsName}:\n{TAB}pass")
    else:
        lines.append(f"class {clsName}:")
        if clsAttr:
            if not nullSafety:
                for key, value in jsonData.items():
                    gtp = type(value).__name__
                    rtp = Any if gtp == 'NoneType' else gtp
                    lines.append(f"{TAB}{key} : {rtp} = {repr(value)}")
            else:
                for key, value in jsonData.items():
                    gtp = type(value).__name__
                    rtp = Any if gtp == 'NoneType' else gtp
                    lines.append(f"{TAB}{key} : {Optional}[{rtp}] = {repr(value)}")
            # toJson Obj
            lines.append(f"\n{TAB}@classmethod")
            lines.append(f'{TAB}def toJson(cls) -> dict:')
            lines.append(f'{TAB}{TAB}target = {{}}')
            lines.append(f'{TAB}{TAB}for key in cls.__annotations__.keys():')
            lines.append(f'{TAB}{TAB}{TAB}target[key] = getattr(cls, key)')
            lines.append(f'{TAB}{TAB}return target\n')
        else:
            lines.insert(0, 'import json')
            args = []
            if not nullSafety:
                for key, value in jsonData.items():
                    gtp = type(value).__name__
                    rtp = Any if gtp == 'NoneType' else gtp
                    args.append(f'{key} : {rtp}')
                    lines.append(f"{TAB}{TAB}self.{key} = {key}")
            else:
                for key, value in jsonData.items():
                    gtp = type(value).__name__
                    rtp = Any if gtp == 'NoneType' else gtp
                    args.append(f'{key} : {Optional}[{rtp}]')
                    lines.append(f"{TAB}{TAB}self.{key} = {key}")
            lines.insert(2, f"{TAB}def __init__(self,\n{TAB}{TAB}{f', \n{TAB}{TAB}'.join(args)}\n{TAB}):")
            # toJson Obj
            lines.append(f'\n{TAB}def toJson(self) -> dict:')
            lines.append(f'{TAB}{TAB}target = {{}}')
            lines.append(f'{TAB}{TAB}for key, value in self.__dict__.items():')
            lines.append(f'{TAB}{TAB}{TAB}target[key] = value')
            lines.append(f'{TAB}{TAB}return target')
            # from Json Obj
            lines.append(f'\n{TAB}@classmethod')
            lines.append(f'{TAB}def fromJson(cls, fileName : str, encoding : str = "u8") -> "{clsName}":')
            lines.append(f'{TAB}{TAB}jsonData : dict = json.load(open(fileName, "r", encoding=encoding))')
            if nullSafety:
                lines.append(f'{TAB}{TAB}return {clsName}(')
                for key in jsonData.keys():
                    lines.append(f'{TAB}{TAB}{TAB}{key}=jsonData.get("{key}"),')
                lines.append(f'{TAB}{TAB})\n')
            else:
                lines.append(f'{TAB}{TAB}return cls(**jsonData)\n')

    return "\n".join(lines) + "\n"

