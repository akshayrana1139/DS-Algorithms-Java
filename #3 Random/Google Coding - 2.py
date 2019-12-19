def solution(B):
  if "?" not in B:
    return B
  A = [x for x in B]
  v0, v1 = A[0], A[1]
  if v0 == "?" and v1 == "?":
    A[0],A[1] = "2","3"
  elif v0 == "?" and v1 != "?":
    if int(v1) > 3:
      A[0] = "1"
    else:
      A[0] = "2"
  elif v0 != "?" and v1 == "?":
    if v0 == "2":
      A[1] = "3"
    else:
      A[1] = "9"
  v0, v1 = A[3], A[4]
  if v0 == "?":
    A[3] = "5"
  if v1 == "?":
    A[4] = "9"
  return "".join([a for a in A])