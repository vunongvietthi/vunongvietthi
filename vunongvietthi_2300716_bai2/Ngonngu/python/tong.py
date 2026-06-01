N = int(input("Nhap so nguyen duong N: "))
tong = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        tong += i
print(f"Tong cac so chan tu 1 den {N} la: {tong}")
