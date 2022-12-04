import Gen_random
class Unique(object):
    def __init__(self, items, **kwargs):
        self.arr = []
        for i in items:
            if len(kwargs) > 0 and kwargs["ignore_case"]:
                if i.lower() not in self.arr:
                    self.arr.append(i.lower())
            else:
                if i not in self.arr:
                    self.arr.append(i)

    def __next__(self):
        item = self.arr[0]
        del self.arr[0]
        return item

    def __iter__(self):
        return self
if __name__ == '__main__':
    print('TEST1')
    D = [2,2,2,2,2,1,1,1]
    t = Unique(D)
    print(t.__next__())
    print(t.__next__())
    print('TEST2')
    D = ['A','a','B','b']
    t = Unique(D,ignore_case=True)
    print(t.__next__())
    print(t.__next__())
    print('TEST3')
    D = Gen_random.gen_random(10,1,3)
    t = Unique(D)
    print(t.__next__())
    print(t.__next__())
