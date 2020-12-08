def setup():
    fullScreen()
    background(0)
def draw():
    strokeWeight(random(1,25))
    viiiiiv =color(random(0,255),random(0,255),random(0,255))
    fill(viiiiiv)
    stroke(viiiiiv)
    point(random(0,width),random(0,height)) 
    rect(random(0,width),random(0,height),random(0,25),random(0,25))
