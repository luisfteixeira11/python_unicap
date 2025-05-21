import random
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 18
GPIO_ECHO = 24
GPIO.setup(GPIO_TRIGGER, GPIO.OUT) ##seta o sensor
GPIO.setup(GPIO_ECHO, GPIO.IN)

top_tempos = [0, 0, 0, 0, 0]
top_nomes = ["", "", "", "", ""] ##para o sistema de pontuação
lugar = -1

verde = False
amarelo = False
vermelho = False
errado = False
fimdoprograma = False
atualizado = False
 
GPIO.setup(17, GPIO.OUT)  # vermelho
GPIO.setup(22, GPIO.OUT)  # verde
GPIO.setup(27, GPIO.OUT)  # amarelo

def iniciar():
    global fimdoprograma
    x = input("Escreva 'vamos' abaixo pra iniciar quando tu tiver pronto, se quiser terminar digite 'xao' :)\n")
 
    while x.lower() != 'vamos' and x.lower() != 'xao':
        x = input("Deixe de resenha vá\n")
    if x.lower() == 'xao':
        fimdoprograma = True
 
def luzes_acendem(): ##todas as luzes vao acendendo como um sinal de transito no intervalo de 1s e depois apagam
    GPIO.output(17, GPIO.HIGH)  # vermelho
    time.sleep(1)
    GPIO.output(27, GPIO.HIGH)  # amarelo
    time.sleep(1)
    GPIO.output(22, GPIO.HIGH)  # verde
    time.sleep(1)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
 
def medir_distancia(): ##calcula a distância medida pelo sensor ultrassonico
    GPIO.output(GPIO_TRIGGER, False)
    time.sleep(0.05)
 
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    while GPIO.input(GPIO_ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        pulse_end = time.time()
 
    pulse_duration = pulse_end - pulse_start
    distancia = pulse_duration * 17150
    return round(distancia, 2)
 
def cronometro_de_espera(tempolim): ##da um tempo de espera para concentração
    agora = time.time()
    while True:
        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - agora
        if medir_distancia() < 60:
            print("KKKKKKKK queimou a largadapae")
            return False
        elif tempolim <= tempo_decorrido:
            largada(random.randint(1,8))
            return True
        time.sleep(0.01)
 
def largada(x): ##acende uma luz, assim, dando o necessário para o jogador acionar o sensor na distância pedida
    global verde, amarelo, vermelho
    verde = False
    amarelo = False 
    vermelho = False
 
    if x == 1:
        GPIO.output(22, GPIO.HIGH)  # verde
        verde = True
    elif x == 2:
        GPIO.output(17, GPIO.HIGH)  # vermelho
        vermelho = True
    else:
        GPIO.output(27, GPIO.HIGH)  # amarelo
        amarelo = True
 
def cronometro_reacaovdd(): ##funcionamento do jogo de reacao
    global errado, lugar
    errado = False
    agora = time.time()

    while True:
        dist = medir_distancia()
        tempo_decorrido = time.time() - agora
        if dist <= 60:
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            if dist <= 20 and not verde:
                print("Tuderrado")
                return True, -1  
            elif dist <= 40 and not amarelo:
                print("Tuderrado")
                return True, -1
            elif dist <= 60 and not vermelho:
                print("Tuderrado")
                return True, -1
            tempo_e_dist(tempo_decorrido, dist)
            lugar = atualizar_top5(tempo_decorrido)
            return False, lugar
        if tempo_decorrido > 10:
            print("esquecesse foi?kkkkkkkkkkkkkkkkkkkkk")
            return True, -1
        time.sleep(0.01)
 
def tempo_e_dist(tempo_decorrido, dist): ##printa no terminal o tempo e a distancia
    print(f"Tempo de Reação: {tempo_decorrido:.2f} segundos")
    print(f"Distância: {dist:.2f} cm")
    
def atualizar_top5(tempo):
    global top_tempos, top_nomes, atualizado

    # Se for pior que todos, não entra no ranking
    if tempo > top_tempos[4] and top_tempos[4] != 0:
        return -1

    pos = 4
    while pos > 0 and (top_tempos[pos - 1] == 0 or tempo < top_tempos[pos - 1]):
        top_tempos[pos] = top_tempos[pos - 1]
        top_nomes[pos] = top_nomes[pos - 1]
        pos -= 1

    top_tempos[pos] = tempo
    top_nomes[pos] = ""  # será preenchido depois
    atualizado = True
    return pos
 
while not fimdoprograma:
    iniciar()
    if fimdoprograma:
        break
    luzes_acendem()
    while True:
        if cronometro_de_espera(random.randint(2, 10)):
            errado, lugar = cronometro_reacaovdd()
        if atualizado and lugar != -1:
            nomao = input("Bota teu nome que tu ganhou: ").strip()
            if not nomao:
                nomao = "nao botou nada pq quis"
            top_nomes[lugar] = nomao
        print("\nRanking Top 5 Tempos de Reação:")
        for i in range(5):
            if top_tempos[i] != 0:
                print(f"{i+1}º: {top_nomes[i]} - {top_tempos[i]:.2f} segundos")
        atualizado = False