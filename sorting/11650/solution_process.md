2차원 리스트를 키에 따라 정렬하는 방법   
> sort에 'key' parameter 사용

    example = [[1, 2], [2, 1]]
    example.sort(key=lambda x:x[1])

> dim=1 방향으로 정렬

    example.sort(key=lambda x:(x[0], x[1]))

> key를 2개 사용: x[0] 방향으로 정렬, 같으면 x[1] 방향으로 정렬
