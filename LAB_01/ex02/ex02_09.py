def kiemtra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Nhap mot so muon ktr: "))
if kiemtra_so_nguyen_to(number):
    print(str(number) + " la so nguyen to.")
else:
    print(str(number) + " khong phai la so nguyen to.")