def gerar_html():
    html = """
    <html>
    <head>
        <title>Exemplo de HTML gerado por Python</title>
    </head>
    <body>
        <h1>Olá, mundo!</h1>
        <p>Este é um exemplo de HTML gerado por Python.</p>
    </body>
    </html>
    """
    return html

# Chama a função para gerar o código HTML
codigo_html = gerar_html()

# Salva o código HTML em um arquivo
nome_arquivo = "exemplo.html"
with open(nome_arquivo, "w") as arquivo:
    arquivo.write(codigo_html)

print(f"Arquivo HTML '{nome_arquivo}' gerado com sucesso!")
