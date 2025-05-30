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
contavitórias = 0
 
verde = False
amarelo = False
vermelho = False
fimdoprograma = False
atualizado = False
errado = False
 
GPIO.setup(17, GPIO.OUT)  # vermelho
GPIO.setup(22, GPIO.OUT)  # verde
GPIO.setup(27, GPIO.OUT)  # amarelo
 
def iniciar():
    global fimdoprograma
    x = input("Escreva 'vamos' abaixo pra iniciar quando tu tiver pronto, se quiser terminar digite 'xao' :)\n")
 
    while x.lower() != 'vamos' and x.lower() != 'xao':
        x = input("Deixe de resenha vá\n")
        print("")
    if x.lower() == 'xao':
        fimdoprograma = True
 
def luzes_acendem(): ##todas as luzes vao acendendo como um sinal de transito no intervalo de 0.5s e depois apagam
    GPIO.output(17, GPIO.HIGH)  # vermelho
    time.sleep(0.5)
    GPIO.output(27, GPIO.HIGH)  # amarelo
    time.sleep(0.5)
    GPIO.output(22, GPIO.HIGH)  # verde
    time.sleep(0.5)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    
def luzes_comemoram():
    for _ in range(5):  # piscam 5 vezes se entrar no ranking
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        time.sleep(0.2)
        
def luzes_tristes():
    # pisca o vermelho 3 vezes para tristeza
    for _ in range(3):
        GPIO.output(17, GPIO.HIGH) 
        time.sleep(0.3)
        GPIO.output(17, GPIO.LOW)
        time.sleep(0.3)
        
def luzes_recorde():
    for _ in range(7):
        GPIO.output(22, GPIO.HIGH)  ##verde varias vezes
        time.sleep(0.15)
        GPIO.output(22, GPIO.LOW)
        time.sleep(0.15)
        
def luzes_aplaudem():
    for _ in range(7):
        GPIO.output(17, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(27, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(22, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(22, GPIO.LOW)
 
def medir_distancia(): ##calcula a distância medida pelo sensor ultrassonico
    GPIO.output(GPIO_TRIGGER, False)
    time.sleep(0.000002)
 
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    while GPIO.input(GPIO_ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        pulse_end = time.time()
 
    pulse_duration = pulse_end - pulse_start
    distancia = pulse_duration * 17150 ##agora tá em milissegundos
    return round(distancia, 2)
 
def cronometro_de_espera(tempolim): ##da um tempo de espera para concentração
    global errado
    agora = time.time()
    while True:
        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - agora
        if medir_distancia() <= 60:
            luzes_tristes()
            print("KKKKKKKK queimou a largadapae")
            print("")
            errado = True
            return False
        elif tempolim <= tempo_decorrido:
            largada(random.randint(1,3))
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
 
def cronometro_reacao():
    global lugar, contavitórias, errado
    agora = time.time()

    while True:
        dist = medir_distancia()
        tempo_decorrido = time.time() - agora
        if dist <= 60:
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            # acertou a cor e a distância
            if verde and dist <= 20:
                tempo_e_dist(tempo_decorrido, dist)
                lugar = atualizar_top5(tempo_decorrido)
                contavitórias+=1
                return lugar
            elif amarelo and 20 < dist <= 40:
                tempo_e_dist(tempo_decorrido, dist)
                lugar = atualizar_top5(tempo_decorrido)
                contavitórias+=1
                return lugar
            elif vermelho and 40 < dist <= 60:
                tempo_e_dist(tempo_decorrido, dist)
                lugar = atualizar_top5(tempo_decorrido)
                contavitórias+=1
                return lugar
            # errou a cor ou a distância
            else:
                print("Tuderrado")
                print("")
                luzes_tristes()
                time.sleep(1)
                tempo_e_dist(tempo_decorrido, dist)
                errado = True
                return -1
        if tempo_decorrido > 10:
            print("esquecesse foi?kkkkkkkkkkkkkkkkkkkkk")
            print("")
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            return -1
        time.sleep(0.01)
 
def tempo_e_dist(tempo_decorrido, dist): ##printa no terminal o tempo e a distancia
    global verde, amarelo, vermelho
    tempo = tempo_decorrido*1000
    print(f"Tempo de Reação: {tempo:.2f} milissegundos")
    print("")
    print(f"Verde: {verde}, Amarelo: {amarelo}, Vermelho: {vermelho}, Distância: {dist}")
    print("")
    print(f"Distância: {dist:.2f} cm")
    print("")
   
def atualizar_top5(tempo):
    global top_tempos, top_nomes, atualizado
 
    # se for o pior, não entra no ranking
    if tempo > top_tempos[4] and top_tempos[4] != 0:
        return -1
 
    pos = 4
    while pos > 0 and (top_tempos[pos - 1] == 0 or tempo < top_tempos[pos - 1]):
        top_tempos[pos] = top_tempos[pos - 1]
        top_nomes[pos] = top_nomes[pos - 1]
        pos -= 1
 
    top_tempos[pos] = tempo
    top_nomes[pos] = ""  # preenchido depois
    atualizado = True
    return pos
 
while not fimdoprograma:
    iniciar()
    if fimdoprograma:
        print("Jogo encerrado.")
        break
    while True:
        errado = False
        luzes_acendem()
        if cronometro_de_espera(random.randint(2, 15)):
            lugar = cronometro_reacao()
            time.sleep(2)
        else:
            tempo_e_dist(0, medir_distancia())
            time.sleep(2)
        if atualizado and lugar != -1:
            nomao = input("Bota teu nome que tu ganhou: ").strip()
            luzes_comemoram()
            if not nomao:
                nomao = "nao botou nada pq quis"
            print("")
            if lugar == 0:
                luzes_recorde()
            top_nomes[lugar] = nomao
            print("\nRanking Top 5 Tempos de Reação:")
            for i in range(5):
                if top_tempos[i] != 0:
                    print(f"{i+1}º: {top_nomes[i]} - {top_tempos[i]:.2f} segundos")
                print("")
            atualizado = False
        if contavitórias >= 3:
            luzes_aplaudem()
            print("Você atingiu 3 ou mais vitórias")
        if errado:
            fimdoprograma = True
            break
        vermelho = False
        amarelo = False
        verde = False
    if fimdoprograma:
        print("Jogo encerrado.")
        print("\nRanking Top 5 Tempos de Reação:")
        for i in range(5):
            if top_tempos[i] != 0:
                print(f"{i+1}º: {top_nomes[i]} - {top_tempos[i]:.2f} segundos")
            print("")
        try:
            jogardnv = int(input("Digite '1' para jogar novamente...\n"))
        except ValueError:
            jogardnv = 0
        if jogardnv == 1:
            fimdoprograma = False
            continue
        break