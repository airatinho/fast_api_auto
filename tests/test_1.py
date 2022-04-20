import requests
def test_get(type:str):
    """test GET request
    type : dilers or cars"""
    resp = requests.get(f"http://127.0.0.1:8000/{type}")
    return resp

def test_post(data:dict,type:str):
    """test POST request
        data : input dict data
        type : dilers or cars"""

    resp = requests.post(
        f"http://127.0.0.1:8000/{type}",
        json=data
    )
    return resp


def test_put(data: dict, type: str,id:int):
    """test PUT request
        data : new data
        type : dilers or cars
        id : unique id of element"""

    resp = requests.post(
        f"http://127.0.0.1:8000/{type}/{id}",
        json=data
    )
    return resp


def test_delete(type: str,id:int):
    """test DELETE request
        type : dilers or cars
        id : unique id of element"""

    resp = requests.delete(
        f"http://127.0.0.1:8000/{type}/{id}"
    )
    return resp