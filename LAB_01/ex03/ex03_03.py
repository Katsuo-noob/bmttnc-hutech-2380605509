def tao_tuple_tu_list(lst):
    return tuple(lst)

input_list = input("Nhập một danh sách các phần tử (cách nhau bằng dấu phẩy): ").split(',')
numbers = list(map(int, input_list))  # Chuyển đổi các phần tử thành số nguyên
my_tuple = tao_tuple_tu_list(numbers)
print("Tuple được tạo từ danh sách:", my_tuple)