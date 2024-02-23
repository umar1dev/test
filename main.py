def decor(function):
    def init(*args):
        mylist = [*args]
        summ, ints, strs, floats = 0, 0, 0, 0
        for x in mylist:
            summ += 1
            if type(x) is int:
                ints += 1
            elif type(x) is  str:
                strs += 1
            elif type(x) is float:
                floats += 1
        print(f'Umumiy {summ}')
        print(f'Int {ints}')
        print(f'Str {strs}')
        print(f'Float {floats}')
        svg = function(*args)
        return svg
    return init

@decor
def Umumiy_info(*args):
    mylist = [*args]
    ints, strs, floats = [], [], []
    for i in mylist:
        if type(i) is int:
            ints.append(i)
        elif type(i) is str:
            strs.append(i)
        elif type(i) is float:
            floats.append(i)
    print(f"""
Int: {ints}
Str: {strs}
Float: {floats}""")


Umumiy_info(1,2,23,54,67,123,'dasa','salom',1.2,23.45)


