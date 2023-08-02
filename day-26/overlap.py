import pandas

data1 = pandas.read_csv("file1.txt", names=["numbers"])
data2 = pandas.read_csv("file2.txt", names=["numbers"])
common = data1.merge(data2).drop_duplicates()
result = common["numbers"].values.tolist()

# Write your code above 👆
print(result)


def convertToNumber(a):
    return int(a.strip())


with open("file1.txt") as file:
    numbers_1 = [convertToNumber(i) for i in file.readlines()]
with open("file2.txt") as file:
    numbers_2 = [convertToNumber(i) for i in file.readlines()]

common_1 = [num for num in numbers_1 if num in numbers_2]
common_2 = [num for num in numbers_2 if num in numbers_1]
result_1 = list(set(common_1 + common_2))

print(result_1)
