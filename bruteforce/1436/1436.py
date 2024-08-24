N = int(input())

list_ = ['666']
    
for i in range(3, 7):
    for item in list_:
        if len(item) == i:
            for j in range(0, 10):
                list_.append(item + str(j))
            for j in range(0, 10):
                list_.append(str(j) + item)

list_ = list(map(int, list_))            
list_ = list(set(list_))
list_.sort()


print(list_[N - 1])

