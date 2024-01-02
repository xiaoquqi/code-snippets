def myfunc(name=None, age=None, hobbies=[]):
    print(name)
    print(age)
    print(hobbies)

kwargs = {
    "name": "Ray",
    "age": 23,
    "hobbies": ["soccer", "bowling"]
}

myfunc(**kwargs)
