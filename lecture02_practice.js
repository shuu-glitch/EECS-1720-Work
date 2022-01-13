var w;

function setup() {
  createCanvas(700, 700);
  
  // make a Jitter object
  w = new Jitter();
}

function draw() {
  background(0);
  
  // update and display object
  w.update();
  w.display();
}

function Jitter() {

  // start circle in center
  this.pos = createVector(width / 2, height / 2);

  this.update = function() {
    // move circle randomly
    var vel = createVector(random(-5, 5), random(-5, 5));
    this.pos.add(vel);
  }

  this.display = function() {
    // draw jittery circle
    fill(252, 186, 3);
    strokeWeight(2);
    stroke(255);
    ellipse(this.pos.x, this.pos.y, 50, 50);
  }
}