"""
ilk 10.000 asal sayının kaç tanesi 3 ile başlar 7 ile biter.
"""

seq = list()
seq.append(2)
number = 3

while True:
    prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            prime = False
            break
    if prime:
        seq.append(number)
        if len(seq) == 10000:
            break
    number += 1

seq2 = []
for prime in seq:
    strPrime = str(prime)
    if strPrime.startswith("3") and strPrime.endswith("7"):
        seq2.append(prime)

print(seq2)
