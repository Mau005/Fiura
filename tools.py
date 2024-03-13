
def generate_atlas(nameFIle,size_x, size_y, quad_x, quad_y):
    normalize = {}
    quad = [size_x / quad_x, size_y / quad_y]
    count_x = size_x / quad_x
    count_y = size_y / quad_y
    aux = 0
    for x in range(0, int(count_x)):
        for y in range(0, int(count_y)):
            aux+=1
            normalize.update({str(aux): [x * quad_x, y * quad_y, quad_x, quad_y]})
            
    
    return {
        nameFIle:normalize
    }


import json
generate = generate_atlas("human.atlas",256,256, 64,64)

with open("assets/human.atlas", "w") as file:
    file.write(json.dumps(generate, indent=1))
    