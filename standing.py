tanding = int(input('masukkan jumlah pertandingan:'))
x = 0

while x < tanding:
    x += 1
    total = 0
    nilai = 0
    poin = input('pertandingan ke-{}: '.format(x))
    if poin == 'm':
        nilai = 3
    elif poin == 's':
        nilai = 1
    elif poin == 'k':
        nilai = 0
    total += nilai
print(total)
    
