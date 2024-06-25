def count_calls():
    global calls
    calls += 1
    return


def string_info(string):
    count_calls()
    future_tuple = [len(string), string.upper(), string.lower()]
    return tuple(future_tuple)


def is_contains(sample, suspicious):
    count_calls()
    test = False
    for i in suspicious:
        if sample.lower() == i.lower():
            test = True
    return test


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Hello, world!'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)

