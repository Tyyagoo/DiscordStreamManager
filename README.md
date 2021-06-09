<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** Tyyagoo, DiscordStreamManager, tyyago_, email, Discord Stream Manager, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


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
2. Crie um novo ambiente virtual
   ```sh
   python -m venv venv
   ```
3. Ative o ambiente virtual
   ```sh
   .\venv\Scripts\activate
   ```
4. Instale as dependências do projeto
   ```sh
   pip install -r requirements.txt
   ```
5. Abra a pasta do projeto
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

1. Abra o terminal na pasta do bot
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
