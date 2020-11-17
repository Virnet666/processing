def setup():
    fullScreen()
    background(0)
    
def draw():
    strokeWeight(random(1,25))
    stroke(random(0,255),random(0,255),random(0,255))
    point(random(0,width),random(0,height)) 
    saveFrame("####nooooviiiiigoood.png")
