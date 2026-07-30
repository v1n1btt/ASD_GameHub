# -*- coding: utf-8 -*-
"""
Banco de cenários do minigame de Leitura Social.

Cada cenário representa uma situação social simples do dia a dia escolar.
Cada escolha tem:
    "nivel"-> "ideal" (atitude mais adequada) ou "ok" (também válida, mas existe uma melhor)
    "feedback"-> texto curto, gentil, sem punição, explicando o porquê
    "reacao"-> emoção do COLEGA envolvido na cena, mostrada como uma carinha (ex: "feliz", "triste", "assustado", "bravo", "neutro", "pensativo"). É assim que o jogador treina a leitura social: vendo o efeito real (mas sem drama) da sua escolha na expressão de quem está por perto.
    "reacao_texto"-> legenda curta sob a carinha do colega.

Não existe "errado"/punição agressiva: toda escolha recebe uma
explicação clara do porquê, e a reação do colega é sempre mostrada de
forma gentil (mesmo quando é uma reação menos positiva).
"""

CENARIOS=[
    {
        "id":1,
        "situacao":"A professora está explicando a matéria e surge uma dúvida na sua cabeça.\nO que você faz?",
        "escolhas":[
            {
                "texto":"Levanto a mão e espero ser chamado(a)",
                "nivel":"ideal",
                "feedback":"Muito bem! Levantar a mão mostra respeito pela turma e você ainda tira sua dúvida.",
                "reacao":"feliz",
                "reacao_texto":"A turma continua tranquila.",
            },
            {
                "texto":"Grito a pergunta bem alto",
                "nivel":"ok",
                "feedback":"Sua dúvida é muito importante! Mas gritar pode assustar quem está perto. Na próxima, tente levantar a mão.",
                "reacao":"assustado",
                "reacao_texto":"Seu colega se assustou com o grito.",
            },
            {
                "texto":"Fico quieto(a) e não pergunto",
                "nivel":"ok",
                "feedback": "Tudo bem ter dúvidas! Você pode perguntar depois, em particular, ou levantar a mão na próxima oportunidade.",
                "reacao":"pensativo",
                "reacao_texto":"Seu colega nem percebeu sua dúvida.",
            },
        ],
    },
    {
        "id":2,
        "situacao":"Um colega deixou os lápis caírem no chão perto de você.\nO que você faz?",
        "escolhas":[
            {
                "texto":"Ajudo a pegar os lápis",
                "nivel":"ideal",
                "feedback":"Que gentileza! Ajudar um colega fortalece a amizade e deixa todo mundo mais feliz.",
                "reacao":"feliz",
                "reacao_texto":"Seu colega ficou feliz com a ajuda!",
            },
            {
                "texto":"Continuo fazendo minha atividade",
                "nivel":"ok",
                "feedback":"Tudo bem se você está concentrado(a)! Mas um pequeno gesto de ajuda também é muito bem-vindo.",
                "reacao":"triste",
                "reacao_texto":"Seu colega ficou um pouco triste, sozinho(a) recolhendo tudo.",
            },
            {
                "texto":"Aviso a professora sobre o ocorrido",
                "nivel":"ok",
                "feedback":"Avisar pode ajudar, mas nesse caso seu colega só precisa de uma mãozinha rápida, sem grande alarde.",
                "reacao":"neutro",
                "reacao_texto":"Seu colega ficou sem graça com a situação.",
            },
        ],
    },
    {
        "id":3,
        "situacao":"O sinal do recreio tocou, mas um colega ainda está guardando o material.\nO que você faz?",
        "escolhas":[
            {
                "texto":"Espero alguns segundos por ele(a)",
                "nivel":"ideal",
                "feedback":"Perfeito! Esperar mostra paciência e cuidado com o colega.",
                "reacao":"feliz",
                "reacao_texto":"Seu colega ficou feliz por não ficar para trás.",
            },
            {
                "texto":"Saio correndo para o recreio",
                "nivel":"ok",
                "feedback":"É natural estar animado(a) para o recreio! Mas esperar um instante pelo colega é um gesto gentil.",
                "reacao":"triste",
                "reacao_texto":"Seu colega ficou triste por ser deixado(a) para trás.",
            },
            {
                "texto":"Pergunto se ele(a) precisa de ajuda",
                "nivel":"ideal",
                "feedback":"Ótima atitude! Perguntar mostra que você se importa com o colega.",
                "reacao":"feliz",
                "reacao_texto":"Seu colega ficou contente com a pergunta!",
            },
        ],
    },
    {
        "id":4,
        "situacao": "No recreio, você percebe um colega sentado(a) sozinho(a).\nO que você faz?",
        "escolhas": [
            {
                "texto":"Vou até ele(a) e convido para brincar",
                "nivel":"ideal",
                "feedback":"Excelente! Convidar alguém para brincar pode alegrar o dia dessa pessoa.",
                "reacao":"feliz",
                "reacao_texto":"Seu colega ficou muito feliz com o convite!",
            },
            {
                "texto": "Fico brincando com meus amigos como sempre",
                "nivel": "ok",
                "feedback": "Tudo bem curtir seus amigos! Só não esqueça: um convite gentil de vez em quando faz diferença.",
                "reacao": "triste",
                "reacao_texto": "Seu colega continuou se sentindo sozinho(a).",
            },
            {
                "texto":"Aceno e sorrio de longe",
                "nivel": "ok",
                "feedback":"Que gesto gentil! Um sorriso já ajuda. Se quiser, da próxima vez pode chegar mais perto e conversar.",
                "reacao":"pensativo",
                "reacao_texto":"Seu colega sorriu de volta, mas ficou pensando se você viria.",
            },
        ],
    },
    {
        "id":5,
        "situacao":"A turma está em fila para sair da sala e você quer sair logo.\nO que você faz?",
        "escolhas": [
            {
                "texto": "Espero minha vez na fila",
                "nivel": "ideal",
                "feedback": "Isso mesmo! Esperar a vez é justo com todos os colegas",
                "reacao": "feliz",
                "reacao_texto": "A fila ficou tranquila para todo mundo",
            },
            {
                "texto": "Passo na frente dos outros",
                "nivel": "ok",
                "feedback": "Entendo a vontade de sair logo! Mas esperar a vez deixa a fila mais tranquila para todo mundo",
                "reacao": "bravo",
                "reacao_texto": "Seu colega ficou incomodado(a) por perder o lugar na fila",
            },
            {
                "texto": "Pergunto se posso trocar de lugar na fila",
                "nivel": "ok",
                "feedback": "Perguntar é um bom caminho! Só lembre que esperar também é uma ótima opção",
                "reacao": "pensativo",
                "reacao_texto": "Seu colega pensou um pouco, mas topou trocar",
            },
        ],
    },
    {
        "id":6,
        "situacao":"Você terminou sua atividade antes dos colegas e está entediado(a).\nO que você faz?",
        "escolhas":[
            {
                "texto":"Espero em silêncio, fazendo um desenho",
                "nivel":"ideal",
                "feedback":"Boa! Esperar quietinho(a) ajuda os colegas que ainda estão concentrados a terminar",
                "reacao":"feliz",
                "reacao_texto":"A turma continuou concentrada",
            },
            {
                "texto":"Fico batendo o lápis na mesa",
                "nivel":"ok",
                "feedback":"Entendo que esperar é chato! Mas o barulhinho pode distrair quem ainda está terminando",
                "reacao":"neutro",
                "reacao_texto":"Um colega perto de você se distraiu um pouco",
            },
            {
                "texto":"Pergunto baixinho à professora se posso ler um livro",
                "nivel":"ideal",
                "feedback":"Ótima ideia! Pedir permissão e escolher uma atividade tranquila é uma atitude muito boa",
                "reacao":"feliz",
                "reacao_texto":"A professora sorriu e a turma seguiu tranquila",
            },
        ],
    },
    {
        "id":7,
        "situacao":"Um colega te mostra um desenho que fez e pergunta o que você achou.\nO que você faz?",
        "escolhas":[
            {
                "texto":"Elogio algo específico que gostei",
                "nivel":"ideal",
                "feedback":"Isso mesmo! Elogiar algo específico mostra que você prestou atenção de verdade",
                "reacao":"feliz",
                "reacao_texto":"Seu colega ficou radiante com o elogio!",
            },
            {
                "texto":"Digo só \"legal\" e volto pro que eu tava fazendo",
                "nivel":"ok",
                "feedback":"Tudo bem estar ocupado(a)! Mas um comentário um pouquinho mais atencioso faria seu colega se sentir mais valorizado",
                "reacao":"neutro",
                "reacao_texto":"Seu colega ficou sem saber se você gostou de verdade",
            },
            {
                "texto":"Aponto o que poderia estar diferente",
                "nivel":"ok",
                "feedback":"Dar sua opinião é válido! Mas nesse momento, começar elogiando algo bom deixa a pessoa mais à vontade",
                "reacao":"triste",
                "reacao_texto":"Seu colega ficou um pouco desanimado(a)",
            },
        ],
    },
    {
        "id":8,
        "situacao":"Durante um jogo em grupo, seu time perdeu.\nO que você faz?",
        "escolhas":[
            {
                "texto":"Parabenizo o outro time",
                "nivel":"ideal",
                "feedback":"Isso aí! Parabenizar quem venceu mostra espírito esportivo, mesmo perdendo",
                "reacao":"feliz",
                "reacao_texto":"Os colegas do outro time ficaram felizes com o gesto",
            },
            {
                "texto":"Fico bravo(a) e reclamo do resultado",
                "nivel":"ok",
                "feedback":"É normal ficar chateado(a) ao perder! Mas tentar demonstrar isso com calma ajuda todo mundo a curtir o jogo",
                "reacao":"assustado",
                "reacao_texto":"Alguns colegas ficaram sem graça com a reclamação",
            },
            {
                "texto":"Fico quieto(a) e me afasto do grupo",
                "nivel":"ok",
                "feedback":"Tudo bem precisar de um tempinho! Só não esqueça de voltar e cumprimentar o outro time depois",
                "reacao":"triste",
                "reacao_texto":"Seus colegas sentiram sua falta na comemoração",
            },
        ],
    },
    {
        "id":9,
        "situacao":"A professora pede pra turma formar duplas para um trabalho, e ninguém te chamou ainda.\nO que você faz?",
        "escolhas":[
            {
                "texto":"Vou até alguém e pergunto se quer fazer dupla comigo",
                "nivel":"ideal",
                "feedback":"Isso aí! Tomar a iniciativa é uma atitude corajosa e gentil",
                "reacao":"feliz",
                "reacao_texto":"Seu colega ficou feliz com o convite!",
            },
            {
                "texto":"Espero quieto(a) até sobrar alguém",
                "nivel":"ok",
                "feedback":"Esperar é uma opção! Mas ir atrás de alguém pode deixar o processo mais tranquilo pra você",
                "reacao":"neutro",
                "reacao_texto":"Seu colega nem percebeu que você estava sem dupla",
            },
            {
                "texto":"Levanto a mão e aviso a professora que estou sem dupla",
                "nivel":"ideal",
                "feedback":"Boa escolha! Pedir ajuda à professora quando precisar também é uma atitude válida e madura",
                "reacao":"feliz",
                "reacao_texto":"A professora te ajudou a encontrar uma dupla rapidinho",
            },
        ],
    },
    
    {
        "id":10,
        "situacao":"Você percebe que empurrou sem querer um colega no corredor.\nO que você faz?",
        "escolhas":[
            {
                "texto":"Peço desculpas na hora",
                "nivel":"ideal",
                "feedback":"Isso mesmo! Pedir desculpas logo mostra cuidado com o outro, mesmo quando foi sem querer",
                "reacao":"feliz",
                "reacao_texto":"Seu colega ficou tranquilo com o pedido de desculpas",
            },
            {
                "texto":"Continuo andando sem dizer nada",
                "nivel":"ok",
                "feedback":"Às vezes a gente nem percebe o que aconteceu! Mas um 'desculpe-me' rápido faz toda diferença",
                "reacao":"bravo",
                "reacao_texto":"Seu colega ficou incomodado(a) com a falta do pedido de desculpas",
            },
            {
                "texto":"Pergunto se ele(a) está bem e peço desculpas",
                "nivel":"ideal",
                "feedback":"Excelente! Perguntar como a pessoa está mostra ainda mais cuidado",
                "reacao":"feliz",
                "reacao_texto":"Seu colega se sentiu bem cuidado(a)",
            },
        ],
    },
    {
        "id":11,
        "situacao":"Você vê um colega chorando sozinho(a) no canto da sala.\nO que você faz?",
        "escolhas":[
            {
                "texto":"Vou até ele(a) e pergunto se está tudo bem",
                "nivel":"ideal",
                "feedback":"Muito bem! Perguntar com carinho mostra que você se importa com o bem-estar do colega",
                "reacao":"triste",
                "reacao_texto":"Seu colega ainda está triste, mas ficou grato(a) pela atenção",
            },
            {
                "texto":"Finjo que não vi e continuo minha atividade",
                "nivel":"ok",
                "feedback":"Às vezes não sabemos o que fazer e isso é normal! Mas se aproximar com cuidado costuma ajudar bastante",
                "reacao":"triste",
                "reacao_texto":"Seu colega se sentiu mais sozinho(a)",
            },
            {
                "texto":"Chamo a professora para ajudar",
                "nivel":"ideal",
                "feedback":"Ótima atitude! Pedir ajuda de um adulto quando um colega está sofrendo é muito responsável",
                "reacao":"triste",
                "reacao_texto":"Seu colega recebeu o cuidado que precisava",
            },
        ],
    },
    {
        "id":12,
        "situacao":"Você quebrou sem querer o lápis de cor favorito de um colega.\nO que você faz?",
        "escolhas":[
            {
                "texto":"Conto a verdade e ofereço um lápis meu",
                "nivel":"ideal",
                "feedback":"Isso mesmo! Ser honesto(a) e tentar resolver o problema mostra responsabilidade",
                "reacao":"neutro",
                "reacao_texto":"Seu colega ficou triste com o lápis, mas valorizou sua honestidade",
            },
            {
                "texto":"Escondo o lápis quebrado",
                "nivel":"ok",
                "feedback":"É normal ter medo da reação do outro! Mas contar a verdade costuma ser melhor pra confiança entre vocês",
                "reacao":"bravo",
                "reacao_texto":"Seu colega descobriu depois e ficou chateado(a)",
            },
            {
                "texto":"Peço desculpas, mas não ofereço nada em troca",
                "nivel":"ok",
                "feedback":"Pedir desculpas já é um ótimo passo! Oferecer ajudar a resolver também mostra ainda mais cuidado",
                "reacao":"neutro",
                "reacao_texto":"Seu colega aceitou as desculpas, mas ainda ficou sem o lápis",
            },
        ],
    },
    {
        "id":13,
        "situacao":"Dois colegas estão discutindo sobre quem começou uma brincadeira primeiro.\nO que você faz?",
        "escolhas":[
            {
                "texto":"Sugiro que cada um conte sua versão com calma",
                "nivel":"ideal",
                "feedback":"Muito bem! Ajudar a conversa a ficar calma é uma ótima forma de resolver conflitos",
                "reacao":"pensativo",
                "reacao_texto":"Os colegas pararam pra pensar e se acalmaram",
            },
            {
                "texto":"Tomo partido de um dos dois sem ouvir o outro",
                "nivel":"ok",
                "feedback":"Ter uma opinião é normal! Mas ouvir os dois lados antes ajuda a ser mais justo(a)",
                "reacao":"bravo",
                "reacao_texto":"Um dos colegas ficou incomodado(a) por não ser ouvido(a)",
            },
            {
                "texto":"Chamo a professora para ajudar a resolver",
                "nivel":"ideal",
                "feedback":"Boa ideia! Pedir ajuda de um adulto em discussões mais complicadas é uma atitude sensata",
                "reacao":"neutro",
                "reacao_texto":"Os colegas aceitaram a ajuda da professora",
            },
        ],
    },
    {
        "id":14,
        "situacao":"Você ganhou um doce e tem só um para dividir, mas dois colegas estão por perto.\nO que você faz?",
        "escolhas":[
            {
                "texto":"Pergunto se os dois topariam dividir em partes iguais",
                "nivel":"ideal",
                "feedback":"Boa! Dividir igualmente é uma forma justa e gentil de compartilhar",
                "reacao":"feliz",
                "reacao_texto":"Os dois colegas ficaram felizes com a divisão justa",
            },
            {
                "texto":"Dou o doce só para o colega que é meu amigo mais próximo",
                "nivel":"ok",
                "feedback":"É natural querer agradar quem é mais próximo! Mas incluir todo mundo evita que alguém se sinta deixado de lado",
                "reacao":"triste",
                "reacao_texto":"O outro colega ficou um pouco triste por ficar de fora",
            },
            {
                "texto":"Guardo o doce para comer sozinho(a) depois",
                "nivel":"ok",
                "feedback":"Tudo bem guardar algo seu! Mas compartilhar de vez em quando é um gesto bonito com os colegas",
                "reacao":"neutro",
                "reacao_texto":"Os colegas nem perceberam, mas ficaram sem experimentar",
            },
        ],
    },
    {
        "id":15,
        "situacao":"Você percebe que um colega está sendo excluído de uma brincadeira em grupo.\nO que você faz?",
        "escolhas":[
            {
                "texto":"Convido o colega excluído para brincar com o grupo",
                "nivel":"ideal",
                "feedback":"Muito bem! Incluir quem está sendo deixado de lado é um gesto de muita generosidade",
                "reacao":"feliz",
                "reacao_texto":"O colega ficou muito feliz por ser incluído!",
            },
            {
                "texto":"Fico brincando e não digo nada",
                "nivel":"ok",
                "feedback":"Às vezes não sabemos como agir nessas horas! Mas um convite simples já pode mudar o dia de alguém",
                "reacao":"triste",
                "reacao_texto":"O colega continuou se sentindo excluído",
            },
            {
                "texto":"Aviso a professora sobre o que está acontecendo",
                "nivel":"ideal",
                "feedback":"Ótima atitude! Contar para um adulto quando alguém está sendo excluído ajuda a resolver a situação",
                "reacao":"neutro",
                "reacao_texto":"A professora conversou com o grupo com calma",
            },
        ],
    }
]

#personagens que o user pode escolher
PERSONAGENS=[{"id":"maya","nome":"Maya","imagem":"assets/personagens/maya.png"},
    {"id":"teodoro","nome":"Teodoro","imagem":"assets/personagens/teodoro.png"},
    {"id":"bruno","nome":"Bruno","imagem":"assets/personagens/bruno.png"},
    {"id":"bia","nome":"Bia","imagem":"assets/personagens/bia.png"},
    {"id":"sofia","nome":"Sofia","imagem":"assets/personagens/sofia.png"},
    {"id":"gui","nome":"Gui","imagem":"assets/personagens/gui.png"}]

#reação à escolha do player
REACOES_IMG={"feliz":"assets/reacoes/feliz.png",
    "triste":"assets/reacoes/triste.png",
    "assustado":"assets/reacoes/assustado.png",
    "bravo": "assets/reacoes/bravo.png",
    "neutro":"assets/reacoes/neutro.png",
    "pensativo":"assets/reacoes/pensativo.png"}