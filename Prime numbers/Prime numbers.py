from math import sqrt, ceil


def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0 or num <= 1:
        return False

    for i in range(2, int(ceil(sqrt(num)) + 1)):
        if num % i == 0:
            return False
        if i == ceil(sqrt(num)):
            return True
    return True


sum = 0
counter = 0
for i in range(1, 51190):
    if is_prime(i):
        sum += i
        counter += 1

msg = "Jest " + str(counter) + " licz pierwszych, a ich suma to " + str(sum) + ".\n"
print(msg)
with open('odpowiedzi.txt', 'w') as f:
    f.write(msg)
