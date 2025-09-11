class DynamicArray:
    """A dynamic array class akin to a simplified Python list (no ctypes)."""

    def __init__(self):
        self._n = 0                 # número de elementos válidos
        self._capacity = 1          # capacidad inicial (>0)
        self._A = [None] * self._capacity

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        return self._A[k]

    def __str__(self):
        return str([self._A[i] for i in range(self._n)])

    # --- API pública ---

    def capacity(self):
        """Devuelve la capacidad interna (útil para ver redimensionamientos)."""
        return self._capacity

    def append(self, obj):
        """Añade al final. Amortizado O(1)."""
        if self._n == self._capacity:
            self._resize(max(1, 2 * self._capacity))
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, value):
        """Inserta en índice k desplazando a la derecha. O(n)."""
        if not 0 <= k <= self._n:
            raise IndexError("index out of range")
        if self._n == self._capacity:
            self._resize(max(1, 2 * self._capacity))
        # desplazar [k.._n-1] una posición a la derecha
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        """Elimina la primera ocurrencia de 'value'. O(n)."""
        for k in range(self._n):
            if self._A[k] == value:
                # desplazar a la izquierda desde k+1
                for j in range(k + 1, self._n):
                    self._A[j - 1] = self._A[j]
                self._A[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError("value not found")

    # --- utilidades internas ---

    def _resize(self, c):
        """Redimensiona a capacidad c."""
        B = [None] * c
        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = c


# --------------------- demo / main ---------------------

def main():
    arr = DynamicArray()
    print("Inicial:", arr, "len=", len(arr), "cap=", arr.capacity())

    # append
    for x in (10, 20, 30):
        arr.append(x)
    print("Tras append 10,20,30:", arr, "len=", len(arr), "cap=", arr.capacity())

    # getitem
    print("Elemento en índice 1:", arr[1])  # 20

    # insert al inicio, al medio y al final
    arr.insert(0, 5)        # [5,10,20,30]
    print("insert(0,5):", arr, "len=", len(arr), "cap=", arr.capacity())

    arr.insert(2, 15)       # [5,10,15,20,30]
    print("insert(2,15):", arr, "len=", len(arr), "cap=", arr.capacity())

    arr.insert(len(arr), 40)  # al final
    print("insert(len,40):", arr, "len=", len(arr), "cap=", arr.capacity())

    # remove primera ocurrencia
    arr.remove(20)          # [5,10,15,30,40]
    print("remove(20):", arr, "len=", len(arr), "cap=", arr.capacity())

    # crecer más para ver _resize en acción
    for x in (50, 60, 70, 80):
        arr.append(x)
    print("Tras más append:", arr, "len=", len(arr), "cap=", arr.capacity())

    # remove de valor inexistente (muestra la excepción)
    try:
        arr.remove(999)
    except ValueError as e:
        print("Esperado:", e)

if __name__ == "__main__":
    main()
