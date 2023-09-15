## Aimbot-with-Python

# Criando um Aimbot para o site Aimbooster com python.
  
<div align="center">
  <a href="https://youtu.be/3ENtYIiqMlE">
    <img src="https://img.youtube.com/vi/3ENtYIiqMlE/0.jpg" alt="Assista ao vídeo no YouTube">
  </a>
</div>

pyautogui: Esta biblioteca permite controlar o mouse e o teclado do Python. É usada para tirar um screenshot, obter a cor do pixel e clicar no mouse.<br>
keyboard: Esta biblioteca permite detectar pressionamentos de teclas. É usada para verificar se o usuário pressionou a tecla c para encerrar o programa.<br>
win32api, win32con: Essas bibliotecas são da API do Windows. São usadas para realizar operações de mouse e teclado de baixo nível, como clicar no mouse.<br>
time: Esta biblioteca permite pausar o programa por um determinado período de tempo. Isso é usado para desacelerar o loop para que os cliques do mouse não sejam muito rápidos.<br>

O código primeiro define uma função chamada click(). Essa função usa a biblioteca win32api para simular um clique do mouse nas coordenadas especificadas.
O loop principal do código começa tirando um screenshot da tela. O screenshot é salvo em um arquivo chamado example.jpg. A largura e a altura do screenshot são então obtidas.
O loop então itera pelos pixels do screenshot. Para cada pixel, os valores vermelho, verde e azul (RGB) são obtidos. Se os valores RGB corresponderem à cor desejada, o mouse é clicado nessa localização.

O loop continua até que o usuário pressione a tecla c.
