Aergia
=========

Aergia is my own pygame engine. Updated every now and then, I try to make it useful for quicker dev time.

## Quick Start
```
from aergia import *
from local_file import Scene1, Scene2

app = App()

# Load Ressources
ressource_loader = RessourceLoader()
ressource_loader.load_tilesets(path_to_tileset, tile_width, tile_height)

# Init the scene
scenes = {"scene1": Scene1(), "scene2": Scene2}
app.scene_manager = SceneManager(scenes, "scene1")

# Run the app
app.mainloop() 
```

## Version
Current Version: v0.0.2a
