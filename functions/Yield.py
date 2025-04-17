# write a function that generates even nos upto a certain limit

my_list = []


def even_number_to_limit(n):
    for i in range(0 , n + 1 , 2):
        my_list.append(i)
    return my_list


for num in even_number_to_limit(10):
    print(num)
