class array1:
    
    def __init__(self, max_size):
        self.max = max_size
        self.l = []

    # Create Array
    def CreateArray(self):
        print("Enter elements:")
        for i in range(self.max):
            self.l.append(int(input()))

    # Show Array
    def ShowArray(self):
        print("Array elements are:")
        for i in self.l:
            print(i, end=" ")
        print()

    # Linear Search
    def LinearSearch(self, key):
        for i in range(len(self.l)):
            if self.l[i] == key:
                return i
        return -1

    # Sorting (Bubble Sort)
    def Sorting(self):
        n = len(self.l)
        for i in range(n):
            for j in range(n-i-1):
                if self.l[j] > self.l[j+1]:
                    self.l[j], self.l[j+1] = self.l[j+1], self.l[j]
        print("Array sorted successfully")

    # Binary Search
    def BinarySearch(self, key):
        low = 0
        high = len(self.l) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.l[mid] == key:
                return mid
            elif self.l[mid] < key:
                low = mid + 1
            else:
                high = mid - 1

        return -1

# MAIN
if __name__ == "__main__":
    size = int(input("Enter size of array: "))
    
    obj = array1(size)

    obj.CreateArray()
    obj.ShowArray()

    # Linear Search
    key = int(input("Enter element to search (Linear): "))
    index = obj.LinearSearch(key)
    if index != -1:
        print("Element found at index:", index)
    else:
        print("Element not found")

    # Sorting
    obj.Sorting()
    obj.ShowArray()

    # Binary Search
    key = int(input("Enter element to search (Binary): "))
    index = obj.BinarySearch(key)
    if index != -1:
        print("Element found at index:", index)
    else:
        print("Element not found")