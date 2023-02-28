

class Scene:
    def __init__(self):
        self.objects = []
        self.switch_scene = ""

    def handle_input(self, event):
        for obj in self.objects:
            obj.handle_input(event)

    def update(self, dt):
        for obj in self.objects:
            obj.update(dt)

    def render(self, display):
        for obj in self.objects:
            obj.render(display)


class SceneManager:
    def __init__(self, scenes_dict, initial_scene_key):
        self.scenes = scenes_dict
        self.current_scene = None
        self.set_scene(initial_scene_key)

    def set_scene(self, scene_key):
        self.current_scene = self.scenes[scene_key]

    def switch_scene(self):
        if len(self.current_scene.switch_scene) > 1:
            self.set_scene(self.current_scene.switch_scene)

    def run_scene(self, events, display, dt):
        self.current_scene.handle_input(events)
        self.current_scene.update(dt)
        self.current_scene.render(display)
        self.switch_scene()
