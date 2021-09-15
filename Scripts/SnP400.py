
a  ='a class="external text" href="http://www.nasdaq.com/symbol/achc" rel="nofollow"ACHC/a'

print(a[a.rfind('"'):-1].replace('/','').replace('"',''))
b = a[:-1]
print(b)