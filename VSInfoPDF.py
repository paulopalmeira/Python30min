import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import subprocess

musicas = ('Lib Provisória', 'Sentadão', 'Combatchy', 'Surtada', 'Cheirosa')
indice = np.arange(len(musicas))
acessos = [1068254,866216,763652,758198, 526324]

plt.bar(indice,acessos)
plt.xticks(indice,musicas)
plt.ylabel('Acessos')
plt.title('Ranking do Spotify em 21/12/2012')

# Define o nome do arquivo PDF
nome_arquivo = 'ranking_spotify2.pdf'

# Salva o gráfico em um arquivo PDF
plt.savefig(nome_arquivo)

#concatenando o caminho do pdf
caminho ='C:/Python30min/'
caminhao = caminho+nome_arquivo

# Abre o arquivo PDF automaticamente
subprocess.Popen([r'C:\Program Files\Google\Chrome\Application\chrome.exe', caminhao], shell=True)

# Fecha a janela do gráfico
plt.close()