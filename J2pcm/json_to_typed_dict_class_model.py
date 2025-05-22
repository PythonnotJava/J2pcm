# Json Object converts to Data Model Class.
from typing import Optional, Any
from ._global import _loadJson, TAB

def generate_tyed_dict_codes(
    jsonData: dict,
    clsName: str,
    total : bool = True,
    nullSafety: bool = False,
    headers : Optional[str] = None,
    ends : Optional[str] = None
) -> str:
    lines = ['import json', 'from typing import TypedDict\n', f'class {clsName}(TypedDict, total={total}):']
    if not jsonData:
        lines.append("pass")
    else:
        if nullSafety:
            for key, value in jsonData.items():
                gtp = type(value).__name__
                rtp = Any if gtp == 'NoneType' else gtp
                lines.append(f"{TAB}{key} : {Optional}[{rtp}]")
        else:
            for key, value in jsonData.items():
                gtp = type(value).__name__
                rtp = Any if gtp == 'NoneType' else gtp
                lines.append(f"{TAB}{key} : {rtp}")
    # fromJson
    lines.append(f'\ndef fromJson(fileName : str, encoding : str = "u8") -> {clsName}:')
    lines.append(f'{TAB}jsonData : dict = json.load(open(fileName, "r", encoding=encoding))')
    if nullSafety:
        lines.append(f'{TAB}return {clsName}(')
        for key in jsonData.keys():
            lines.append(f'{TAB}{TAB}{key}=jsonData.get("{key}"),')
        lines.append(f'{TAB})\n')
    else:
        lines.append(f'{TAB}return {clsName}(**jsonData)\n')
    if headers:
        lines.insert(0, headers)
    if ends:
        lines.append(ends)
    code_str = "\n".join(lines) + "\n"
    return code_str

def generate_tyed_dict_class(
    fileName: str,
    output: str,
    clsName: str,
    encoding: str = 'utf-8',
    total: bool = True,
    nullSafety: bool = False,
    headers: Optional[str] = None,
    ends: Optional[str] = None
) -> None:
    codes = generate_tyed_dict_codes(
        _loadJson(fileName, encoding),
        clsName,
        total,
        nullSafety,
        headers,
        ends
    )
    with open(f'{output}', 'w', encoding=encoding) as f:
        f.write(codes)
        f.close()

__all__ = ['generate_tyed_dict_codes', 'generate_tyed_dict_class']

if __name__ == '__main__':
    generate_tyed_dict_class('example/mutable.json', 'example/f.py', 'Testing', total=True, headers='import typing')
    generate_tyed_dict_class('example/mutable.json', 'example/g.py', 'Testing', total=False, headers='import typing')
    generate_tyed_dict_class('example/mutable_leak.json', 'example/g_safe.py', 'Testing', total=False, headers='import typing', nullSafety=True)