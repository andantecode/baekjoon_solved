### 첫 접근
- - -
    - 숫자의 크기를 기준으로 하는 rank를 알아내기 위해 set과 sort를 사용한 뒤 처음 입력받은 list의 item들의 rank를 index로 구한다. 

    - N = 1000000이므로, O(N^2)의 시간복잡도 사용 -> 시간초과 발생

> 어떻게 해야할까 고민하다가 dictionary를 사용하면, index 방식보다 빠르게 key를 통해 값을 찾아오지 않을까 생각

### 해결
- - -
    - list의 item들의 rank를 index로 구하지말고, dictionary의 key 값으로 구하자

```py
sorted_list = sorted(set(list_))
sorted_list = {sorted_list[i]: i for i in range(len(sorted_list))}
```

> 이런식으로 작성하면, item이 key값이 되어 빠르게 rank(value)에 접근 가능

### 추가
- - -
    - 시간복잡도를 고려할 때, time을 import해서 측정을 해보자
    - 또한, from random import choice를 통해 겹치지 않게 랜덤하게 선택 가능
```py
import time
from random import choice

list_ = sample(range(1, 10), 3) # 1~10중에 겹치지 않게 3개 선택

start = time.time() # 현재 시간 저장
# 시간 복잡도를 계산할 구간
end = time.time()

print(f'{end - start :.5f} sec')
```
