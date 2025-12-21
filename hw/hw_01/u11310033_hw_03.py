from js import document, window
import random

canvas = document.getElementById("game")
ctx = canvas.getContext("2d")

# 遊戲參數
gravity = 0.6
jump_power = -12
dino_y = 130
dino_v = 0
is_jumping = False

cactus_x = 600
score = 0
game_over = False

def draw():
    ctx.clearRect(0, 0, 600, 200)

    # 地面
    ctx.fillRect(0, 160, 600, 5)

    # 恐龍
    ctx.fillRect(50, dino_y, 30, 30)

    # 仙人掌
    ctx.fillRect(cactus_x, 140, 20, 20)

    # 分數
    ctx.fillText(f"Score: {score}", 10, 20)

def update():
    global dino_y, dino_v, is_jumping
    global cactus_x, score, game_over

    if game_over:
        ctx.fillText("GAME OVER", 250, 100)
        return

    # 恐龍跳躍
    dino_v += gravity
    dino_y += dino_v

    if dino_y >= 130:
        dino_y = 130
        dino_v = 0
        is_jumping = False

    # 仙人掌移動
    cactus_x -= 5
    if cactus_x < 0:
        cactus_x = random.randint(600, 800)
        score += 1

    # 碰撞判斷
    if 50 < cactus_x < 80 and dino_y > 110:
        game_over = True

    draw()
    window.requestAnimationFrame(lambda _: update())

def jump(event):
    global dino_v, is_jumping
    if event.code == "Space" and not is_jumping:
        dino_v = jump_power
        is_jumping = True

document.addEventListener("keydown", jump)
draw()
update()
