var c = document.getElementById("playground");
var dotButton = document.getElementById("circle");
var dvdButton = document.getElementById("dvd");
var stopButton = document.getElementById("stop");

var ctx = c.getContext("2d");
ctx.fillStyle = "green";

var requestID;

var clear = (e) => {
  // e.preventDefault();
  ctx.clearRect(0, 0, c.width, c.height);
};

var dvdLogoSetup = function() {
  window.cancelAnimationFrame(requestID);

  var rectWidth = 50;
  var rectHeight = 50;

  var rectX = Math.random() * (c.width - rectWidth);
  var rectY = Math.random() * (c.height - rectHeight);

  var xVel = 2;
  var yVel = 2;

  var logo = new Image();
  logo.src = "logo_dvd.jpg";

  var dvdLogo = function() {
    clear(); //different here
    ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
    if (rectX <= 0 || rectX >= c.width - rectWidth) {
      xVel *= -1;
    }
    if (rectY <= 0 || rectY >= c.height - rectHeight) {
      yVel *= -1;
    }
    rectX += xVel;
    rectY += yVel;
    requestID = window.requestAnimationFrame(dvdLogo);
  };
  dvdLogo();
};

var radius = 0;
var growing = true;

var drawDot = () => {
  window.cancelAnimationFrame(requestID);

  clear();
  ctx.beginPath();
  ctx.arc(250, 250, radius, 0, 2 * Math.PI);
  ctx.fill();
  ctx.stroke();

  if (growing) {
    radius++;
  }
  if (!growing) {
    radius--;
  }
  if (radius == 250) {
    growing = false;
  }
  if (radius == 0) {
    growing = true;
  }

  requestID = window.requestAnimationFrame(drawDot);
};

var stopIt = () => {
  console.log(requestID);
  window.cancelAnimationFrame(requestID);
};

dotButton.addEventListener("click", drawDot);
dvdButton.addEventListener("click", dvdLogoSetup);
stopButton.addEventListener("click", stopIt);
