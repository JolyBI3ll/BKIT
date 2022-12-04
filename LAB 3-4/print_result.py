def print_result(func):
    def f(*args,**kwargs):
        print(func.__name__)
        output = func(*args,**kwargs)
        if type(output) == list:
            for i in output:
                print(i)
        elif type(output) == dict:
            for key in output.keys():
                print('{} = {}'.format(key,output[key]))
        else:
            print(output)
        return output
    return f

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
