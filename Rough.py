import pprint
import os

pprint.pprint(os.listdir())  # nice
print()


from turtle import *

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    print(pos())
    if abs(pos()) < 1:
        break
end_fill()
done()
