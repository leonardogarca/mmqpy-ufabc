# MMQPY-UFABC

Script feito pra calcular a reta de regressão usando a fórmula que os relatórios dos laboratórios da ufabc pedem.

Não é bonito, mas funciona.

# Como usar

Só rodar o mmq.py no terminal. Tem dois modos: ler os valores de um .csv, ou digitar cada valor individualmente.
Caso queira importar um .csv, crie uma planilha com três colunas: x, y, sigmay. E coloque nelas os valores de x, y, e a incerteza de cada valor de y separados por ponto. Caso esteja usando o Sheets, para mudar os valores de virgula para ponto, é só ir em Arquivo - Configurações e mudar o local de Brasil para Estados Unidos.
Com o .csv baixado e no diretório do script, é só entrar no terminal "python3 mmq.py NomeDoArquivoCSV.csv"
No final, serão mostrados os valores do coeficiente angular e do coeficiente linear, junto com as suas incertezas.
