class InvalidTypeCast(Exception):
    pass

inp = "hello"

try:
    if isinstance(inp, str):
        raise InvalidTypeCast
    else:
        print("Type casting possible to int")
except InvalidTypeCast:
    print("Can't typecast to int type")