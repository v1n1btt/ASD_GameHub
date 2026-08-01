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
        "id": "par_alegre",
        "lado_a": "assets/memoria/alegre.jpg",
        "lado_b": "assets/memoria/alegre_t.jpg",
        "nome": "Alegre"
    },
    {
        "id": "par_bravo",
        "lado_a": "assets/memoria/bravo.jpg",
        "lado_b": "assets/memoria/bravo_t.jpg",
        "nome": "Bravo"
    },
    {
        "id": "par_cansado",
        "lado_a": "assets/memoria/cansado.jpg",
        "lado_b": "assets/memoria/cansado_t.jpg",
        "nome": "Cansado"
    },
    {
        "id": "par_confuso",
        "lado_a": "assets/memoria/confuso.jpg",
        "lado_b": "assets/memoria/confuso_t.jpg",
        "nome": "Confuso"
    },
    {
        "id": "par_feliz",
        "lado_a": "assets/memoria/feliz.jpg",
        "lado_b": "assets/memoria/feliz_t.jpg",
        "nome": "Feliz"
    },
    {
        "id": "par_pensativo",
        "lado_a": "assets/memoria/pensativo.jpg",
        "lado_b": "assets/memoria/pensativo_t.jpg",
        "nome": "Pensativo"
    },
    {
        "id": "par_surpreso",
        "lado_a": "assets/memoria/surpreso.jpg",
        "lado_b": "assets/memoria/surpreso_t.jpg",
        "nome": "Surpreso"
    },
    {
        "id": "par_triste",
        "lado_a": "assets/memoria/triste.jpg",
        "lado_b": "assets/memoria/triste_t.jpg",
        "nome": "Triste"
    }
]
