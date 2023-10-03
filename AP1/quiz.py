answer = 0
print("O que este segmento de código mostra? \n c <- 17 \n x <- 4 \n x <- 14 MOD 2 \n c <- c * x \n DISPLAY c \n")
print(" A) 68 \n B) 34 \n C) 17 \n D) 0")

while answer != "D":
    answer = input("Resposta: ").capitalize()
    if answer == "D":
        print("Acertou!")
    else:
        print("Errou, tente outra")
