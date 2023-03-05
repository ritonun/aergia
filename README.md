Aergia
=========

Aergia is my own pygame engine. Updated every now and then, I try to make it useful for quicker dev time.

## Read the docs
[Link to documentation](https://ritonun.github.io/aergia/)


## Quick Start
Project Structure:  
```
project_name
|_res/
  |_tileset/
    |_tileset.png
  |_fonts/
  	|_arial.ttf	
  |_images/
    |_player/
  	  |_up.png
  	  |_down.png
  	|_mob/
  	  |_slime.png

```

Example:  
```
import os
from aergia import *
from local_file import Scene1, Scene2

app = App()

# Load Ressources
app.ressource_manager = RessourceManager(ressource_path=os.path.join("..", "res", ""))
ressource_manager.load_tilesets("tileset", tile_width, tile_height)
ressource_manager.load_images("images", subfolders=["player", "slime"])
ressource_manager.load_fonts("fonts")

# Init the scene
scenes = {"scene1": Scene1(), "scene2": Scene2}
app.scene_manager = SceneManager(scenes, "scene1")

# Run the app
app.mainloop() 
```

## Version
Current Version: v0.0.2a
