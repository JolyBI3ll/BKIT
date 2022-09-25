import sys
import math

def get_coef(index, prompt):
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        while True:
            print(prompt)
            coef_str = input()
            try:
                coef = float(coef_str)
                break
            except:
                print('Попробуйте еще раз!')
    return coef


def get_rootskvur(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        result.append(root1)
        result.append(root2)
    return result


def get_rootsbikvur(roots):
    result = []
    len_roots = len(roots)
    for i in range(len_roots):
        if roots[i] > 0:
            t1 = math.sqrt(roots[i])
            t2 = -(math.sqrt(roots[i]))
            result.append(t1)
            result.append(t2)
    return result


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    if a == 0 and b == 0:
        if c == 0:
            print('Бесконечное количество корней!')
            exit()
        else:
            print('Нет корней')
    if a == 0:
        if c == 0:
            print('Один корень:', 0)
            exit()
        else:
            rootskvur = get_rootskvur(a, b, c)
            len_roots = len(rootskvur)
            if len_roots == 0:
                print('Нет корней')
            elif len_roots == 1:
                print('Два корня: {}'.format(rootskvur[0]))
            elif len_roots == 2:
                print('Четыре корня: {} и {}'.format(rootskvur[0], rootskvur[1]))
            exit()
    if b == 0:
        if c == 0:
            print('Один корень: ', 0)
            exit()
    rootskvur = get_rootskvur(a, b, c)
    rootsbikvur = get_rootsbikvur(rootskvur)
    len_roots = len(rootsbikvur)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(rootsbikvur[0], rootsbikvur[1]))
    elif len_roots == 4:
        print('Четыре корня: {} и {} и {} и {}'.format(rootsbikvur[0], rootsbikvur[1],rootsbikvur[2],rootsbikvur[3]))

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

    # Пример запуска
    # qr.py 1 0 -4