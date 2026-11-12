def total(*args):
    print(type(args), args)
    return sum(args)
    # total = 0
    # for number in args:
    #     total += number
    # return total
print(total(1, 2, 3, 4))

def create_user(**kwargs):
    print(type(kwargs), kwargs)

create_user(
    first_name='Blue', 
    last_name='Cambridge', 
    age=23, 
    country='Toronto'
)
