import json


# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
def save_to_json(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        data = {
            "parameters": {
                "args": args,
                "kwargs": kwargs
            },
            "result": result
        }
        with open("result_dz9_4.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
    return wrapper


@save_to_json
def test_function(a, b):
    return a + b