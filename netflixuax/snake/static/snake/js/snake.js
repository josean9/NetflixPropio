document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById("gameCanvas");
    const ctx = canvas.getContext("2d");

    const box = 20; // Tamaño de los bloques
    let snake = [{ x: 9 * box, y: 10 * box }]; // Posición inicial de la serpiente
    let food = {
        x: Math.floor(Math.random() * (canvas.width / box)) * box,
        y: Math.floor(Math.random() * (canvas.height / box)) * box,
    };
    let direction;
    let score = 0;
    let highScore = localStorage.getItem("highScore") || 0;

    const snakeHeadImg = new Image();
    snakeHeadImg.src = "/static/snake/images/snake_head.png";

    const foodColorSelector = document.getElementById("foodColorSelector");

    window.addEventListener("keydown", (event) => {
        if (["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"].includes(event.key)) {
            event.preventDefault();
        }
    });

    document.addEventListener("keydown", setDirection);

    function setDirection(event) {
        if (event.keyCode === 37 && direction !== "RIGHT") direction = "LEFT";
        else if (event.keyCode === 38 && direction !== "DOWN") direction = "UP";
        else if (event.keyCode === 39 && direction !== "LEFT") direction = "RIGHT";
        else if (event.keyCode === 40 && direction !== "UP") direction = "DOWN";
    }

    function drawBackground() {
        for (let x = 0; x < canvas.width; x += box) {
            for (let y = 0; y < canvas.height; y += box) {
                ctx.fillStyle = (x / box + y / box) % 2 === 0 ? "#333" : "#444";
                ctx.fillRect(x, y, box, box);
            }
        }
    }

    function drawGame() {
        drawBackground();

        for (let i = 0; i < snake.length; i++) {
            if (i === 0) {
                if (snakeHeadImg.complete) {
                    ctx.drawImage(snakeHeadImg, snake[i].x, snake[i].y, box, box);
                } else {
                    ctx.fillStyle = "red";
                    ctx.fillRect(snake[i].x, snake[i].y, box, box);
                }
            } else {
                ctx.fillStyle = "#00ff00";
                ctx.beginPath();
                ctx.arc(
                    snake[i].x + box / 2,
                    snake[i].y + box / 2,
                    box / 2.5,
                    0,
                    Math.PI * 2
                );
                ctx.fill();
            }
        }

        ctx.fillStyle = foodColorSelector.value;
        ctx.beginPath();
        ctx.arc(food.x + box / 2, food.y + box / 2, box / 3, 0, Math.PI * 2);
        ctx.fill();

        let snakeX = snake[0].x;
        let snakeY = snake[0].y;

        if (direction === "LEFT") snakeX -= box;
        if (direction === "UP") snakeY -= box;
        if (direction === "RIGHT") snakeX += box;
        if (direction === "DOWN") snakeY += box;

        if (snakeX === food.x && snakeY === food.y) {
            score++;
            food = {
                x: Math.floor(Math.random() * (canvas.width / box)) * box,
                y: Math.floor(Math.random() * (canvas.height / box)) * box,
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
            if (score > highScore) {
                highScore = score;
                localStorage.setItem("highScore", highScore);
            }
            alert(`Game Over! Puntuación: ${score} | Récord: ${highScore}`);
            location.reload();
        }

        snake.unshift(newHead);

        ctx.fillStyle = "#fff";
        ctx.font = "20px Arial";
        ctx.fillText(`Puntuación: ${score}`, 10, canvas.height - 30);
        ctx.fillText(`Récord: ${highScore}`, 10, canvas.height - 10);
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
