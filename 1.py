""""
money = 0

while True:
coin = int(input())
if coin == -1:
  break
money += coin

money %= 60
coins = [200,100,50,20,10,5,2,1]

coins_given = 0
while money != 0:
greatest = 0
for s in coins:
  if s <= money:
    greatest = s
    break
money -= greatest
coins_given += 1

print(coins_given)
"""


pairs = int(input())
chains = int(input())

lights = []

for _ in range(chains):
  inp = input().split(' ')
  num1 = inp[0]
  num2 = inp[1]
  part = sorted([num1, num2])
  done = False
for s in lights:
  if not done:
    for b in s:
      if b.count(num1) > 0 or b.count(num2) > 0:
        s.append(part)
        done = True
        break
  
  else: break
          
    
if not done:
  lights.append([part])
print(lights)

max_l = -1
for s in lights:
if len(s) > max_l:
  max_l = len(s)
  print(max_l)
