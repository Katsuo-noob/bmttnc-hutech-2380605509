input_str = input("Nhap X y :")
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]
multidim_list = [[0 for j in range(colNum)] for i in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multidim_list[row][col] = row * col
print(multidim_list)