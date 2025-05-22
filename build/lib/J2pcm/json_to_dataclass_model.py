# Json Object converts to dataclass.
from typing import Optional, Any

from ._global import TAB, _loadJson, is_mutable_type_in_json
from .json_to_base_class_model import generate_base_class_codes

def generate_data_class_codes(
    jsonData: dict,
    clsName: str,
    nullSafety: bool = False,
    headers : Optional[str] = None,
    ends : Optional[str] = None,
    **kwargs
) -> str:
    # null值被Any类型代替并且设置为待传入参数，根据dataclass的意见将该类参数放置前面
    # 如果json中有可变类型，将会被强制转换为普通的类属性
    for value in jsonData.values():
        if is_mutable_type_in_json(value):
            return generate_base_class_codes(jsonData, clsName, True, nullSafety, headers, ends)
    lines = ['from dataclasses import dataclass\n']
    if kwargs:
        params = ', '.join(f'{k}={v!r}' for k, v in kwargs.items())
        lines.append(f'@dataclass({params})')
    else:
        lines.append('@dataclass')
    if not jsonData:
        lines.append(f"class {clsName}:\n{TAB}pass")
    else:
        lines.append(f"class {clsName}:")
        lines.insert(0, 'import json')
        _insert_pos = 4
        if not nullSafety:
            for key, value in jsonData.items():
                gtp = type(value).__name__
                if gtp != 'NoneType':
                    lines.append(f"{TAB}{key} : {gtp} = {repr(value)}")
                else:
                    lines.insert(_insert_pos, f'{TAB}{key} : {Any}')
                    _insert_pos += 1
        else:
            for key, value in jsonData.items():
                gtp = type(value).__name__
                if gtp != 'NoneType':
                    lines.append(f"{TAB}{key} : {Optional}[{gtp}] = {repr(value)}")
                else:
                    lines.insert(_insert_pos, f'{TAB}{key} : {Any}')
                    _insert_pos += 1
        # toJson Obj
        lines.append(f'\n{TAB}def toJson(self) -> dict:')
        lines.append(f'{TAB}{TAB}return self.__dict__')
        # from Json Obj
        lines.append(f'\n{TAB}@classmethod')
        lines.append(f'{TAB}def fromJson(cls, fileName : str, encoding : str = "u8") -> "{clsName}":')
        lines.append(f'{TAB}{TAB}jsonData : dict = json.load(open(fileName, "r", encoding=encoding))')
        if not nullSafety:
            lines.append(f'{TAB}{TAB}return cls(**jsonData)\n')
        else:
            lines.append(f'{TAB}{TAB}return cls(')
            for key in jsonData.keys():
                lines.append(f'{TAB}{TAB}{TAB}{key}=jsonData.get("{key}"),')
            lines.append(f'{TAB}{TAB})\n')

    if headers:
        lines.insert(0, headers)
    if ends:
        lines.append(ends)
    code_str = "\n".join(lines) + "\n"
    return code_str

def generate_data_class(
    fileName: str,
    output : str,
    clsName: str,
    encoding: str = 'utf-8',
    nullSafety: bool = False,
    headers : Optional[str] = None,
    ends : Optional[str] = None,
    **kwargs
) -> None:
    codes = generate_data_class_codes(
        _loadJson(fileName, encoding),
        clsName,
        nullSafety,
        headers,
        ends,
        **kwargs
    )
    with open(f'{output}', 'w', encoding=encoding) as f:
        f.write(codes)
        f.close()

__all__ = ['generate_data_class_codes', 'generate_data_class']

if __name__ == '__main__':
    generate_data_class('example/mutable.json', 'example/c.py', "Testing", headers='import typing')
    generate_data_class('example/immutable.json', 'example/d.py', 'Testing', headers='import typing')
    generate_data_class('example/immutable.json', 'example/e.py', 'Testing', headers='import typing', frozen=True)
    generate_data_class('example/mutable_leak.json', 'example/c_safe.py', 'Testing', nullSafety=True)