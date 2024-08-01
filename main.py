def factorial_recursive(n):
    if n < 0:
        return
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

num = int(input("Введіть число для обчислення факторіала: "))
print(f"Факторіал {num} = {factorial_recursive(num)}")