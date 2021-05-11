
CANVAS_FUNCTIONS = {
  circle: function(ctx, args) {
    ctx.beginPath();
    ctx.arc(args.x, args.y, args.d/2, 0, 2*Math.PI);
    ctx.stroke();
  },
  line: function(ctx, args) {
    ctx.beginPath();
    ctx.moveTo(args.x1, args.y1);
    ctx.lineTo(args.x2, args.y2);
    ctx.stroke();
  },
  rect: function(ctx, args) {
    ctx.beginPath();
    ctx.rect(args.x, args.y, args.w, args.h);
    ctx.stroke();
  },
  clear: function(ctx, args) {
    var width = 300;
    var height = 300;
    ctx.clearRect(0, 0, width, height);
  }
}

function drawOnCanvas(canvasElement, funcName, args) {
  var ctx = canvasElement.getContext('2d');
  var func = CANVAS_FUNCTIONS[funcName];

  var scalex = canvasElement.width/300;
  var scaley = canvasElement.height/300;

  ctx.save();
  ctx.scale(scalex, scaley);
  func(ctx, args);
  ctx.restore();
}
