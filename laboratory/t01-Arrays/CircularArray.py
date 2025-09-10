class CircularArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.tail = -1
        self.size = 0

    def push_back(self, valor):
        if self.size == self.capacity:
            raise OverflowError("El arreglo circular está lleno")
        self.tail = (self.tail + 1) % self.capacity
        self.array[self.tail] = valor
        self.size += 1

    def pop_back(self):
        if self.size == 0:
            raise IndexError("El arreglo circular está vacío")
        valor = self.array[self.tail]
        self.array[self.tail] = None
        self.tail = (self.tail - 1 + self.capacity) % self.capacity
        self.size -= 1
        return valor

    def push_front(self, valor):
        if self.size == self.capacity:
            raise OverflowError("El arreglo circular está lleno")
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.array[self.front] = valor
        self.size += 1
        if self.size == 1:  # primer elemento
            self.tail = self.front

    def pop_front(self):
        if self.size == 0:
            raise IndexError("El arreglo circular está vacío")
        valor = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return valor

    def __str__(self):
        """Imprime los elementos en orden lógico de front a tail"""
        if self.size == 0:
            return "[]"
        elementos = []
        idx = self.front
        for _ in range(self.size):
            elementos.append(self.array[idx])
            idx = (idx + 1) % self.capacity
        return str(elementos)


# Ejemplo de uso:
if __name__ == "__main__":
    arreglo_circular = CircularArray(5)
    arreglo_circular.push_back(1)
    arreglo_circular.push_back(2)
    arreglo_circular.push_back(3)
    arreglo_circular.push_back(4)

    print(arreglo_circular)              # [1, 2, 3, 4]
    print(arreglo_circular.pop_front())  # 1
    print(arreglo_circular)              # [2, 3, 4]
    print(arreglo_circular.pop_back())   # 4
    print(arreglo_circular)              # [2, 3]
