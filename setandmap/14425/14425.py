n, m = list(map(int, input().split(' ')))

set_ = set()

for i in range(n):
    set_item = input()
    set_.add(set_item)

list_ = list(set_)
dict_ = {list_[i]: i for i in range(len(list_))}

count = 0

for i in range(m):
    target = input()
    if dict_.get(target) is not None:
        count += 1

print(count)