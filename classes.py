import itertools
class Class1:
    @staticmethod
    def Aux_generator(x):
        for i in range(2 ** x):
            yield '0' * (x - len(bin(i)[2:])) + bin(i)[2:]
    @staticmethod
    def check(matrix):
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                if matrix[i] == matrix[j]: return False 
        return True
class Class2(Class1):
    @staticmethod
    def Generator1(matrix):
        counter = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '.': counter += 1
        for substitution in Class1.Aux_generator(counter):
            aux_matrix = [[j for j in i] for i in matrix]
            pointer = 0
            for i in range(len(aux_matrix)):
                for j in range(len(aux_matrix[i])):
                    if aux_matrix[i][j] == '.':
                        aux_matrix[i][j] = substitution[pointer]
                        pointer += 1
            if Class1.check(aux_matrix):
                yield aux_matrix
            else:
                continue
    @staticmethod
    def Generator2(string):
        for permutated_string in itertools.permutations(string):
            yield list(permutated_string)
    @staticmethod
    def Flag(matrix, permutated_var_names, expression):
        for string in matrix:
            expected_value = bool(int(string[-1]))
            for i in range(len(string) - 1):
                locals()[permutated_var_names[i]] = bool(int(string[i]))
            if expected_value != eval(expression):
                return False
        return True





