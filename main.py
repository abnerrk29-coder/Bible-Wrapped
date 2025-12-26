import csv
from collections import Counter

arquivo = "leituras.csv"

dias = 0
tempo_total = 0
sentimentos = []
verdades = []
musicas = []
marcou = 0

with open(arquivo, encoding="utf-8") as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        dias += 1
        tempo_total += int(linha["tempo_min"])
        sentimentos.append(linha["sentimento_regente"])
        verdades.append(linha["verdade_aprendida"])
        musicas.append(linha["musica_escutada"])
        if linha["marcou_muito"].lower() == "sim":
            marcou += 1

sentimento_top = Counter(sentimentos).most_common(1)[0][0]
verdade_top = Counter(verdades).most_common(1)[0][0]
musica_top = Counter(musicas).most_common(1)[0][0]

horas = tempo_total // 60
minutos = tempo_total % 60

texto = f"""
📘 Bible Wrapped — Retrospectiva

📅 Dias de leitura: {dias}
⏱️ Tempo total: {horas}h {minutos}min

💛 Sentimento regente: {sentimento_top}
🔥 Leituras que marcaram muito: {marcou}

📖 Verdade mais recorrente:
"{verdade_top}"

🎵 Música mais presente:
{musica_top}
"""

with open("retrospectiva.txt", "w", encoding="utf-8") as f:
    f.write(texto)

print(texto)
