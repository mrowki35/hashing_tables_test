class ChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return int(key) % self.size

    def insert(self, key):
        hash_value = self.hash_function(key)
        if self.table[hash_value] is None:
            self.table[hash_value] = [key]
        else:
            self.table[hash_value].insert(0, key)

    def search(self, element):
        index = self.hash_function(element)
        if element in self.table[index]:
            return index
            

    def delete(self, element):
        index = self.hash_function(element)
        if element in self.table[index]:
            self.table[index].remove(element)

    def display(self):
        output = []
        for index in range(self.size):
            if self.table[index]:
                output.append(str(self.table[index]))
            else:
                output.append('None')
        print('[' + ', '.join(output) + ']')


class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return int(key) % self.size

    def insert(self, element):
        index = self.hash_function(element)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = element

    def search(self, element):
        index = self.hash_function(element)
        for index in range(self.size):
            if self.table[index] == element:
                return index

    def delete(self, element):
        index = self.search(element)
        if index != -1:
            self.table[index] = 'Deleted'

    def display(self):
        output = []
        for index in range(self.size):
            if self.table[index] is not None:
                output.append(str(self.table[index]))
            else:
                output.append('None')
        print('[' + ', '.join(output) + ']')
        
class QuadraticProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return int(key) % self.size
        
    def resolve_collision(self, hash_value, i):
        return (hash_value + i + i**2) % self.size

    def insert(self, element):
        index = self.hash_function(element)
        i = 0
        while self.table[index] is not None:
            index = (index + i + i ** 2) % self.size
            i += 1
        self.table[index] = element

    def search(self, element):
        index = self.hash_function(element)
        i = 0
        while self.table[index] is not None:
            if self.table[index] == element:
                return index
            i += 1
            index = (index + i + i ** 2) % self.size

    def delete(self, element):
        index = self.search(element)
        if index != -1:
            self.table[index] = 'Deleted'

    def display(self):
        output = []
        for index in range(self.size):
            if self.table[index] is not None:
                output.append(str(self.table[index]))
            else:
                output.append('None')
        print('[' + ', '.join(output) + ']')

class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function_1(self, key):
        return int(key) % self.size

    def hash_function_2(self, key):
        return 1 + (int(key) % (self.size - 1))

    def resolve_collision(self, hash_value, i):
        h1 = self.hash_function_1(hash_value)
        h2 = self.hash_function_2(hash_value)
        return (h1 + i * h2) % self.size

    def insert(self, element):
        index = self.hash_function_1(element)
        i = 0
        while self.table[index] is not None:
            index = self.resolve_collision(element, i)
            i += 1
        self.table[index] = element

    def search(self, element):
        index = self.hash_function_1(element)
        i = 0
        while self.table[index] is not None:
            if self.table[index] == element:
                return index
            index = self.resolve_collision(element, i)
            i += 1


    def delete(self, element):
        index = self.search(element)
        if index != -1:
            self.table[index] = 'Deleted'

    def display(self):
        output = []
        for index in range(self.size):
            if self.table[index] is not None:
                output.append(str(self.table[index]))
            else:
                output.append('None')
        print('[' + ', '.join(output) + ']')



def afterthefirst():
    input_string = input()
    input_list = input_string.split()
    size = int(input_list[0])
    collision_method = int(input_list[1])
    elements = [element for element in input_list[2:]]

    if collision_method == 1:
        hash_table = ChainingHashTable(size)
    elif collision_method == 2:
        hash_table = LinearProbingHashTable(size)
    elif collision_method == 3:
        hash_table = QuadraticProbingHashTable(size)
    elif collision_method == 4:
        hash_table = DoubleHashingHashTable(size)

    for element in elements:
        hash_table.insert(element)

    hash_table.display()

    while True:
        command = input().split()
        if command[0] == '-1':
            break
        elif command[0] == '0':
            element = command[1]
            hash_table.insert(element)
            hash_table.display()
        elif command[0] == '1':
            element = command[1]
            index = hash_table.search(element)
            print(index)
        elif command[0] == '2':
            element = command[1]
            hash_table.delete(element)
            hash_table.display()

afterthefirst()  

