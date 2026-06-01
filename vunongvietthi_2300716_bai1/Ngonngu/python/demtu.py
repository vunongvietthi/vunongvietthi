chuoi = input("Nhap mot chuoi: ")

cac_tu = chuoi.split()
so_tu = len(cac_tu)
print(f"So tu trong chuoi: {so_tu}")

print("Cac tu dai hon 5 ky tu:")
for tu in cac_tu:
    if len(tu) > 5:
        print(f"  - {tu} ({len(tu)} ky tu)")
