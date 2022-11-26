# Roleta de Aposta - Bot Telegram

Um bot criado 100% com python afim de analisar e verificar repetições de apostas nas roletas da plataforma Betano/Playtech. 
O robô tem conexão com o telegram utilizando o pyTelegramBotAPI para fazer os envios das mensagens de modo simples. 

O BOT NÃO ESTÁ MAIS ATUALIZADO, MAS PARA FAZER A ATUALIZAÇÃO, SE NECESSÁRIO, É SIMPLES.

A criação deste bot foi feita afim de estudar webscraping e trabalhar com o Selenium. 

## Como instalar.

A instalação do bot é simples, mas requer a verificações de alguns detalhes, principalmente nos <code>XPATH</code> do site. 

- Clone o repositório: <code>git clone https://github.com/lithoykai/roulette_bet_bot-</code></br>
- Use <code>pip3 install -r requirements.txt</code> para instalar os requesitos.</br>
- Abra o arquivo <code>actions.py</code> e altere as informações de login para conectar a Betano.
- Abra o arquivo <code>messagem.py</code> e coloque o <code>TOKEN</code> e o <code>GROUPID</code>
- Execute o index.py, lá você pode alterar qual roleta da Playtech você quer conectar alterando apenas o link. 


