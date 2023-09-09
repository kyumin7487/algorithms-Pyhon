a = int(input())
count = 0

for i in range(50):
    count = count + i

    if count >= a:
        print(i)
        break
