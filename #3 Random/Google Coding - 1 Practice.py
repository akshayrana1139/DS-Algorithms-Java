import sys

def solution(A):
  """Your solution goes here."""
  dic = {}; dic[1] = A[0]; rows = 1 
  for i in range(1,len(A)):
    val = A[i]
    flag = True
    for key in dic:
      if dic[key] > val:
        dic[key] = val
        flag = False
        break
    if flag: 
      rows += 1
      dic[rows] = val
  return rows

def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = [int(x) for x in input[0].split(",")]
  sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
  main()
