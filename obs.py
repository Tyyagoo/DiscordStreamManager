import obswebsocket
from obswebsocket import obsws, requests, events

try:
    from settings import OBS_IP, OBS_PORT, OBS_PASSWORD, DEFAULT_SCENE, SCENE_NAME
except ImportError:
    print("Error on getting obs settings.\n"
          "Please verify settings.py file.")
    exit(0)


class OBS:
    debug_mode = True

    def __init__(self):
        self.ws = obsws(host=OBS_IP, port=OBS_PORT, password=OBS_PASSWORD)
        self.current_scene_name = ""
        self.ws.register(self.on_event)
        self.ws.register(self.on_switch_scene, events.SwitchScenes)

    def connect(self):
        self.ws.connect(host="localhost" if OBS_IP is None else OBS_IP, port=OBS_PORT)

    def disconnect(self):
        self.ws.disconnect()

    def reconnect(self):
        self.ws.reconnect()

    def call(self, request):
        self.ws.call(request)

    def change_scene(self, scene_name):
        if scene_name != self.current_scene_name:
            self.call(obswebsocket.requests.SetCurrentScene(scene_name))

    def change_scene_by_number(self, number: int = 0):
        if number <= 1:  # Streamer não está em um voice, ou está sozinho na call.
            self.change_scene(DEFAULT_SCENE)
        else:
            desired_scene = SCENE_NAME.replace("%", str(number))
            self.change_scene(desired_scene)

    # EVENTS
    def on_event(self, event=None):
        if OBS.debug_mode:
            print(f"{event}\n")

    def on_switch_scene(self, msg):
        self.current_scene_name = msg.getSceneName()

        if self.debug_mode:
            print(f"on_switch_scene: {self.current_scene_name}")
