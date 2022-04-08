# Python Driver Code

def solve(n: int) -> str:
  n=str(n)
  n=list(n)
  mid=int(len(n)//2)
  if len(n)%2==0:
    p="".join(n[mid:])
    q="".join(n[mid:])
   else:
      p="".join(n[mid+1:])
      q="".join(n[:mid])
    if int(q)>int(p):
      return("magic number")
    else:
      return("normal number")
  


# The following snippet reads the input in the required format. 
# Just complete the solve function above. 

T = int(input())
for i in range(T):
  test_case = input()
  answer = solve(test_case)
  print(answer)
