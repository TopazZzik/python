def example_us(degree):
    degree = degree.replace('=', '').replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').replace('(', ' ( ').replace(')', ' ) ') 
    list_degree = degree.split()
    for i, el in enumerate(list_degree):
        if el.isdigit():
            list_degree[i] = int(el)
    while len(list_degree)>1:
        for i, el in enumerate(list_degree):
            if el == '(':
                index1 = i
            if el == ')':
                index2 = i
                break
        if '(' in list_degree:
            result = calculator(list_degree[index1+1 : index2])
            del list_degree[index1+1:index2+1]
            list_degree[index1] = result
        else:
            result = calculator(list_degree)
    return result
    

def calculator(slice):
    for i, el in enumerate(slice):
        if el == '-':
            slice[i+1]*=-1
            slice[i] = '+'
    while '*' in slice or '/' in slice:
        for i, el in enumerate(slice):
            match(el):
                case '*':
                    res = slice[i-1] * slice[i+1]
                    slice.pop(i+1)
                    slice.pop(i)
                    slice[i-1] = res
                case '/': 
                    if slice[i+1] == 0:
                        print("Ошибка: на нуль делить нельзя!")
                    res = slice[i-1] / slice[i+1]
                    slice.pop(i+1)
                    slice.pop(i)
                    slice[i-1] = res  
    while len(slice)>1 and '+' in slice: 
        for i, el in enumerate(slice):
            match(el):
                case '+':
                    res = slice[i-1] + slice[i+1]
                    slice.pop(i+1)
                    slice.pop(i)
                    slice[i-1] = res
    return res