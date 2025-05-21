# Json Object converts to Data Model Class.
from typing import Optional, Any

from _global import TAB, _loadJson

def generate_base_class_codes(
    jsonData: dict,
    clsName: str,
    clsAttr: bool = False,
    nullSafety : bool = False,
    headers : Optional[str] = None,
    ends : Optional[str] = None
) -> str:
    """
    # generate base class by json datas.If the value is empty, it is declared as [Any] type.
    """
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
    if headers:
        lines.insert(0, headers)
    if ends:
        lines.append(ends)
    code_str = "\n".join(lines) + "\n"
    return code_str

def generate_base_class(
    fileName: str,
    output : str,
    clsName: str,
    clsAttr: bool = False,
    encoding: str = 'utf-8',
    nullSafety : bool = False,
    headers : Optional[str] = None,
    ends : Optional[str] = None
) -> None:
    codes = generate_base_class_codes(
        _loadJson(fileName, encoding),
        clsName,
        clsAttr,
        nullSafety,
        headers,
        ends
    )
    with open(f'{output}', 'w', encoding=encoding) as f:
        f.write(codes)
        f.close()

if __name__ == '__main__':
    generate_base_class(
        'mutable.json',
        'example/a.py',
        'Testing',
        False,
        headers="import typing",
        ends='__all__ = ["Testing"]'
    )
    generate_base_class(
        'mutable.json',
        'example/b.py',
        'Testing',
        True,
        headers='"""Testing is a testing class."""\nimport typing\n', ends='__all__ = ["Testing"]'
    )
    generate_base_class(
        'mutable.json',
        'example/a_safe.py',
        'Testing',
        False,
        headers="import typing",
        ends='__all__ = ["Testing"]',
        nullSafety=True
    )
    generate_base_class(
        'mutable.json',
        'example/b_safe.py',
        'Testing',
        True,
        headers='"""Testing is a testing class."""\nimport typing\n', ends='__all__ = ["Testing"]',
        nullSafety=True
    )