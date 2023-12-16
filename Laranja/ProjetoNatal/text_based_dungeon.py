import random
import time

lista_de_monstros = ["Grinch", "Krampus", "Renas", "Duendes", "Boneco de Neve"]

personagem = {"vida": 100, "presentes": 0}


def gerador_de_salas():
  amigavel = random.randint(0, 1)
  lista_de_monstros_len = len(lista_de_monstros)
  tipo_de_monstro = random.randint(0, (lista_de_monstros_len - 1))

  print(f"\nUm/a {lista_de_monstros[tipo_de_monstro]} surge do nada...")
  time.sleep(2)

  if amigavel == 1:
    numero_de_presentes = random.randint(2, 30)
    personagem["presentes"] = personagem["presentes"] + numero_de_presentes

    print(
        f"Para te dar os seus presentes!!! (+{numero_de_presentes}presentes!!)\n"
    )
    time.sleep(2)
  else:
    valor_de_ataque = random.randint(10, 60)
    personagem["vida"] = personagem["vida"] - valor_de_ataque

    if personagem["vida"] < 0:
      personagem["vida"] = 0

    print(
        f"Para te atacar!!!({personagem['vida']} pontos de vida restantes!!)\n"
    )
    time.sleep(2)

def intro():
  print("O teu doce sono das manhãs de sábado é interrompido por um estrondo\n"
        "vindo da cozinha. Este som persiste, ecoando pelas escadas que\n"
        "levam ao teu quarto, e sem pensar duas vezes, saltas da cama para\n"
        "encontrar uma solução...\n")
  time.sleep(10)
  print(
      "Ao descer as escadas, os raios de sol escapam por entre as apertadas\n"
      "brechas das cortinas e acordam os teu olhos cansados. No canto da\n"
      "sala é agora visivel o calendario que marca o dia da véspera de natal.\n"
      "Alguém já deve ter acordado para marcar o novo dia, no entanto,\n"
      "enquanto te preparavas para dar um sermão a quem quer que ousou\n"
      "perturbar o teu sono, reparas num velho perto da\n"
      "lareira...\n")
  time.sleep(10)
  print(
      "A criatura usava um chapéu pontiagudo, um belo fato vermelho, e\n"
      "trazia um saco vazio às costas. Os vossos olhares cruzam, e encontra\n"
      "uma cara de desespero expressa no velho.\n")
  time.sleep(5)
  print("- Preciso da tua ajuda! - diz o velho enquanto que aponta para a tua\n"
        "dispensa.\n")
  time.sleep(3)
  print(
      "- O natal já não é como era antes, preciso que salves o natal!\n"
      "O Grinch e o Krampus está a dominar a minha fábrica e preciso que vás\n"
      "lá para conseguires derrotá-los \n"
      "e voltarmos a fazer as pessoas felizes!\n"
  )
  time.sleep(10)
  print("Caso fiques sem vidas sou obrigada a trazer-te de volta sem nada,\n"
        "se quiseres voltar diz \"hohoho\"\n"
        )



def game():
  intro();
  personagem_não_morreu = 1
  continuar_loop = 1
  # game loop
  while continuar_loop == 1:
    # generates a room with a creature
    gerador_de_salas()

    # ends loop if the character's life is == 0
    if personagem["vida"] == 0:
      print(f"Foste apanhado com {personagem['presentes']} presentes que a\n"
            "pequena criatura não conseguiu resgatar :(\n")
      personagem_não_morreu = 0
      continuar_loop = 0

    input_valido = 0
    # handles input errors
    while input_valido == 0 and personagem_não_morreu == 1:
      try:
        # ends loop if the player chooses to
        continuar_loop = int(input("Queres continuar? (1 to continue)\n"))
        input_valido = 1
      except:
        print("Input inválido, tem de ser um número!\n")
        input_valido = 0

  if personagem_não_morreu == 1:
    if personagem["presentes"] >= 50:
      print(f" -Ganhaste {personagem['presenstes']} presentes :D !!!\n")
    elif personagem["presentes"] == 0:
      print("- Oh, nem tentaste, ganhaste 0 presentes :(")
    else:
      print("Melhor sorte para a próxima, conseguiste trazer apenas\n"
            f"{personagem['presentes']} presentes!\n")


game()
