import pandas as pd
import matplotlib.pyplot as plt

# ==================================================
# LEITURA DA BASE DE DADOS
# ==================================================

print("\n==============================")
print("LEITURA DA BASE DE DADOS")
print("==============================\n")

df = pd.read_csv("base_recarga_veiculos_eletricos_convertido.csv")

print("Base de dados carregada com sucesso!\n")


# ==================================================
# VISUALIZAÇÃO DOS DADOS
# ==================================================

print("==============================")
print("VISUALIZAÇÃO DOS DADOS")
print("==============================\n")

print("Primeiras 5 linhas da base:\n")
print(df.head())

print("\n==============================\n")

print("Informações da base:\n")
print(df.info())

print("\n==============================\n")

print("Estatísticas gerais:\n")
print(df.describe())


# ==================================================
# GRÁFICO DE SETORES (PIZZA)
# ==================================================

print("\n==============================")
print("GRÁFICO DE SETORES")
print("==============================\n")

tipos = df["tipo_carregador"].value_counts()

print("Quantidade por tipo de carregador:\n")
print(tipos)

plt.figure(figsize=(8, 6))

plt.pie(
    tipos,
    labels=tipos.index,
    autopct='%1.1f%%',
    colors=["skyblue", "orange"]
)

plt.title("Distribuição dos Tipos de Carregadores")

plt.legend(tipos.index)

plt.show()


# ==================================================
# GRÁFICO DE BARRAS
# ==================================================

print("\n==============================")
print("GRÁFICO DE BARRAS")
print("==============================\n")

consumo_horario = df.groupby("horario")["energia_kwh"].mean()

print("Consumo médio por horário:\n")
print(consumo_horario)

plt.figure(figsize=(8, 6))

consumo_horario.plot(
    kind="bar",
    color="green"
)

plt.title("Consumo Médio por Horário")

plt.xlabel("Horário")

plt.ylabel("Energia Média (kWh)")

plt.legend(["Consumo Médio"])

plt.grid(axis='y')

plt.show()


# ==================================================
# HISTOGRAMA
# ==================================================

print("\n==============================")
print("HISTOGRAMA")
print("==============================\n")

plt.figure(figsize=(8, 6))

plt.hist(
    df["energia_kwh"],
    color="purple",
    bins=10
)

plt.title("Distribuição do Consumo de Energia")

plt.xlabel("Energia Consumida (kWh)")

plt.ylabel("Quantidade de Sessões")

plt.show()


# ==================================================
# BOXPLOT
# ==================================================

print("\n==============================")
print("BOXPLOT")
print("==============================\n")

plt.figure(figsize=(8, 6))

box = plt.boxplot(
    df["energia_kwh"],
    patch_artist=True
)

for caixa in box['boxes']:
    caixa.set_facecolor("lightblue")

plt.title("Boxplot do Consumo de Energia")

plt.xlabel("Consumo")

plt.ylabel("Energia Consumida (kWh)")

plt.show()


# ==================================================
# ESTATÍSTICA DESCRITIVA - ENERGIA
# ==================================================

print("\n==============================")
print("ESTATÍSTICA DESCRITIVA - ENERGIA")
print("==============================\n")

# Média
media = df["energia_kwh"].mean()
print(f"Média: {media:.2f}")

# Mediana
mediana = df["energia_kwh"].median()
print(f"Mediana: {mediana:.2f}")

# Moda
moda = df["energia_kwh"].mode()

print("\nModa:")
print(moda)

# Variância
variancia = df["energia_kwh"].var()
print(f"\nVariância: {variancia:.2f}")

# Desvio padrão
desvio = df["energia_kwh"].std()
print(f"Desvio Padrão: {desvio:.2f}")

# Amplitude
amplitude = df["energia_kwh"].max() - df["energia_kwh"].min()
print(f"Amplitude: {amplitude:.2f}")

# Quartis
quartis = df["energia_kwh"].quantile([0.25, 0.50, 0.75])

print("\nQuartis:")
print(quartis)


# ==================================================
# ESTATÍSTICA DESCRITIVA - TEMPO DE RECARGA
# ==================================================

print("\n==============================")
print("ESTATÍSTICA DESCRITIVA - TEMPO DE RECARGA")
print("==============================\n")

# Média
media2 = df["tempo_min"].mean()
print(f"Média: {media2:.2f}")

# Mediana
mediana2 = df["tempo_min"].median()
print(f"Mediana: {mediana2:.2f}")

# Moda
moda2 = df["tempo_min"].mode()

print("\nModa:")
print(moda2)

# Variância
variancia2 = df["tempo_min"].var()
print(f"\nVariância: {variancia2:.2f}")

# Desvio padrão
desvio2 = df["tempo_min"].std()
print(f"Desvio Padrão: {desvio2:.2f}")

# Amplitude
amplitude2 = df["tempo_min"].max() - df["tempo_min"].min()
print(f"Amplitude: {amplitude2:.2f}")

# Quartis
quartis2 = df["tempo_min"].quantile([0.25, 0.50, 0.75])

print("\nQuartis:")
print(quartis2)


# ==================================================
# FINALIZAÇÃO
# ==================================================

print("\n==============================")
print("ANÁLISE FINALIZADA COM SUCESSO")
print("==============================\n")