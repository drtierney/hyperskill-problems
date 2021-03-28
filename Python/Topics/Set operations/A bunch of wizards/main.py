gryffindor = set(input().split())
ravenclaw = set(input().split())
slytherin = set(input().split())
hufflepuff = set(input().split())

students = gryffindor | ravenclaw | slytherin | hufflepuff
print(students)
