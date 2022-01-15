let bubble1, bubble2, bubble3;

function setup() {
  createCanvas(650, 650);
  bubble1 = new Bubble();
  bubble2 = new Bubble();
  bubble3 = new Bubble();
  
  // print(bubble.x, bubble.y);
}

function draw() {
  background(0);
  
  bubble1.move();
  bubble1.show();
  
  bubble2.move();
  bubble2.show();
  
  bubble3.move();
  bubble3.show();
}

class Bubble {
  constructor() {
    this.x = random(width);
    this.y = random(height);
  }
  
  move() {
    this.x = this.x + random(-5, 5);
    this.y = this.y + random(-5, 5);
  }
  
  show() {
    stroke(255);
    strokeWeight(3);
    fill(random(255), random(255), random(255));
    ellipse(this.x, this.y, 50, 50);
  }
  
}