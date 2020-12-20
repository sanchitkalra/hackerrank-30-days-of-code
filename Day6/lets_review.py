n = int(input())

for k in range(n):
    string = input()
    even = ""
    odd = ""
    for j in range(len(string)):
        if j%2==0:
            even += string[j]
        else:
            odd += string[j]
    print(even + " " + odd)