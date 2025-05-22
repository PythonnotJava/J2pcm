# Json Object converts to properties.
from typing import Optional, Any

from ._global import TAB, _loadJson

def generate_property_codes(
    jsonData: dict,
    clsName: str,
    nullSafety: bool = False,
    headers : Optional[str] = None,
    ends : Optional[str] = None
) -> str:
    lines = []
    if not jsonData:
        lines.append(f"class {clsName}:\n{TAB}pass")
    else:
        lines.append(f"class {clsName}:")
        lines.insert(0, 'import json\n')
        args = []
        _types = []
        if not nullSafety:
            for key, value in jsonData.items():
                gtp = type(value).__name__
                rtp = Any if gtp == 'NoneType' else gtp
                args.append(f'{key} : {rtp}')
                lines.append(f"{TAB}{TAB}self._{key} = {key}")
                _types.append(rtp)
        else:
            for key, value in jsonData.items():
                gtp = type(value).__name__
                rtp = Any if gtp == 'NoneType' else gtp
                args.append(f'{key} : {Optional}[{rtp}]')
                lines.append(f"{TAB}{TAB}self._{key} = {key}")
                _types.append(f'{Optional}[{rtp}]')
        lines.insert(2, f"{TAB}def __init__(self,\n{TAB}{TAB}{f', \n{TAB}{TAB}'.join(args)}\n{TAB}):")
        # property
        _type_index = 0
        for key in jsonData.keys():
            lines.append(f'{TAB}@property')
            lines.append(f'{TAB}def {key}(self):')
            lines.append(f'{TAB}{TAB}return self._{key}')
            lines.append(f'{TAB}@{key}.setter')
            lines.append(f'{TAB}def {key}(self, value : {_types[_type_index]}):')
            lines.append(f'{TAB}{TAB}self._{key} = value\n')
            _type_index += 1
        # toJson Obj
        lines.append(f'{TAB}def toJson(self) -> dict:')
        lines.append(f'{TAB}{TAB}target = {{}}')
        lines.append(f'{TAB}{TAB}for key, value in self.__dict__.items():')
        lines.append(f'{TAB}{TAB}{TAB}target[key[1:]] = value')
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

def generate_property_class(
    fileName: str,
    output: str,
    clsName: str,
    encoding: str = 'utf-8',
    nullSafety: bool = False,
    headers: Optional[str] = None,
    ends: Optional[str] = None
) -> None:
    codes = generate_property_codes(
        _loadJson(fileName, encoding),
        clsName,
        nullSafety,
        headers,
        ends
    )
    with open(f'{output}', 'w', encoding=encoding) as f:
        f.write(codes)
        f.close()

__all__ = ['generate_property_codes', 'generate_property_class']

if __name__ == '__main__':
    generate_property_class('example/mutable.json', 'example/h.py', 'Testing', nullSafety=False)
    generate_property_class('example/mutable.json', 'example/h_safe.py', 'Testing', nullSafety=True)

