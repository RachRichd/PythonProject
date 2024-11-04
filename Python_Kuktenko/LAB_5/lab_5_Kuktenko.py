#1
hat_list = [1, 2, 3, 4, 5]  
hat_list[2] = int(input("Enter a new number to replace the middle element: "))
hat_list.pop()

print("List length after modification:", len(hat_list))
print(hat_list) 

#2

def bubble_sort(arr):
    n = len(arr)
   
    for i in range(n):
        swapped = False
# Останні i елементів вже відсортовані, тому до них не потрібно перевіряти
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
# Міняємо елементи місцями, якщо вони в неправильному порядку
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
# Якщо жодного обміну не було, список вже відсортовано
        if not swapped:
            break

arr = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", arr)

bubble_sort(arr)
print("Sorted list in ascending order:", arr)

#3
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print("The list with unique elements only:")
print(unique_list)

#4
temps = [[0.0 for h in range(24)] for d in range(31)]

for day in range(31):
    print(f"Day {day+1}: {temps[day]}")

#5
def create_chessboard():
  
    chessboard = [['_' for _ in range(8)] for _ in range(8)]
    chessboard[0][0] = 'ROOK'
    chessboard[0][7] = 'ROOK'
    chessboard[7][0] = 'ROOK'
    chessboard[7][7] = 'ROOK'

    return chessboard

def print_chessboard(chessboard):
    for row in chessboard:
        print(' '.join(row))

if __name__ == "__main__":
    board = create_chessboard()
    print_chessboard(board)
