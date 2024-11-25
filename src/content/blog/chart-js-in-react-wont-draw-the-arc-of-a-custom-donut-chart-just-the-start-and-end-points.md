---
title: Creating a Pie Chart with Canvas.js and Arc
publishDate: 2020-03-02 00:00:00
img: /assets/blog/data-visualization-with-d3.png
img_alt: Data Visualization with D3
description: Learn how to visualize your data with the power of D3.
tags:
  - Data Visualization
  - D3 Charts
  - Data Science
  - Data Analysis
  - IMAP Client
  - Advanced Workflows
  - Multiple workspaces
---


## Drawing with the arc() Function

The _arc()_ method in the _canvas API_ is used to draw circles and arcs. Let’s begin with a basic example of drawing a circle:~


```aiignore

<canvas id="myCanvas"></canvas>
<script>
  let c = document.getElementById("myCanvas");
  let ctx = c.getContext('2d');
  ctx.beginPath();
  ctx.arc(100, 75, 50, 0, 2 * Math.PI); // Draws a full circle
  ctx.stroke();
</script>

```


### Understanding Radians

Radians are the unit used for measuring angles in _arc()_. One full circle is 2π radians, which equals 360 degrees. 

To convert percentages to radians, use the formula:

```matlab
radians = 2π × %/100
```

### Setting Up a Canvas
Start by creating an HTML file and linking a JavaScript file. In the HTML file, include a <canvas> element:

```aiignore
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pie Chart</title>
</head>
<body>
  <canvas id="myCanvas"></canvas>
  <script src="script.js"></script>
  <script>
  function drawLine(ctx, startX, startY, endX, endY) {
  ctx.beginPath();
  ctx.moveTo(startX, startY);
  ctx.lineTo(endX, endY);
  ctx.stroke();
}
  function drawArc(ctx, centerX, centerY, radius, startAngle, endAngle) {
  ctx.beginPath();
  ctx.arc(centerX, centerY, radius, startAngle, endAngle);
  ctx.stroke();
}
  function drawPieSlice(ctx, centerX, centerY, radius, startAngle, endAngle, color) {
  ctx.fillStyle = color;
  ctx.beginPath();
  ctx.moveTo(centerX, centerY); // Move to the center of the circle
  ctx.arc(centerX, centerY, radius, startAngle, endAngle);
  ctx.closePath();
  ctx.fill();
}
  let myData = {
  'Classical music': 10,
  'Alternative music': 14,
  'Pop': 2,
  'Jazz': 12
};
  class Piechart {
  constructor(options) {
    this.options = options;
    this.canvas = options.canvas;
    this.ctx = this.canvas.getContext('2d');
    this.colors = options.colors;
  }

  draw() {
    let totalValue = 0;
    let colorIndex = 0;

    // Calculate total value
    for (let category in this.options.data) {
      totalValue += this.options.data[category];
    }

    // Draw each slice
    let startAngle = 0;
    for (let category in this.options.data) {
      let value = this.options.data[category];
      let sliceAngle = (2 * Math.PI * value) / totalValue;

      drawPieSlice(
        this.ctx,
        this.canvas.width / 2,
        this.canvas.height / 2,
        Math.min(this.canvas.width / 2, this.canvas.height / 2),
        startAngle,
        startAngle + sliceAngle,
        this.colors[colorIndex % this.colors.length]
      );

      startAngle += sliceAngle;
      colorIndex++;
    }
  }
}
  
</body>
</html>

```

