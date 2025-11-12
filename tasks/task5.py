# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    input_string = input()
    characters = input_string.split()
    print(f"Код символа {characters[0]} равен {ord(characters[0])}")
    print(f"Код символа {characters[1]} равен {ord(characters[1])}")
    print(f"Код символа {characters[2]} равен {ord(characters[2])}")
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
