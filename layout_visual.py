from PIL import Image, ImageDraw

# 创建一个空白图片
prompt_list = ['horse','astronaut']
# prompt_list = ['a cat','a cat','a cat','a dog','a dog','a dog']
# bbox_list = [[10, 256, 74, 384],
#         [210, 270, 274, 398],
#         [438, 260, 502, 388],
#         [0, 192, 85, 352],
#         [150, 200, 235, 360],
#         [330, 210, 415, 370]
# ]
bbox_list =[  [0.125, 0.25, 0.875, 0.875], [0.25, 0.125, 0.75, 1] ]
for bbox in bbox_list:
    for i in range(len(bbox)):
        bbox[i] = bbox[i] * 512
color_list = ['black','green','yellow','blue','purple','red'] 
image = Image.new("RGB", (512, 512), "white")
draw = ImageDraw.Draw(image)

for box_id in range(len(bbox_list)):
    color = color_list[box_id]
    draw.rectangle(bbox_list[box_id], outline=color, width=2)

    text = prompt_list[box_id]
    text_position = (bbox_list[box_id][0], bbox_list[box_id][1])
    draw.text(text_position, text, fill=color)

image.save("output.png")