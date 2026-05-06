"""
Quando você se exercita fisicamente para fortalecer seu coração,
deve manter sua frequência cardíaca dentro de uma faixa por pelo menos 20
minutos. Para encontrar essa faixa, subtraia sua idade de 220. Essa
diferença é sua frequência cardíaca máxima por minuto. Seu coração
simplesmente não baterá mais rápido que esse máximo (220 - idade).
Ao se exercitar para fortalecer seu coração, você deve manter sua
frequência cardíaca entre 65% e 85% da frequência cardíaca máxima.
"""
idade = input(int('Por favor, digite sua idade: 23 '))
frequencia = 220 - idade
print(f'Ao se exercitar para fortalecer o coração, você deve manter sua frequência cardíaca entre 128 e 167 batimentos por minuto.')