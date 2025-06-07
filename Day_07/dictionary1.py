# key -> key shirf tuple ko bnate h (bcoz this is immutable -> not changable)

info = {
    "key": "value",
    "name": "khushi",
    "subjects": ["python", "C", "Java"],
    "topics": ("dict", "set"),
    "age": 20,
    "is_adult": True,
}
print(info)
print(type(info))


# Access each elements of dict like this:-
print(info["name"])
print(info["subjects"])


# we can change the name and all.
info["name"] = "Aryan"  # overwrite
info["surname"] = "sharma"
print(info)


# we can also create a null dictionary and assign value in it.
null_dict = {}
null_dict["name"] = "sandhya"
print(null_dict)

