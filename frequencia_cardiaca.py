"""
Quando você se exercita fisicamente para fortalecer seu coração,
deve manter sua frequência cardíaca dentro de uma faixa por pelo menos 20
minutos. Para encontrar essa faixa, subtraia sua idade de 220. Essa
diferença é sua frequência cardíaca máxima por minuto. Seu coração
simplesmente não baterá mais rápido que esse máximo (220 - idade).
Ao se exercitar para fortalecer seu coração, você deve manter sua
frequência cardíaca entre 65% e 85% da frequência cardíaca máxima.
"""
idade = int(input('Por favor, digite sua idade: '))
frequencia = 220 - idade
percent_frequ_min = (frequencia * 65) /100
percent_frequ_max = (frequencia * 85) /100
print(f'Ao se exercitar para fortalecer o coração, você deve manter sua frequência cardíaca entre {percent_frequ_min} e {percent_frequ_max} batimentos por minuto.')