calls = 0

def count_calls():
    global calls
    calls += 1
    return calls


def string_info(up_, down_, str_):
    a = up_.upper()
    b = down_.lower()
    c = len(str_)

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


g = string_info('Capybara', 'Capybara', 'Capybara')
print(g)
k = string_info('Armageddon', 'Armageddon', 'Armageddon')
print(k)
n = is_contains('Urban', ['Urban', 'BaNaN', 'urBAN'])
print(n)
m = is_contains('cycle', ['recycling', 'cyclic',])
print(m)
print(calls)


