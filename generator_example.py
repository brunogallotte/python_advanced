def my_gen():
    n = 1
    print('Primeiro print')
    yield n

    n += 1
    print('Segundo print')
    yield n

    n += 1
    print('Terceiro e ultimo print')
    yield n