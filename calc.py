def add(a, b): return a + b
def subtract(a, b): return a - b
 
if __name__ == "__main__":
    print("1. Add\n2. Subtract")
    choice = input("Select: ")
    n1 = int(input("Num 1: "))
    n2 = int(input("Num 2: "))
    if choice == '1': print(add(n1, n2))
