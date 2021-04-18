while True:                                                 #condition untuk memastikan input sesuai yang di inginkan
    try:
        x = []                                              #list untuk mengakomodasi input
        xQuota = int(input('Masukkan Jumlah Inputan: '))    #total input yang di inginkan
        for i in range(xQuota):
            xNumbers = int(input('Masukkan Angka: '))       #variable untuk setiap input
            x.append(xNumbers)
    except ValueError:
        print('Invalid Input!')
        continue

    if xNumbers <= 0:
        print('Invalid Input!')
        continue
    elif xNumbers > 100:
        print('Invalid Input!')
    elif xNumbers == float:
        print('Invalid Input!')
    else:
        break

n = len(x)                                  #menghitung panjang list
for i in range(n):                          #rumus untuk memastikan setiap angka lebih besar atau lebih kecil dari angka berikutnya
    for j in range(0, n-i-1):
        if x[j] > x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]

print(x)