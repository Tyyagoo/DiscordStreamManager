TOKEN: str = "token_here"
STREAMER_ID: int = None

OBS_IP = None
OBS_PORT = 4444
OBS_PASSWORD = ""

DEFAULT_SCENE = "OnlyStreamer"
# Cena padrão quando o streamer conecta em um chat de voz que só tenha ele.
# É pra essa cena que irá caso o streamer saia do chat de voz.
# OBS: Quando o streamer não está em um chat de voz, o bot NÃO altera nenhuma cena.

SCENE_NAME = "%pessoas"
# O símbolo de porcentagem representa o número de pessoas.
# Exemplo: VDN6pessoas -> VDN%pessoas

# Para passar ads mais facilmente, e bloquear a mudança de cenas por parte do bot.
# Key: Value -> kto: "ad kto"
# Nota: A key não pode ter espaços, e o valor deve ser idêntico ao nome da cena no OBS.
# Para passar o ad da kto, use !ad kto
# Para passar o da "adidas", use !ad adidas
# Para apenas bloquear o gerenciamento automático de cenas, digite apenas !ad
# Você pode adicionar quantos anunciantes quiser, basta seguir o modelo abaixo.
SPONSORS = {
    "KTO": "AD Kto",
    "adidas": "AD Adidas",
}
