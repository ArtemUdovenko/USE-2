from classes import Class1,Class2

def Input():
    with open("data.txt") as file:
        Data = [i.rstrip() for i in file.readlines()]
        globals()['variable_names'] = Data[0]
        globals()['table'] = [i for i in Data[1:-1]]
        globals()['expression'] = Data[-1]


def CheckInput():
    global variable_names, table, expression
    Variable_namespace = open("Variable_namespace.txt")
    var_dictionary = set(Variable_namespace.readline())
    Variable_namespace.close()
    if set(variable_names) - var_dictionary or {i for i in variable_names if variable_names.count(i) > 1}:
        return 1
    for string in table:
        if ''.join(string).replace('1', '').replace('0', '').replace('.', '') != '' or len(string) != len(variable_names) + 1:
            return 2
    for variable in variable_names:
        locals()[variable] = True
    try:
        f = eval(expression)
    except:
        return 3
    return 0

def main():
    File = open('output.txt', 'w')
    try:
        Input()
        assert(not(CheckInput()))
        for matrix in Class2.Generator1(table):
            for permutated_var_names in Class2.Generator2(variable_names):
                if Class2.Flag(matrix, permutated_var_names, expression):
                    for var in permutated_var_names:
                        print(var, end=' ')
                        File.write(var + ' ')
                    print(expression)
                    File.write(expression + '\n')
                    for string in matrix:
                        for element in string:
                            print(element,end = ' ')
                            File.write(element + ' ')
                        print()
                        File.write('\n')
    except AssertionError:
        Errors_dict = ['Incorrect variable names', 'Incorrect table', 'Incorrect expression']
        File.write(Errors_dict[CheckInput() - 1])
    except:
        File.write('Incorrect input')
    finally:
        File.close()

if __name__ == "__main__":
    main()



