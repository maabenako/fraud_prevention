# 🔍 Projeto de Detecção de Fraudes em Transações com Kedro

Este projeto implementa uma **pipeline completa e modular com Kedro** para detectar padrões de fraude em dados de transações financeiras, usando heurísticas de risco e modelos supervisionados de Machine Learning.

## ⚙️ Tecnologias Utilizadas

- "Python 3.12"
- "Kedro"
- "Pandas", "NumPy", "Scikit-learn"
- Estrutura de projeto limpa e reproduzível

---

## 💡 Objetivo

Detectar possíveis fraudes em transações com base em:
- Regras heurísticas baseadas em comportamento e localização
- Modelos supervisionados treinados em dados enriquecidos
- Padronização e escalonamento de variáveis para modelagem

---

## 🧠 Lógica de Negócio e Regras Heurísticas

Durante o enriquecimento dos dados, são aplicadas **regras de negócio** que marcam transações suspeitas:

### 📌 Regras Aplicadas

1. **Valor da Transação**
   - Transações muito acima da média histórica do usuário (5x maior)

2. **Horário**
   - Transações realizadas entre 00h e 05h são consideradas suspeitas

3. **Localização**
   - Transações feitas **fora da Europa** (com exceção do Reino Unido) são marcadas como suspeitas

4. **Velocidade de Transação**
   - Se o tempo desde a última transação for inferior a 60 segundos

---

## 📈 Estrutura da Pipeline

""
.
├── data/
│   ├── 01_raw/                  <- Dados brutos (CSV)
│   ├── 02_intermediate/         <- Dados tratados
│   ├── 03_primary/              <- Dados enriquecidos
│   ├── 05_model_input/          <- Base final para modelagem
│   ├── 06_models/               <- Modelo treinado
│   └── 08_reporting/            <- Avaliações do modelo
├── src/
│   └── fraud_detection/
│       ├── pipelines/
│       │   ├── enriquecimento/
│       │   └── detectar_fraudes/
│       └── pipeline_registry.py
└── README.md
""

---

## 🧪 Etapas do Projeto

### 1. "enriquecer_transacoes"
- Calcula tempo desde a última transação
- Gera média, frequência mensal, gasto total
- Aplica regras e define a coluna "is_fraud"

### 2. "preparar_dados_modelo"
- Seleciona variáveis relevantes
- Normaliza dados com "StandardScaler"
- Separa variável alvo: "is_fraud"

### 3. "treinar_modelo"
- Treina modelo "RandomForestClassifier" para classificação de fraude

### 4. "avaliar_modelo"
- Gera relatório com métricas de classificação

---

## 🚀 Como Executar

1. Clone o projeto:

""
git clone https://github.com/seuusuario/nome-do-repo.git
cd nome-do-repo
""

2. Instale as dependências (ex: com Miniconda):

""
conda create -n fraud python=3.12 -y
conda activate fraud
pip install -r src/requirements.txt
""

3. Execute o pipeline:

""
kedro run
""

---

## 🧠 Resultado Esperado

Ao final da execução, você terá:
- Arquivo ".csv" com marcações de fraude
- Modelo ".pkl" treinado para futuras previsões
- Relatório com métricas como precisão, recall, F1-score

---

## 📌 Observações

- Este projeto simula cenários de fraude, ideal para testes e aprendizado.
- Pode ser adaptado para bases reais, conectando com APIs de transações, bancos de dados, etc.

---

## 💖 Autoria

Feito com 💡 e muito amor pela [Marcela](https://github.com/seuusuario), com o suporte carinhoso do Kedro e de sua IA bestie 💻✨
