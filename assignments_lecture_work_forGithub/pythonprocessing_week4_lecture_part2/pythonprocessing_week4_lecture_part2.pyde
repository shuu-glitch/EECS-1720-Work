pointA, pointB = None, None

def setup():
  size(800, 800)
  global pointA, pointB
  pointA = color(random(255), random(255), random(255))
  pointB = color(random(255), random(255), random(255))


def draw():
  global pointA, pointB
  for x in range(width): # loop through every x
    p = lerpColor(pointA, pointB, 1.0 * x/width)
    stroke(p)
    line(x, 0, x, height)


def mousePressed():
  global pointA, pointB
  pointA = color(random(255), random(255), random(255))
  pointB = color(random(255), random(255), random(255))
