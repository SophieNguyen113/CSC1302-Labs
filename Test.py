def solution(a):
    people = []
    for i in a:
        if i > 0:
            people.append(i)
    
    people.sort()
    
    return people
    
a = [-1, 150, 190, 170, -1, -1, 160, 180]
solution(a)