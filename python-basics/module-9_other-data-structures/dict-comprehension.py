user = {'id': 1, 'name': 'John', 'age': 30, 'city': 'Berlin'}

filtered_user_args = list(filter(lambda value: isinstance(value, str), list(user.values())))
filtered_user_args = list(map(lambda value: str(value).upper(), filtered_user_args))

filtered_user_args_2 = {
    k: v.upper() #Expression
    for k, v in user.items() #Loop
    if isinstance(v, str) #Filter
}

print(filtered_user_args, filtered_user_args_2) 