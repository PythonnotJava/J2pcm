from typing import Any
import json

TAB = '    '
_JsonSupportObjReplace = {
    'int' : 0,
    'str' : "''",
    'bool' : True,
    Any : None,
    'float' : 0.0,
    'dict' : {},
    'list' : []
}

# json可以传的不可变类型
def is_mutable_type_in_json(obj):
    return type(obj) not in (bool, int, float, str, type(None))

_simpleLoader = lambda fileName, encoding : json.load(open(fileName, 'r', encoding=encoding))

def _loadJson(fileName : str, encoding : str = 'u8') -> Any:
    """take datas, ignore any exception."""
    try:
        with open(fileName, 'r', encoding=encoding) as file:
            jsonData: dict[str, Any] = json.load(file)
            file.close()
        return jsonData
    except:
        return {}

