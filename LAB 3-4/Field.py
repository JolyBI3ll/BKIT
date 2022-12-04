goods = [
    {'title': 'Cover', 'price': 2000, 'color': 'green'},
    {'title': 'Divan dlya otdixa', 'price': 5300, 'color': 'black'}
]
def field(items, *args):
    res = []
    for i in range(0, len(items)):
        for j in range(0, len(args)):
            if(items[i].get(args[j]) != None):
                res.append(items[i].get(args[j]))
    return res
print(field(goods,'title','price'))
