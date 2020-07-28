STATUS = {0: "corridor",
          1: "wall",
          5: "macgyver",
          6: "guardian",
          7: "exit"}
    
IMAGES = {"wall": "./ressource/wall.png",
          "corridor": "",
          "macgyver": "",
          "exit": "./ressource/exit2.png",
          "guardian": "./ressource/Gardien.png"}

status = ""
image = ""
def essai(value):
    status= STATUS[value]
    image = IMAGES[status]
    print(status)
    print(image)

essai(1)

