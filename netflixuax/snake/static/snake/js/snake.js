document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById("gameCanvas");
    if (!canvas) {
      console.error("No se encontró el elemento canvas con id 'gameCanvas'.");
      return;
    }
    const ctx = canvas.getContext("2d");
  
    let box = 20;
    let snake = [];
    snake[0] = { x: 9 * box, y: 10 * box };
    let food = {
      x: Math.floor(Math.random() * 19 + 1) * box,
      y: Math.floor(Math.random() * 19 + 1) * box,
    };
    let direction;
    let score = 0;
  
    document.addEventListener("keydown", setDirection);
  
    function setDirection(event) {
      if (event.keyCode === 37 && direction !== "RIGHT") direction = "LEFT";
      else if (event.keyCode === 38 && direction !== "DOWN") direction = "UP";
      else if (event.keyCode === 39 && direction !== "LEFT") direction = "RIGHT";
      else if (event.keyCode === 40 && direction !== "UP") direction = "DOWN";
    }
  
    function drawGame() {
      ctx.fillStyle = "#000";
      ctx.fillRect(0, 0, canvas.width, canvas.height);
  
      for (let i = 0; i < snake.length; i++) {
        ctx.fillStyle = i === 0 ? "#e50914" : "#fff";
        ctx.fillRect(snake[i].x, snake[i].y, box, box);
      }
  
      ctx.fillStyle = "#00ff00";
      ctx.fillRect(food.x, food.y, box, box);
  
      let snakeX = snake[0].x;
      let snakeY = snake[0].y;
  
      if (direction === "LEFT") snakeX -= box;
      if (direction === "UP") snakeY -= box;
      if (direction === "RIGHT") snakeX += box;
      if (direction === "DOWN") snakeY += box;
  
      if (snakeX === food.x && snakeY === food.y) {
        score++;
        food = {
          x: Math.floor(Math.random() * 19 + 1) * box,
          y: Math.floor(Math.random() * 19 + 1) * box,
        };
      } else {
        snake.pop();
      }
  
      let newHead = { x: snakeX, y: snakeY };
  
      if (
        snakeX < 0 ||
        snakeY < 0 ||
        snakeX >= canvas.width ||
        snakeY >= canvas.height ||
        collision(newHead, snake)
      ) {
        clearInterval(game);
        alert("Game Over! Your score: " + score);
      }
  
      snake.unshift(newHead);
    }
  
    function collision(head, array) {
      for (let i = 0; i < array.length; i++) {
        if (head.x === array[i].x && head.y === array[i].y) {
          return true;
        }
      }
      return false;
    }
  
    let game = setInterval(drawGame, 100);
  });
  