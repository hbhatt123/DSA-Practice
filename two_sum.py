def read(n: int, book: [int], target: int) -> str:
  # using hashmap

  
    map = {}

    for i in range(n):
        a = book[i] 
        more = target - a

        if more in map:
           return 'YES'

        map[a] = i

    return 'NO'    
