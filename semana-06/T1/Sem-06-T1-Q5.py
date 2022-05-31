n1 = float(input().strip())
n2 = float(input().strip())
n3 = float(input().strip())
media = (n1 + n2 + n3) / 3
if n3 > 8:
    media = media + 1
    if media > 10:
        media = 10
        print(media)
    else:
        print(media)
else:
    print(media)
