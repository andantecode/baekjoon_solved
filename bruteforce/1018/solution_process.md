내가 파이썬을 아직 완전히 모른다는 걸 깨달았다.   
2차원 배열에서

```py
list_ = [[1, 2, 3], [4, 5, 6]]
list_[1:, 1:] # numpy에서 사용하는 slicing 방식이라 불가능
```

> __코테는 외부 라이브러리를 사용하면 안되기에 2차원 배열을 슬라이싱 하기 위해선
for-loop를 돌며 열 단위로 슬라이싱 한 뒤 합쳐주는 작업이 필요하다.__

```py
list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = []

for row in range(1, len(list_)):
    temp_list = list_[row][1:]
    print(temp_list)
    new_list.append(temp_list)

print(new_list) # [[5, 6], [8, 9]]
```

또한, 2차원 배열을 그 구조대로 출력해서 확인하려면
pprint 라이브러리를 사용한다.
```py
import pprint   
pprint.pprint('new_list')
```