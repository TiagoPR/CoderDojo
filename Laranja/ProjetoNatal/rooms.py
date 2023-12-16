import time, random
import utils

class Room:
    def __init__(self, description):
        self.description = description
        self.connections = {}
        self.visits = 0;

    def add_connection(self, direction, connected_room):
        self.connections[direction] = connected_room
    
    def get_connection(self, direction):
        return self.direction.get(direction)
    
    def increment_visit(self):
        self.visits += 1;

class EntryHall(Room):
    def __init__(self):
        super().__init__(
            """
            Passas pela porta da tua dispensa, que por magia encontras-te numa sala muito grande,
            com um espelho e uma carta.
            """
        )
    
    def start(self):
        print(self.description)
        print(
            """
            Ao vertes ao espelho deparas-te com um boneco de gengibre e 
            uma carta colada que diz:
            """
        )
        time.sleep(1);
        print(
            """
            Pressiona qualquer tecla para seguir em frente
            """)
        input();
        Room.increment_visit(self)
        # Ir para a MachineRoom();
        return

class MachineRoom(Room):
    def __init__(self):
        super().__init__(
        """
        Ao entrares na sala deparaste com um enchente de duendes a chorar.
        """)

    def start(self):
        print(self.description)
        if(self.visits == 0){
            print(
            """
            Duende - Por favor és a nossa única esperança para voltar o Natal. 
            """
        )
        input("Pressiona uma tecla para continuar a conversa")
        print(
            """
            Eu - Eu vou tentar o meu melhor!
            """
        )
        input("Pressiona uma tecla para continuar a conversa")
        print(
            """
            Dundes - BOA SORTE!
            """
        )
        }
        Room.increment_visit(self)
        # Escolhas de caminho
        utils.get_direction()
        return

class Stable(Room):
    def __init__(self):
        super().__init__(
            """
            Encontras-te numa sala cheio de palha.
            """)

    def start(self):
        print(self.description)
        prob = random.randint(0,1)

        if(prob == 0):
            print(
                """
                As renas estão ocupadas a comer palha. 
                """
            )
        else:
            print(
                """
                As renas dizem-te adoram bebidas com gás.
                """
            )
        
        # Escolhas de caminho
        utils.get_direction()
        return

class Library(Room):
    def __init__(self):
        super().__init__(
            """
            Encontras-te numa sala cheio de livros..
            """)

    def start(self):
        print(self.description)
        return
        
class StorageRoom(Room):
    def __init__(self):
        super().__init__(""" <TEXTO AQUI> """)

    def start(self):
        print(self.description)
        return

class Courier(Room):
    def __init__(self):
        super().__init__(
            """ 
            Estás num local cheio de cartas.
            """)

    def start(self):
        print(self.description)
        prob = random.randint(0,4)
        if(prob == 0):
            print("O GRINCH APARECE, ATACA-TE E TIRA 10 DE VIDA")
            # retirar vida
        print(
            """ 
            Pegas numa carta dourada e está escrito:

            O Pai Natal foi criado pela?
            (1) Coca-Cola
            (2) Ice-Tea
            """)
        
        res = input("Escolhe entre 1 e 2, 3 caso não queiras responder")
        # caso nao queira responder
        if res == "1":
            print("Abriu-se uma porta à direita")

        # movimento
        utils.get_direction()
        return
    
class Gate(Room):
    def __init__(self):
        super().__init__(""" <TEXTO AQUI> """)

    def start(self):
        print(self.description)
        return

class SantaClausOffice(Room):
    def __init__(self):
        super().__init__(""" E  SOU O KRAMPUS E DESAFIO-TE PARA UM JOGO DE SORTE PELO NATAL""")

    def start(self):
        print(self.description)
        utils.boss_fight()
        return