from typing import Any, Optional
from collections import OrderedDict

from ._global import TAB, _loadJson

class_defs = OrderedDict()

def to_camel_case(path: list[str]) -> str:
    return ''.join(part[0].upper() + part[1:] for part in path)

def infer_type(value: Any, path: list[str]) -> str:
    if value is None:
        return "Any"
    elif isinstance(value, bool):
        return "bool"
    elif isinstance(value, int):
        return "int"
    elif isinstance(value, float):
        return "float"
    elif isinstance(value, str):
        return "str"
    elif isinstance(value, list):
        if not value:
            return "list[Any]"
        first = value[0]
        if isinstance(first, dict):
            class_name = to_camel_case(path)
            return f"list[{class_name}]"
        return f"list[{infer_type(first, path)}]"
    elif isinstance(value, dict):
        class_name = to_camel_case(path)
        return class_name
    return "Any"

def register_class(path: list[str], obj: dict):
    class_name = to_camel_case(path)
    if class_name in class_defs:
        return

    fields = []
    for key, value in obj.items():
        field_path = path + [key]
        typ = infer_type(value, field_path)
        fields.append((key, typ, value))

        # register nested class
        if isinstance(value, dict):
            register_class(field_path, value)
        elif isinstance(value, list) and value and isinstance(value[0], dict):
            register_class(field_path, value[0])
    class_defs[class_name] = fields

def generate_class_code(name: str, fields: list[tuple[str, str, Any]]) -> str:
    lines = [f"class {name}:"]

    if not fields:
        # 空类的默认方法实现
        lines += [
            f"{TAB}@classmethod",
            f"{TAB}def from_dict(cls, *args) -> \"{name}\":",
            f"{TAB}{TAB}return cls()\n",
            f"{TAB}@classmethod",
            f"{TAB}def fromJson(cls, *args) -> \"{name}\":",
            f"{TAB}{TAB}return cls()\n",
            f"{TAB}def toJson(self, *args) -> dict:",
            f"{TAB}{TAB}return {{}}\n"
        ]
        return "\n".join(lines)

    # 正常类的 __init__
    args = ", ".join(f"{k}: {t}" for k, t, _ in fields)
    lines.append(f"{TAB}def __init__(self, {args}):")
    for k, _, _ in fields:
        lines.append(f"{TAB}{TAB}self.{k} = {k}")
    lines.append("")

    # from_dict
    lines.append(f"{TAB}@classmethod")
    lines.append(f"{TAB}def from_dict(cls, data: dict) -> \"{name}\":")

    init_lines = []
    for k, t, v in fields:
        if t.startswith("list[") and "from_dict" in t:
            inner = t[5:-1]
            init_lines.append(f"{TAB}{TAB}{TAB}{k}=[{inner}.from_dict(i) for i in data['{k}']]")
        elif "from_dict" in t or t in class_defs:
            init_lines.append(f"{TAB}{TAB}{TAB}{k}={t}.from_dict(data['{k}'])")
        else:
            init_lines.append(f"{TAB}{TAB}{TAB}{k}=data['{k}']")
    lines.append(f"{TAB}{TAB}return cls(\n" + ",\n".join(init_lines) + "\n        )\n")

    # fromJson
    lines.append(f"{TAB}@classmethod")
    lines.append(f"{TAB}def fromJson(cls, filename: str, encoding: str = 'u8') -> \"{name}\":")
    lines.append(f"{TAB}{TAB}with open(filename, 'r', encoding=encoding) as f:")
    lines.append(f"{TAB}{TAB}{TAB}data = json.load(f)")
    lines.append(f"{TAB}{TAB}return cls.from_dict(data)\n")

    # toJson
    lines.append(f"{TAB}def toJson(self) -> dict:")
    lines.append(f"{TAB}{TAB}return {'{'}")
    for k, t, v in fields:
        if t.startswith("list[") and "from_dict" in t:
            lines.append(f"{TAB}{TAB}{TAB}\"{k}\": [i.toJson() for i in self.{k}],")
        elif "from_dict" in t or t in class_defs:
            lines.append(f"{TAB}{TAB}{TAB}\"{k}\": self.{k}.toJson(),")
        else:
            lines.append(f"{TAB}{TAB}{TAB}\"{k}\": self.{k},")
    lines.append(f"{TAB}{TAB}{'}'}\n")

    return "\n".join(lines)

def _generate_nested_parallel_codes(
    jsonData: dict,
    root_class_name: str = "Root"
) -> str:
    class_defs.clear()
    register_class([root_class_name], jsonData)
    code = ["import json\n"]
    for name, fields in class_defs.items():
        code.append(generate_class_code(name, fields))
    return "\n".join(code)

def generate_nested_parallel_codes(
    jsonData: dict,
    root_class_name: str = "Root",
    headers: Optional[str] = None,
    ends: Optional[str] = None
) -> str:
    class_defs.clear()
    register_class([root_class_name], jsonData)
    code = []
    if headers:
        code.append(headers)
    code.append("import json\n")
    for name, fields in class_defs.items():
        code.append(generate_class_code(name, fields))
    if ends:
        code.append(ends)
    return "\n".join(code)

def generate_nested_parallel_class(
    fileName: str,
    output: str,
    root_class_name: str = "Root",
    encoding: str = 'utf-8',
    headers: Optional[str] = None,
    ends: Optional[str] = None
) -> None:
    codes = generate_nested_parallel_codes(
        _loadJson(fileName, encoding),
        root_class_name,
        headers,
        ends
    )
    with open(output, "w", encoding=encoding) as f:
        f.write(codes)
        f.close()

__all__ = ['generate_nested_parallel_class', 'generate_nested_parallel_codes']

if __name__ == "__main__":
    generate_nested_parallel_class('example/nested_parallel.json', 'example/j.py')
    generate_nested_parallel_class('example/immutable.json', 'example/k.py')