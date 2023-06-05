import yfinance as yf

# Função para obter dados de uma ação específica
def obter_dados_acao(symbol):
    stock = yf.Ticker(symbol)
    dados = stock.history(period='5y')
    return dados

# Função para calcular o valor justo da empresa usando o método do fluxo de caixa descontado (DCF)
def calcular_valor_justo(dados, taxa_desconto):
    fluxo_caixa = dados['Close'].pct_change()
    fluxo_caixa.iloc[0] = 0
    valor_justo = ((fluxo_caixa / (1 + taxa_desconto) * 100)).sum()
    return valor_justo

# Símbolo da ação a ser avaliada
symbol = 'AAPL'  # Exemplo para a Apple Inc.

# Taxa de desconto (custo de capital) para o DCF
taxa_desconto = 0.1

# Obter dados da ação
dados_acao = obter_dados_acao(symbol)

# Calcular o valor justo da empresa
valor_justo = calcular_valor_justo(dados_acao, taxa_desconto)

# Imprimir o valor justo da empresa
print(f"O valor justo da empresa {symbol} é: {valor_justo}")

