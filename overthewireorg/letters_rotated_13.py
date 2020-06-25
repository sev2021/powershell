# all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

pp = ""  # Put password here!!!

al = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
bl = al.upper()

for i in pp:
  if i in al:
    rr += al[al.find(i) + 13]
  elif i in bl:
    rr += bl[bl.find(i) + 13]
  else:
    rr += i
    
print(rr)
