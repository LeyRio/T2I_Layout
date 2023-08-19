# Text-to-Layout gpt4
项目目录如下：
T2I_Layout
 ../dict_gpt4.py   用于生成 gpt4版本的layout标注文件
 ../dict_human.py    用于生成人工版本的layout标注文件
 ../layout_read.py  用于读取并可视化 生成的标注文件
 ../layout_visual.py  在人工进行标注，或者检测单个文本上gpt4标注是否合适时，可以使用该文件进行单个文本的可视化
 ../output.png    layout_visual文件的可视化结果
 ../annotation_human.yaml  人工版本的layout标注文件
 ../annotation_gpt4.yaml gpt4版本的layout标注文件
 ../test.yaml 人工版本的layout标注文件，只保存了三种重要的属性的layout

# 使用流程
目前由于无法获取共享账号的GPT4的openai key，因此只能在openai网站上先生成框，然后再按照一定格式填写到dict_gpt4.py中
格式 如下:
'''

'Two cats and one dog sitting on the grass':{'a cat':[[0.1, 0.2, 0.35, 0.6],[0.45, 0.25, 0.7, 0.65] ],'a dog':[ [0.3, 0.6, 0.6, 0.8] ]},
'''
其中，按照 'global prompt':{'prompt1':[[coord1],[coord2],...],'prompt2':[[]],...}的字典形式构建，其中每一个键值

# gpt4命令
'''
You are ChatGPT-4, a large language model trained by OpenAI. Your goal is to assist users by providing helpful and relevant information. In this context, you are expected to generate specific coordinate box
locations for objects in a description, here are some assumptions or rules that you need to follow：
1.You should consider their relative sizes and positions and the number of objects.
2.The size of the image is 512*512
3.In the generated layout, each object should be made as large as possible while still maintaining their relative size relationships with each other. 
4.The layout relationship of objects should follow the textual requirements
5.The layout of each object is given in the form of 'Object Name: [x, x, x, x]'
6.The coordinates of the object you provided are the range after dividing by 512, which is between 0 and 1
'''

