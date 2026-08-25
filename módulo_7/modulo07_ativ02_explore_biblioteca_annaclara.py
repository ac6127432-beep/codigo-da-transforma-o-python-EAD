# PROVA DE LÍNGUA PORTUGUESA
# Aluna: Anna Helena
# Professor: Miguel
# Data: 25/08/2026
# Horário: 14:41
# ==========================================

def aplicar_prova():
    print("=" * 40)
    print("       ESCOLA - AVALIAÇÃO DE PORTUGUÊS")
    print("=" * 40)
    print(f"Aluna: Anna Helena")
    print(f"Professor: Miguel")
    print(f"Data: 25/08/2026 | Horário: 14:41")
    print("=" * 40 + "\n")

    questoes = [
        {
            "pergunta": "1. Assinale a alternativa em que há concordância verbal incorreta:",
            "opcoes": [
                "A) Fazem dois anos que não viajo.",
                "B) Devem existir soluções para este problema.",
                "C) Houve muitos protestos durante a manifestação.",
                "D) Alguém entre nós resolverá a questão."
            ],
            "resposta_correta": "A",
            "explicacao": "O verbo 'fazer', quando indica tempo decorrido, é impessoal e deve ficar na 3ª pessoa do singular ('Faz dois anos')."
        },
        {
            "pergunta": "2. Na frase 'O livro que comprei é interessante', a palavra 'que' classifica-se morfologicamente como:",
            "opcoes": [
                "A) Conjunção integrante",
                "B) Pronome relativo",
                "C) Conjunção subordinativa causal",
                "D) Preposição"
            ],
            "resposta_correta": "B",
            "explicacao": "O 'que' retoma o termo anterior ('o livro') e pode ser substituído por 'o qual', exercendo a função de pronome relativo."
        },
        {
            "pergunta": "3. Qual das opções abaixo apresenta um exemplo de figura de linguagem chamada 'antítese'?",
            "opcoes": [
                "A) O vento sussurrava segredos na janela.",
                "B) Ele chorava rios de lágrimas.",
                "C) O sol tristonho brilhava entre as nuvens escuras.",
                "D) Tristeza e alegria moram na mesma casa."
            ],
            "resposta_correta": "D",
            "explicacao": "A antítese consiste no uso de palavras com sentidos opostos ('tristeza' e 'alegria') em uma mesma frase para dar ênfase."
        }
    ]

    pontos = 0

    for i, q in enumerate(questoes, 1):
        print(q["pergunta"])
        for op in q["opcoes"]:
            print(op)
        
        resposta_usuario = input("\nSua resposta (A, B, C ou D): ").strip().upper()
        
        if resposta_usuario == q["resposta_correta"]:
            print("✔ Resposta correta!\n")
            pontos += 1
        else:
            print(f"✘ Resposta incorreta. A alternativa correta era: {q['resposta_correta']}")
            print(f"Explicação: {q['explicacao']}\n")
        print("-" * 40)

    print(f"\nFim da prova, Anna Helena!")
    print(f"Professor Miguel agradece a dedicação.")
    print(f"Sua pontuação final: {pontos} de 3 acertos.")

if __name__: str == "__main__"
aplicar_prova()
