from PIL import Image, ImageDraw
import os
import yaml

# 该文件展示了如何读取并利用标注绘制框

# 明确路径并加载文件
files = open('/home/liyou/T2I_Layout/annotations_gpt4.yaml','r')

# 不同的框用不同的颜色进行标注
color_list = ['black','green','yellow','blue','purple','red'] 
cfg = files.read()

d = yaml.load(cfg,Loader = yaml.FullLoader)  # 用load方法转字典

# 遍历标注的每个key，也就是遍历每个全局文本
for prompt in d.keys():
    # 在这里全局文本作为文件名得到可视化图像
    file_name = prompt
    objects = d[prompt]

    # 创建空白图像，为了可视化每个框的位置
    image = Image.new("RGB", (512, 512), "white")
    draw = ImageDraw.Draw(image)


    bbox_final = []
    prompt_final = []

    # 在每个全局文本对应的子字典内，遍历所有的物体
    # 因为一个物体名称(比如猫) 可能对应多个框，依次将其append到bbox_final中，最终就能够得到我们需要的形式
    for instances in objects.keys():
        bbox_list = objects[instances]
        for bbox in bbox_list:
            prompt_final.append(instances)
            bbox_final.append(bbox)
    # 将框恢复到512尺度之下
    for bbox in bbox_final:
        for i in range(len(bbox)):
            bbox[i] = bbox[i] * 512
    print(bbox_final)
    print(prompt_final)

    # 根据框及其对应的类别名称，绘制可视化图像
    for box_id in range(len(bbox_final)):
        color = color_list[box_id]
        draw.rectangle(bbox_final[box_id], outline=color, width=2)

        text = prompt_final[box_id]
        text_position = (bbox_final[box_id][0], bbox_final[box_id][1])
        draw.text(text_position, text, fill=color)

    image.save(f"./mid_result_gpt4/{file_name}.png")
    
# 创建一个空白图片
# prompt_list = ['cat ','a tennis racket']
# # prompt_list = ['a cat','a cat','a cat','a dog','a dog','a dog']
# # bbox_list = [[10, 256, 74, 384],
# #         [210, 270, 274, 398],
# #         [438, 260, 502, 388],
# #         [0, 192, 85, 352],
# #         [150, 200, 235, 360],
# #         [330, 210, 415, 370]
# # ]
# bbox_list = [[0.6,0.2,1.0,0.8],[0.1,0.3,0.4,0.7]]
# for bbox in bbox_list:
#     for i in range(len(bbox)):
#         bbox[i] = bbox[i] * 512
# color_list = ['black','green','yellow','blue','purple','red'] 
# image = Image.new("RGB", (512, 512), "white")
# draw = ImageDraw.Draw(image)

# for box_id in range(len(bbox_list)):
#     color = color_list[box_id]
#     draw.rectangle(bbox_list[box_id], outline=color, width=2)

#     text = prompt_list[box_id]
#     text_position = (bbox_list[box_id][0], bbox_list[box_id][1])
#     draw.text(text_position, text, fill=color)

# 