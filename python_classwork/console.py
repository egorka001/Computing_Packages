def rec_star(n, count_str):
    a = ""
    if count_str > 0:
        rec_in(a, n)
    else:
        return
    rec_star(n, count_str - 1)

def rec_in(a, n):
    if n > 0:
        a = a + "*"
    else:
        print(a)
        return
    rec_in(a, n - 1)

n = int(input("Input N: "))

print("iter")
print(("*" * n + "\n") * n)

print("rec")
rec_star(n, n)

