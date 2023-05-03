import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

musicas = ('Lib Provisória', 'Sentadão', 'Combatchy', 'Surtada', 'Cheirosa')
indice = np.arange(len(musicas))
acessos = [1068254,866216,763652,758198, 526324]

plt.bar(indice,acessos)
plt.xticks(indice,musicas)
plt.ylabel('Acessos')
plt.title('Ranking do Spotify em 21/12/2012')

plt.show()