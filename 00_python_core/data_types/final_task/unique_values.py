from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    return {value for dictionary in lst for value in dictionary.values()}

input_data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
              {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

output = check(input_data)
print(output)