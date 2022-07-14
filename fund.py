a=5
def rec(num):
      if num==0 or num==1:
        return 1
      p= num+rec(num-1)
      return p
print(rec(a))  