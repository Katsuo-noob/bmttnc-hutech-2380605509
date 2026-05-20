def dao_nguoc_list(x):
    return x[::-1]
input_list=input("Nhập một chuỗi: ")
numbers = list(map(int, input_list.split(',')))

list_dao_nguoc = dao_nguoc_list(numbers)
print("Danh sách sau khi đảo ngược:", list_dao_nguoc)