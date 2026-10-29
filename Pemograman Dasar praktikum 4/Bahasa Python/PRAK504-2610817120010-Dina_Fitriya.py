def reverse(n):
    results = 0

    while n > 0:
        results = results * 10 + n % 10
        n = n // 10

    return results


A, B = map(int, input().split())
A = reverse(A)
B = reverse(B)
C = A + B
print(reverse(C))