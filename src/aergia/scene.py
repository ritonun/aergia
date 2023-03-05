

class Scene:
    """Scene class

    Attributes:
        objects (list): list of object in the scene
        switch_scene (str): new scene key
    """

    def __init__(self):
        self.objects = []
        self.switch_scene = ""

    def handle_input(self, event):
        """handle event in the scene

        Args:
            event (events): list of pygame event
        """
        for obj in self.objects:
            obj.handle_input(event)

    def update(self, dt):
        """Update all objects in the scene

        Args:
            dt (float): delta time between two frames
        """
        for obj in self.objects:
            obj.update(dt)

    def render(self, display):
        """Render all objects in the scene

        Args:
            display (Surface): Surface to render the scene
        """
        for obj in self.objects:
            obj.render(display)


class SceneManager:
    """SceneManager to handle all the scene in the app

    Attributes:
        current_scene (Scene): Current scene
        scenes (dict): Dict containning all the scene
    """

    def __init__(self, scenes_dict: dict, initial_scene_key: str):
        """Initialize the SceneManager class

        Args:
            scenes_dict (dict): Dict containning all the scene of the app
            initial_scene_key (str): Initial scene key in the scenes_dict
        """
        self.scenes = scenes_dict
        self.current_scene = None
        self.set_scene(initial_scene_key)

    def set_scene(self, scene_key):
        """Set scene

        Args:
            scene_key (str): scene key to change the current scene
        """
        self.current_scene = self.scenes[scene_key]

    def switch_scene(self):
        """Handle scene change
        """
        if len(self.current_scene.switch_scene) > 1:
            self.set_scene(self.current_scene.switch_scene)

    def run_scene(self, events, display, dt):
        """Run the scene

        Args:
            events (events): List of pygame events
            display (Surface): Surface to render the scene
            dt (float): Delta time between two scenes
        """
        self.current_scene.handle_input(events)
        self.current_scene.update(dt)
        self.current_scene.render(display)
        self.switch_scene()
