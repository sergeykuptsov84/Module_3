calls = 0

def count_calls():
    global calls
    calls += 1
    return calls


def string_info(z):
    while len(z):
        a = z.upper()
        b = z.lower()
        c = len(z)

        count_calls()
        return c, a, b


def  is_contains(string, list_to_search):
    i = str(string).lower()
    j = list([s.lower() for s in list_to_search])
    if i in j:
        i = True
    else:
        i = False

    count_calls()
    return i


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['Urban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic',]))
print(calls)

