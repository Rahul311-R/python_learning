from collections import deque

q = deque()
q.append(10)
q.append(20)
q.append(30)
q.append(40)
print(q)
de = q.popleft()
print(de)
print(q)
fr = q[0]
print(fr)