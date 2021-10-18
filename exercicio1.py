import random as r

class Ambiente():
    def __init__(self, salas):
        self.salas = salas

    def sujar(self):
        for i in range(len(self.salas)):
            if r.randint(1, 10) > 6:
                self.salas[i] = 1

    # recebe a posição do agente e verifica se está suja ou limpa
    def status_sala(self, posicao_atual: int):
        if self.salas[posicao_atual] == 1:
            return True
        else:
            return False


        #return self.salas[posicao_atual] == 1

    # Remove a sujeira da sala
    def limpar_sala(self, posicao: int):
        self.salas[posicao] = 0

    # Agente tentando se mover para fora do ambiente (Paredes)
    def colisao(self, posicao):
        return posicao >= len(self.salas) or posicao < 0

    def imprimir_ambiente(self):
        print(self.salas)

class Agente():
    def __init__(self, ambiente: Ambiente, posicao_atual: int):
        self.ambiente = ambiente
        self.posicao_atual = posicao_atual
        self.score = 0


    def varredura(self, loop: int):
        
        i = 1
        
        sentido = 1 # sentido para qual o aspirador irá se movimentar
        # 1 -> direita
        # 0 -> esquerda

        while i <= loop:

            status = ['','']
            #k = 0
            for k in range(2):
                if self.ambiente.salas[k] == 0:
                    status[k] = 'Limpo'
                else:
                    status[k] = 'Sujo'

            print('Aspirador na sala ', self.posicao_atual)
            print('Salas ', status)
            

            #Se sala está suja
            if self.ambiente.status_sala(self.posicao_atual):
                self.aspirar()
                print('limpando sala')
                self.incrementar_score()
                        

            elif sentido:
                sentido = self.movimentar_dir()
            
            else: 
                sentido = self.movimentar_esq()

            print('sujando salas aleatóriamente\n\n')
            self.ambiente.sujar()
            i += 1 
            
    def incrementar_score(self):
        self.score += 1

    def aspirar(self):
        self.ambiente.limpar_sala(self.posicao_atual)

    def movimentar_dir(self):
        if self.ambiente.colisao(self.posicao_atual + 1): # Colidiu com a parede NoOp
            print('Parede, NoOp')
            return 0 # mudar direção para a esquerda
        
        # Movimentar para a direita
        else:
            print('Sala limpa na posição do aspirador, movendo para a Direita')
            self.posicao_atual += 1 
            return 1
        
    def movimentar_esq(self):
        if self.ambiente.colisao(self.posicao_atual - 1): # Colidiu com a parede NoOp
            print('Parede, NoOp')
            return 1 # mudar direção para a direita

        # Movimentar para a Esquerda
        else:
            self.posicao_atual -= 1
            print('Sala limpa na posição do aspirador, movendo para a Esquerda')
            return 0


class main():

    i = 0
    j = 0
    total = 0
    aux = 1
    loop = 1000

    while i < 2:
        j = 0
        
        while j < 4:
            sala = []
            for i in range(2): 
                sala = []
                vet = []
                
                vet.append(r.randint(0, 1))
                vet.append(r.randint(0, 1))
                sala = [vet]
            
            ambiente = Ambiente(sala[0])
            posicao_inicial = r.randint(0,1)
            aspirador = Agente(ambiente, posicao_inicial)

            print('### Verificacao ', aux, '###\n')
            
            aspirador.varredura(loop)
            total += aspirador.score

            print('Score ', aspirador.score)
            print ('***********************************************************\n\n')

            j += 1 
            aux += 1
    
        i += 1

    print('Score Final = ', total, " \n\n\n") 


    


    