## Atenção

[The Future of discord.py](https://gist.github.com/Rapptz/4a2f62751b9600a31a0d3c78100287f1)


### Pré-requisitos

* [Python 3.6.8](https://www.python.org/downloads/release/python-368/)
* [OBS Studio](https://obsproject.com/pt-br/download)
* [OBS Websockets 4.9.0](https://github.com/Palakis/obs-websocket/releases)
* [Criar um BOT do discord](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token)

### Instalação

1. Clone o repositório
   ```sh
   git clone https://github.com/Tyyagoo/DiscordStreamManager.git
   ```
2. Vá para a pasta do projeto
   ```sh
   cd DiscordStreamManager
   ```
3. Crie um novo ambiente virtual
   ```sh
   python -m venv venv
   ```
4. Ative o ambiente virtual
   ```sh
   .\venv\Scripts\activate
   ```
5. Instale as dependências do projeto
   ```sh
   pip install -r requirements.txt
   ```
6. Abra a pasta do projeto
   ```sh
   start .
   ```

Note que existe um arquivo chamado "_settings.py". Remova o "underline" do nome do arquivo.

Agora abra o arquivo com qualquer editor de texto.
* settings.py
```python
   TOKEN: str = "token_here"
   STREAMER_ID: int = None
   
   OBS_IP = None
   OBS_PORT = 4444
   OBS_PASSWORD = ""
   
   DEFAULT_SCENE = "Default"
   SCENE_NAME = "%"

   SPONSORS = {}
   ```

As informações mais relevantes **DEVEM** ser substituídas.
1. TOKEN
2. STREAMER_ID
3. DEFAULT_SCENE
4. SCENE_NAME
5. SPONSORS

**ATENÇÃO:** Não altere as informações do OBS, a menos que você saiba o que está fazendo.



<!-- USAGE EXAMPLES -->
## Como Usar

**Observação:** Caso você ainda não tenha fechado o terminal, vá direto ao passo 3.

1. Vá para a pasta do projeto
    ```sh
    cd C:\path\DiscordStreamManager
    ```
2. Ative o ambiente virtual
   ```sh
   .\venv\Scripts\activate
   ```
2. Inicie o bot
   ```sh
   python main.py
   ```

**Observação:** Sempre que for utilizar o programa, você deve refazer esses 3 passos, na ordem correta.


<!-- HOW EXAMPLES -->
## Como Funciona
   O BOT deve ser um membro do servidor em que o streamer se conectará a algum canal de voz.
   Ele automaticamente irá observar o membro dono do `STREAMER_ID`, e atualizar o HUD da live de acordo.
   
   **Comandos:**
   * !ad <param=None>
     ```
     Esse comando fará com que o bot pare de atualizar o HUD automaticamente, evitando assim mudanças indesejadas.
     Você pode passar um parâmetro informando se deseja passar um "anúncio personalizado", caso tenha patrocinadores.
          
     Exemplos:
     !ad bang_energy
     !ad nike
     !ad
     
     ATENÇÃO:
     Quando você passa um parâmetro para o bot, ele ira travar as atualizações automáticas até que você digite !ad novamente.
     Se não passar nenhum parâmetro, o bot vai sempre alternar entre o gerenciamento automático e o não gerenciamento.
     ```

   * !forceupdate <alias=['forceupdate', 'update', 'fu']>
   ```
      Força a atualização do HUD. Use caso o HUD por algum motivo não esteja mostrando o número correto de usuários.
      
      Exemplos:
      !fu
      !update
      !forceupdate
   ```

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contato

Twitter - [@tyyago_](https://twitter.com/tyyago_)

Discord - Tyyago#2357
