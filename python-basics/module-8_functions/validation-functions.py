def valid_password_length(password: str):
    return len(password) >= 8

print(valid_password_length('blue_is_the_best'))