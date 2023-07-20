import pygltflib
from pygltflib.utils import ImageFormat
import os, sys, json

def main():
    # get the filename from the command line
    if (len(sys.argv) < 2):
        print("Usage: python fixer.py <filename>")
        return

    filename = sys.argv[1]

    # load the glb file
    glb = pygltflib.GLTF2().load(filename)

    # create textures folder
    if not os.path.exists("textures"):
        os.makedirs("textures")
        glb.convert_images(ImageFormat.FILE, "textures/")

    # for each texture in the textures folder append the filename and mimetype to an array
    textures = []

    for file in os.listdir("textures"):
        filename = os.fsdecode(file)

        textures.append({
            "name": filename.split(".")[0],
            "ext": os.path.splitext(filename)[1],
        })

    print(json.dumps(textures))

if __name__ == "__main__":
    main()