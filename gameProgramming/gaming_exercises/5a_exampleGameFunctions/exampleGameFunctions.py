# Example Game Functions Project, Corey Battle, v0.0
import random

def functionOne():
    pass

def functionTwo(param1): 
    pass

def functionThree(param1 = "Default Value"):
    pass

def functionFour(param1, param2, param3):
    pass

# Global Variable
width = 700
height = 550
clock = 60

def getPoleY(baseY):
    return random.randint(100, baseY - 200)


def main():
    gameOn = True
    baseX = 0
    baseY = height - 60
    ballX = 120
    ballY = baseY - 60
    gravity = 10
    bouncing = 25
    poleX = 400
    poleY = getPoleY(baseY)
    speed = 0
    gameOver = False
    basketY = random_Basket(poleY, baseY)
    basket_Score = 0
    score = 0

    # Bouncing
    ballY -= bouncing
    bouncing -= 1
    ballY += gravity
    if(ballY > baseY - 20):
        bouncing = 25
    
    clock.tick(60)


            