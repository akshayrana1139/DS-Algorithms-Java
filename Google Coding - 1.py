import sys





def solution(A):
  """Your solution goes here."""
  dic = {}
  for room in A:
    if room[0] == "+":
      if room[1:3] not in dic:
        dic[room[1:3]] = 0  
      dic[room[1:3]] += 1

  main_val = 0; rooms = []
  for key,val in dic.items():
    if val > main_val:
      main_val = val
      rooms = [key]
    elif val == main_val:
      rooms.append(key)
  return min(rooms)



print(solution(["+1A", "−1A", "+3F", "−3F", "+3F", "+8X", "+8X"]))