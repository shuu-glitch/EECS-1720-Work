add_library('sound')

pointA, pointB, ch_1, ch_2 = None, None, None, None

def setup():
    size(800, 800)
    smooth()
    global pointA, pointB
    c = color(random(255), random(255), random(255))
    d = color(random(255), random(255), random(255))
    
    global ch_1, ch_2
    
    ch_1 = SinOsc(this)
    ch_1.play(0, 1)
    ch_2 = SinOsc(this)
    ch_2.play(0, 1)

def draw():
    background(0)
    stroke(255)
    noFill()
    constantFactor = 1.3
    circleSize = 20
    
    global pointA, pointB
    global ch_1, ch_2
    
    if mousePressed:
        ch_1.set(400, 1, 0, 0)
        ch_2.set(400, 1, 0, 0)
        
        for i in range (0, 20):
            for x in range (width):
                p = lerpColor(pointA, pointB, 1.0 * x / width)
                stroke(p)
                
                strokeWeight(circleSize / 25.0)
                ellipse(width / 2, height, circleSize, circleSize)
                circleSize = circleSize * constantFactor
    
        else:
            ch_1.set(0, 1, 0, 0)
            ch_2.set(0, 1, 0, 0)   
        
def mousePressed():
    global pointA, pointB
    c = color(random(255), random(255), random(255))
    d = color(random(255), random(255), random(255))
    
    ch_1.set(400, 1, 0, 0)
    ch_2.set(400, 1, 0, 0)
