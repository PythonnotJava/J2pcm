# Json Object converts to Protocol.Protocol is an interface implementation.
from typing import Optional, Any

from ._global import TAB, _loadJson, _JsonSupportObjReplace

def generate_protocol_codes(
    jsonData : dict,
    clsName: str,
    nullSafety: bool = False,
    headers : Optional[str] = None,
    ends : Optional[str] = None
) -> str:
    lines = []
    if not jsonData:
        lines.append(f"class {clsName}(typing.Protocol):\n{TAB}pass")
    else:
        lines.append(f"class {clsName}(typing.Protocol):")
        _types = []
        if not nullSafety:
            for key, value in jsonData.items():
                gtp = type(value).__name__
                rtp = Any if gtp == 'NoneType' else gtp
                lines.append(f'{TAB}@property')
                lines.append(f'{TAB}def {key}(self) -> {rtp}: return {_JsonSupportObjReplace[rtp]}')
                lines.append(f'{TAB}@{key}.setter')
                lines.append(f'{TAB}def {key}(self, value : {rtp}) -> None: ...\n')
        else:
            for key, value in jsonData.items():
                gtp = type(value).__name__
                rtp = Any if gtp == 'NoneType' else gtp
                lines.append(f'{TAB}@property')
                lines.append(f'{TAB}def {key}(self) -> {Optional}[{rtp}]: return {_JsonSupportObjReplace[rtp]}')
                lines.append(f'{TAB}@{key}.setter')
                lines.append(f'{TAB}def {key}(self, value : {Optional}[{rtp}]) -> None: ...\n')
        # toJson Obj
        lines.append(f'{TAB}def toJson(self) -> dict:')
        lines.append(f'{TAB}{TAB}...')
        # from Json Obj
        lines.append(f'\n{TAB}@classmethod')
        lines.append(f'{TAB}def fromJson(cls, fileName : str, encoding : str = "u8") -> "{clsName}":')
        lines.append(f'{TAB}{TAB}...')
    if headers:
        lines.insert(0, headers)
    if ends:
        lines.append(ends)
    code_str = "\n".join(lines) + "\n"
    return code_str

def generate_protocol_class(
    fileName: str,
    output: str,
    clsName: str,
    encoding: str = 'utf-8',
    nullSafety: bool = False,
    headers: Optional[str] = None,
    ends: Optional[str] = None
) -> None:
    codes = generate_protocol_codes(
        _loadJson(fileName, encoding),
        clsName,
        nullSafety,
        headers,
        ends
    )
    with open(f'{output}', 'w', encoding=encoding) as f:
        f.write(codes)
        f.close()

__all__ = ['generate_protocol_codes', 'generate_protocol_class']

if __name__ == '__main__':
    generate_protocol_class('example/mutable.json', 'example/i.py', 'Testing', nullSafety=False)
    generate_protocol_class('example/mutable.json', 'example/i_safe.py', 'Testing', nullSafety=True)