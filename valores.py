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
      # Fluxo de caixa futuro da empresa em dólares
    taxa_desconto = 0.1  # Taxa de desconto (custo de capital)

     # Avaliação da empresa usando o método do Fluxo de Caixa Descontado (DCF)
    valor_empresa = sum([cf / (1 + taxa_desconto) ** (2) * 100 for i, cf in enumerate(fluxo_caixa)])

     # Imprimir o valor real da empresa
    print(f"O valor real da empresa é: {valor_empresa} dólares")


    pivot_point = (dados['High'] + dados['Low'] + dados['Close']) / 3
    support_1 = (2 * pivot_point) - dados['High']
    support_2 = pivot_point - ( dados['High'] - dados['Low'] )
    support_3 = dados['Low'] - 2 * (dados['High'] - pivot_point)
    resistance_1 = (2 * pivot_point) - dados['Low']
    resistance_2 = pivot_point + (dados['High'] - dados['Low'])
    resistance_3 = dados['High'] + 2 * (pivot_point - dados['Low'])

    print(pivot_point, support_1, support_2, support_3, resistance_1, resistance_2, resistance_3)


    # Imprime os resultados
    print("Pontos de Pivô:")
    print("Pivot Point:", pivot_point)
    print("Suporte 1:", support_1)
    print("Suporte 2:", support_2)
    print("Suporte 3:", support_3)
    print("Resistência 1:", resistance_1)
    print("Resistência 2:", resistance_2)
    print("Resistência 3:", resistance_3)


    return valor_justo

# Símbolo da ação a ser avaliada
symbol = 'AAPL'  # Exemplo para a Apple Inc.

# Taxa de desconto (custo de capital) para o DCF
taxa_desconto = 0.1

# Obter dados da ação
dados_acao = obter_dados_acao(symbol)

# Calcular o valor justo da empresa
valor_justo = calcular_valor_justo(dados_acao, taxa_desconto)


print(f"O valor justo da empresa {symbol} é: {valor_justo}")

  

