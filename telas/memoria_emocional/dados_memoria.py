"""
Banco de pares para o jogo da memória (associação).

Cada par é composto por duas imagens que se correspondem (ex: nome e figura,
figura e figura relacionada, etc.). Em cada rodada, 3 pares são sorteados
aleatoriamente para compor as 6 cartas.

Estrutura de cada par:
    - id: identificador único (string)
    - lado_a: caminho da imagem do primeiro elemento
    - lado_b: caminho da imagem do segundo elemento
    - nome: (opcional) nome descritivo para debug
"""

VERSO_IMGPATH = "assets/memoria/verso.jpg"
PARES = [
    {
        "id": "par01",
        "lado_a": "assets/memoria/par01a.jpg",
        "lado_b": "assets/memoria/par01b.png",
        "nome": "Exemplo 1"
    },
    {
        "id": "par02",
        "lado_a": "assets/memoria/par02a.png",
        "lado_b": "assets/memoria/par02b.png",
        "nome": "Exemplo 2"
    },
    {
        "id": "par03",
        "lado_a": "assets/memoria/par03a.png",
        "lado_b": "assets/memoria/par03b.png",
        "nome": "Exemplo 3"
    },
    {
        "id": "par04",
        "lado_a": "assets/memoria/par04a.png",
        "lado_b": "assets/memoria/par04b.png",
        "nome": "Exemplo 4"
    },
    {
        "id": "par05",
        "lado_a": "assets/memoria/par05a.png",
        "lado_b": "assets/memoria/par05b.png",
        "nome": "Exemplo 5"
    },
    {
        "id": "par06",
        "lado_a": "assets/memoria/par06a.png",
        "lado_b": "assets/memoria/par06b.png",
        "nome": "Exemplo 6"
    },
    {
        "id": "par07",
        "lado_a": "assets/memoria/par07a.png",
        "lado_b": "assets/memoria/par07b.png",
        "nome": "Exemplo 7"
    },
    {
        "id": "par08",
        "lado_a": "assets/memoria/par08a.png",
        "lado_b": "assets/memoria/par08b.png",
        "nome": "Exemplo 8"
    },
    {
        "id": "par09",
        "lado_a": "assets/memoria/par09a.png",
        "lado_b": "assets/memoria/par09b.png",
        "nome": "Exemplo 9"
    },
    {
        "id": "par10",
        "lado_a": "assets/memoria/par10a.png",
        "lado_b": "assets/memoria/par10b.png",
        "nome": "Exemplo 10"
    },
    {
        "id": "par11",
        "lado_a": "assets/memoria/par11a.png",
        "lado_b": "assets/memoria/par11b.png",
        "nome": "Exemplo 11"
    },
    {
        "id": "par12",
        "lado_a": "assets/memoria/par12a.png",
        "lado_b": "assets/memoria/par12b.png",
        "nome": "Exemplo 12"
    }
]
