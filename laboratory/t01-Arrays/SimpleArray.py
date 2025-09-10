class SimpleArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def push_back(self, data):
        """Inserta al final (O(1))"""
        if self.is_full():
            raise OverflowError("Array lleno")
        self.array[self.size] = data
        self.size += 1

    def push_front(self, data):
        """Inserta al inicio (O(n)) porque hay que desplazar elementos"""
        if self.is_full():
            raise OverflowError("Array lleno")
        for i in range(self.size, 0, -1):  # desplazar a la derecha
            self.array[i] = self.array[i - 1]
        self.array[0] = data
        self.size += 1

    def pop_back(self):
        """Elimina y devuelve el último elemento (O(1))"""
        if self.is_empty():
            raise IndexError("Array vacío")
        value = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        return value

    def pop_front(self):
        """Elimina y devuelve el primer elemento (O(n)) porque hay que desplazar"""
        if self.is_empty():
            raise IndexError("Array vacío")
        value = self.array[0]
        for i in range(1, self.size):  # desplazar a la izquierda
            self.array[i - 1] = self.array[i]
        self.array[self.size - 1] = None
        self.size -= 1
        return value

    def insert(self, data, position):
        """Inserta en posición arbitraria (O(n))"""
        if self.is_full():
            raise OverflowError("Array lleno")
        if position < 0 or position > self.size:
            raise IndexError("Posición fuera de rango")
        for i in range(self.size, position, -1):
            self.array[i] = self.array[i - 1]
        self.array[position] = data
        self.size += 1

    def remove(self, position):
        """Elimina en posición arbitraria (O(n))"""
        if self.is_empty():
            raise IndexError("Array vacío")
        if position < 0 or position >= self.size:
            raise IndexError("Posición fuera de rango")
        value = self.array[position]
        for i in range(position + 1, self.size):
            self.array[i - 1] = self.array[i]
        self.array[self.size - 1] = None
        self.size -= 1
        return value

    def __str__(self):
        """Imprime solo los elementos válidos"""
        return str(self.array[:self.size])


# Ejemplo de uso
if __name__ == "__main__":
    arr = SimpleArray(5)
    arr.push_back(10)
    arr.push_back(20)
    arr.push_front(5)
    print(arr)  # [5, 10, 20]
    arr.insert(15, 2)
    print(arr)  # [5, 10, 15, 20]
    print(arr.pop_front())  # 5
    print(arr.pop_back())   # 20
    print(arr)              # [10, 15]
