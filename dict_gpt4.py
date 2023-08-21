import yaml

dicts = {
  'A red colored car':{'Red Car': [[0.1, 0.2, 0.9, 0.8]]},
  'A black colored car':{'Black Car': [[0.1, 0.2, 0.9, 0.8]]},
  'A pink colored car':{'Pink Car': [[0.1, 0.2, 0.9, 0.8]]},
  'A black colored dog':{'Black Dog':[[0.15, 0.25, 0.85, 0.75]]},
  'A red colored dog':{'Red Dog':[[0.15, 0.25, 0.85, 0.75]]},
  'A blue colored dog':{'Blue Dog':[[0.15, 0.25, 0.85, 0.75]]},
  'A green colored banana':{'Green Banana':[[0.4, 0.1, 0.6, 0.9]]},
  'A red colored banana':{'Red banana':[[0.4, 0.1, 0.6, 0.9]]},
  'A black colored banana':{'Black Banana':[[0.4, 0.1, 0.6, 0.9]]},
  'A white colored sandwich':{'White colored sandwich':[[0.2, 0.35, 0.8, 0.65]]},
  'A black colored sandwich':{'black colored sandwich':[[0.2, 0.35, 0.8, 0.65]]},
  'An orange colored sandwich':{'orange colored sandwich':[[0.2, 0.35, 0.8, 0.65]]},
  'A pink colored giraffe':{'pink colored giraffe':[[0.35, 0.05, 0.65, 0.95]]},
  'A yellow colored giraffe':{'yellow colored giraffe':[[0.35, 0.05, 0.65, 0.95]]},
  'A brown colored giraffe':{'brown colored giraffe':[[0.35, 0.05, 0.65, 0.95]]},
  'A red car and a white sheep':{'red car':[[0.05, 0.05, 0.6, 0.5]],'white sheep':[[0.65, 0.2, 0.9, 0.4]]},
  'A blue bird and a brown bear':{'blue bird':[[0.65, 0.1, 0.8, 0.25]],'brown bear':[[0.1, 0.5, 0.9, 0.9] ]},
  'A green apple and a black backpack':{'green apple':[ [0.1, 0.25, 0.2, 0.35]],'black backpack':[ [0.2, 0.3, 0.8, 0.8] ]},
  'A green cup and a blue cell phone':{'green cup':[[0.1, 0.4, 0.35, 0.7]],'blue cell phone':[[0.45, 0.5, 0.7, 0.7]]},
  'A yellow book and a red vase':{'yellow book':[ [0.1, 0.6, 0.6, 0.8] ],'red vase':[[0.65, 0.45, 0.8, 0.85] ]},
  'A white car and a red sheep':{'white car':[[0.05, 0.05, 0.6, 0.5]],'red sheep':[[0.65, 0.2, 0.9, 0.4]]},
  'A brown bird and a blue bear':{'brown bird':[[0.65, 0.1, 0.8, 0.25]],'blue bear':[[0.1, 0.5, 0.9, 0.9] ]},
  'A black apple and a green backpack':{'black apple':[ [0.1, 0.25, 0.2, 0.35]],'green backpack':[[0.2, 0.3, 0.8, 0.8]]},
  'A blue cup and a green cell phone':{'blue cup':[[0.1, 0.4, 0.35, 0.7]],'green cell phone':[[0.45, 0.5, 0.7, 0.7]]},
  'A red book and a yellow vase':{'red book':[ [0.1, 0.6, 0.6, 0.8]],'yellow vase':[[0.65, 0.45, 0.8, 0.85] ]},
  ###
  'One car on the street':{'a car':[[0.2,0.2,0.8,0.8]]},
  'Two cars on the street':{'a car':[[0.05, 0.6, 0.45, 0.9] , [0.55, 0.6, 0.95, 0.9]]},
  'Three cars on the street':{'a car':[[0.05, 0.6, 0.32, 0.95] ,[0.34, 0.6, 0.66, 0.95], [0.68, 0.6, 0.95, 0.95] ]},
  'Four cars on the street':{'a car':[[0.05, 0.7, 0.47, 0.98],[0.53, 0.7, 0.95, 0.98], [0.05, 0.45, 0.47, 0.7] , [0.53, 0.45, 0.95, 0.7] ]},
  'Five cars on the street':{'a car':[ [0.05, 0.60, 0.30, 0.85], [0.55, 0.60, 0.80, 0.85], [0.15, 0.40, 0.40, 0.60],  [0.60, 0.35, 0.85, 0.55],[0.35, 0.10, 0.65, 0.30]]},
  'One dog on the street':{'a dog':[[0.2,0.2,0.8,0.8]]},
  'Two dogs on the street':{'a dog':[[0.05, 0.6, 0.45, 0.9] ,[0.55, 0.6, 0.95, 0.9]]},
  'Three dogs on the street':{'a dog':[[0.05, 0.6, 0.32, 0.95] ,[0.34, 0.6, 0.66, 0.95], [0.68, 0.6, 0.95, 0.95] ]},
  'Four dogs on the street':{'a dog':[[0.05, 0.7, 0.47, 0.98],[0.53, 0.7, 0.95, 0.98], [0.05, 0.45, 0.47, 0.7] , [0.53, 0.45, 0.95, 0.7] ]},
  'Five dogs on the street':{'a dog':[  [0, 0.375, 0.2, 0.875], [0.2, 0.375, 0.4, 0.875],   [0.4, 0.375, 0.6, 0.875],  [0.6, 0.375, 0.8, 0.875],[0.8, 0.375, 1, 0.875]]},
  'One cat and one dog sitting on the grass':{'a cat':[[0.55, 0.45, 0.75, 0.65]],'a dog':[[0.10, 0.35, 0.55, 0.75]]},
  'One cat and two dogs sitting on the grass':{'a cat':[[0.35, 0.45, 0.55, 0.65]],'a dog':[[0.05, 0.30, 0.35, 0.75],[0.55, 0.35, 0.85, 0.70]]},
  # default model
  'One cat and three dogs sitting on the grass':{'a cat':[ [0.15, 0.2, 0.45, 0.6]],'a dog':[[0.5, 0.2, 0.75, 0.45], [0.1, 0.5, 0.35, 0.75], [0.55, 0.55, 0.8, 0.8]]},
  'Two cats and one dog sitting on the grass':{'a cat':[[0.1, 0.2, 0.35, 0.6],[0.45, 0.25, 0.7, 0.65] ],'a dog':[ [0.3, 0.6, 0.6, 0.8] ]},
  'Two cats and two dogs sitting on the grass':{'a cat':[[0.1, 0.2, 0.35, 0.6],[0.45, 0.25, 0.7, 0.65]],'a dog':[[0.2, 0.6, 0.45, 0.85] ,[0.55, 0.55, 0.8, 0.85]]},
  'Two cats and three dogs sitting on the grass':{'a cat':[[0.1, 0.2, 0.35, 0.6] ,[0.45, 0.25, 0.7, 0.65]],'a dog':[[0.2, 0.6, 0.45, 0.85],[0.55, 0.55, 0.8, 0.85], [0.75, 0.35, 0.9, 0.6]]},
  'Three cats and one dog sitting on the grass':{'a cat':[ [0.1, 0.2, 0.3, 0.5],[0.35, 0.25, 0.55, 0.55],[0.6, 0.2, 0.8, 0.5] ],'a dog':[[0.3, 0.6, 0.6, 0.8]]},
  'Three cats and two dogs sitting on the grass':{'a cat':[ [0.1, 0.1, 0.3, 0.4] , [0.4, 0.1, 0.6, 0.4] ,[0.7, 0.1, 0.9, 0.4] ],'a dog':[[0.2, 0.6, 0.45, 0.8] , [0.55, 0.6, 0.8, 0.8]]},
  'Three cats and three dogs sitting on the grass':{'a cat':[ [0.1, 0.1, 0.3, 0.4] ,[0.4, 0.1, 0.6, 0.4], [0.7, 0.1, 0.9, 0.4]],'a dog':[[0.1, 0.5, 0.3, 0.7],[0.4, 0.5, 0.6, 0.7] ,[0.7, 0.5, 0.9, 0.7] ]},
  'A train on top of a surfboard':{'a train':[[0.3, 0.2, 0.7, 0.4]],'a surfboard':[ [0.1, 0.6, 0.9, 0.7] ]},
  'A wine glass on top of a dog':{'a wine glass':[[0.4, 0.1, 0.6, 0.3]  ],'a dog':[ [0.2, 0.2, 0.8, 0.8]]},
  'A bicycle on top of a boat':{'a bicycle':[[0.3, 0.1, 0.7, 0.4]],'a boat':[ [0.1, 0.5, 0.9, 0.7] ]},
  'An umbrella on top of a spoon':{'an umbrella':[[0.3, 0.1, 0.7, 0.4] ],'a spoon':[[0.4, 0.4, 0.6, 0.6]]},
  'A laptop on top of a teddy bear':{'a laptop':[ [0.25, 0, 0.75, 0.25]],'a teddy bear':[[0.125, 0.25, 0.875, 0.916]]},
  ####
  'A giraffe underneath a microwave':{'a giraffe':[ [0.4375, 0.125, 0.5625, 0.875]],'microwave':[[0.375, 0, 0.625, 0.125]]},
  'A donut underneath a toilet':{'a donut':[[0.417, 0.5, 0.583, 0.666]],'a toliet':[[0.333, 0, 0.666, 0.5]]},
  'A hair drier underneath a sheep':{'a hair drier':[[0.375, 0.333, 0.625, 0.458]],'a sheep':[[0.25, 0, 0.75, 0.333]]},
  'A tennis racket underneath a traffic light':{'a tennis racket':[[0.417, 0.25, 0.583, 0.75]],'a traffic light':[[0.4375, 0, 0.5625, 0.25]]},
  ####
  'A zebra underneath a broccoli':{'a zebra':[[0.25, 0.125, 0.75, 0.75]],'a broccoli':[[0.4375, 0, 0.5625, 0.125]]},
  'A banana on the left of an apple':{'a banana':[[0.1, 0.2, 0.3, 0.8]],'an apple':[[0.4, 0.2, 0.6, 0.8]]},
  'A couch on the left of a chair':{'a couch':[[0.1, 0.2, 0.4, 0.8] ],'a chair':[ [0.5, 0.2, 0.7, 0.8]]},
  'A car on the left of a bus':{'a car':[ [0, 0.375, 0.333, 0.625]],'a bus':[[0.333, 0.25, 1, 0.75]]},
  'A cat on the left of a dog':{'a cat':[ [0.1, 0.2, 0.3, 0.7] ],'a dog':[ [0.4, 0.1, 0.7, 0.8]]},
  'A carrot on the left of a broccoli':{'a carrot':[ [0.1, 0.2, 0.3, 0.8]],'a broccoli':[[0.4, 0.2, 0.7, 0.8]]},
  'A pizza on the right of a suitcase':{'a pizza':[[0.5, 0.2, 0.9, 0.8]],'a suitcase':[[0.1, 0.2, 0.4, 0.8]]},
  'A cat on the right of a tennis racket':{'a cat':[[0.6, 0.2, 0.9, 0.8]],'a tennis racket':[[0.1, 0.2, 0.5, 0.8] ]},
  'A stop sign on the right of a refrigerator':{'a stop sign':[[0.6, 0.2, 0.9, 0.8]],'a refrigerator':[[0.1, 0.2, 0.5, 0.8]]},
  'A sheep to the right of a wine glass':{'a sheep':[[0.125, 0.25, 1, 0.75]],'a wine glass':[ [0, 0.333, 0.125, 0.666]]},
  'A zebra to the right of a fire hydrant':{'a zebra':[ [0.125, 0.125, 1, 0.875]],'a fire hydrant':[[0, 0.375, 0.125, 0.625]]},
  ####### 接下来是 不太重要的一些文本
  # 反事实
  'A horse riding an astronaut.':{'a horse':[  [0.125, 0.25, 0.875, 0.875]],'an astronaut.':[ [0.25, 0.125, 0.75, 1]]},
  'A pizza cooking an oven.':{'a pizza':[[0, 0.25, 0.333, 0.75]],'an oven':[ [0.333, 0.166, 1, 0.833]]},
  'A bird scaring a scarecrow.':{'a bird':[[0.25, 0.25, 0.5, 0.5]],'a scarecrow':[[0.5, 0.125, 1, 0.875]]},
  'A blue coloured pizza.':{'a blue coloured pizza':[[0.1, 0.1, 0.9, 0.9]]},
  'Hovering cow abducting aliens.':{'a cow':[ [0.1, 0.2, 0.9, 0.8]],'aliens':[[0.2, 0.8, 0.3, 0.95],[0.4, 0.85, 0.6, 1], [0.7, 0.8, 0.8, 0.95]]},
  'A panda making latte art.':{'a panda':[[0, 0.1, 0.8, 0.9]],'latte art':[[0.6, 0.6, 0.95, 0.9]]},
  'A shark in the desert.':{'a shark':[ [0.2, 0.3, 0.8, 0.7]],'desert':[ [0, 0, 1, 1]]},
  'An elephant under the sea.':{'an elephant':[ [0.1, 0.3, 0.9, 0.8]],'sea':[[0, 0, 1, 1]]},
  'Rainbow coloured penguin.':{'Rainbow coloured penguin':[[0.2,0.2,0.8,0.8]]},
  'A fish eating a pelican.':{'a fish':[ [0.05, 0.1, 0.95, 0.9]],'a pelican':[[0.4, 0.4, 0.6, 0.6]]},
  # DALLE
  'A triangular purple flower pot. A purple flower pot in the shape of a triangle.':{'triangular purple flower pot':[[0.25, 0.25, 0.75, 0.75]]},
  'A triangular orange picture frame. An orange picture frame in the shape of a triangle.':{' triangular orange picture frame':[[0.25, 0.25, 0.75, 0.75]]},
  'A triangular pink stop sign. A pink stop sign in the shape of a triangle.':{'triangular pink stop sign':[[0.25, 0.25, 0.75, 0.75]]},
  'A cube made of denim. A cube with the texture of denim.':{'A cube made of denim.':[[0.25, 0.25, 0.75, 0.75]]},
  'A sphere made of kitchen tile. A sphere with the texture of kitchen tile.':{'A sphere made of kitchen tile':[[0.2, 0.2, 0.8, 0.8]]},
  'A cube made of brick. A cube with the texture of brick.':{'A cube made of brick':[[0.2, 0.2, 0.8, 0.8]]},
  'A collection of nail is sitting on a table.':{'A collection of nail':[[0.1, 0.7, 0.9, 0.95]],'a table':[[0, 0.7, 1, 1]]},
  'A single clock is sitting on a table.':{'a clock':[[0.35, 0.75, 0.65, 0.95]],'a table':[[0, 0.7, 1, 1]]},
  'A couple of glasses are sitting on a table.':{'a glass':[[0.35, 0.75, 0.5, 0.95],[0.5, 0.75, 0.65, 0.95]],'a table':[ [0, 0.7, 1, 1]]},
  'An illustration of a large red elephant sitting on a small blue mouse.':{'a large red elephant':[[0.1, 0.2, 0.9, 0.9]],'a small blue mouse':[[0.4, 0.85, 0.6, 0.95]]},
  'An illustration of a small green elephant standing behind a large red mouse.':{'a small green elephant':[ [0.1, 0.4, 0.9, 0.8]],'a large red mouse':[[0.15, 0.3, 0.85, 0.9]]},
  'A small blue book sitting on a large red book.':{'a small blue book':[[0.35, 0.4, 0.65, 0.5]],'a large red book':[ [0.1, 0.5, 0.9, 0.9]]},
  'A stack of 3 plates. A blue plate is on the top, sitting on a blue plate. The blue plate is in the middle, sitting on a green plate. The green plate is on the bottom.':{'a blue plate':[[0.25, 0.33, 0.75, 0.66], [0.25, 0, 0.75, 0.33]],'a green plate':[[0.25, 0.66, 0.75, 0.99]]},
  'A stack of 3 cubes. A red cube is on the top, sitting on a red cube. The red cube is in the middle, sitting on a green cube. The green cube is on the bottom.':{'a red cube':[[0.25, 0.33, 0.75, 0.66], [0.25, 0, 0.75, 0.33]],'a green cube':[[0.25, 0.66, 0.75, 0.99]]},
  'A stack of 3 books. A green book is on the top, sitting on a red book. The red book is in the middle, sitting on a blue book. The blue book is on the bottom.':{'a green book':[ [0.25, 0, 0.75, 0.33]],'a red book':[[0.25, 0.33, 0.75, 0.66]],'a blue book':[[0.25, 0.66, 0.75, 0.99]]},
  'An emoji of a baby panda wearing a red hat, green gloves, red shirt, and green pants.':{'a baby panda emoji':[[0.1, 0.1, 0.9, 0.9]],'a red hat':[[0.35, 0.1, 0.65, 0.3]],'a green gloves':[[0.15, 0.4, 0.35, 0.6]],'a red shirt':[[0.15, 0.3, 0.85, 0.5]],'a green pants':[[0.15, 0.5, 0.85, 0.7]]},
  'An emoji of a baby panda wearing a red hat, blue gloves, green shirt, and blue pants.':{'a baby panda emoji':[[0.1, 0.1, 0.9, 0.9]],'a red hat':[ [0.35, 0.1, 0.65, 0.3]],'a blue gloves':[ [0.15, 0.4, 0.35, 0.6]],'a green shirt':[[0.15, 0.3, 0.85, 0.5]],'a blue pants':[ [0.15, 0.5, 0.85, 0.7]]},
  'A fisheye lens view of a turtle sitting in a forest.':{'a turtle':[[0.35, 0.4, 0.65, 0.6]],'a forest':[ [0, 0, 1, 1]]},
  'A side view of an owl sitting in a field.':{'a side view of an owl':[[0.3, 0.5, 0.7, 0.8]],'a field':[[0, 0.8, 1, 1]]},
  'A cross-section view of a brain.':{'A cross-section view of a brain':[[0.15, 0.1, 0.85, 0.9]]},
  ## description:
  'A vehicle composed of two wheels held in a frame one behind the other, propelled by pedals and steered with handlebars attached to the front wheel.':{'a wheel':[[0.1, 0.3, 0.4, 0.7],[0.6, 0.3, 0.9, 0.7]]},
  'A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare.':{'A large motor vehicle carrying passengers by road':[[0.05, 0.2, 0.95, 0.8]],'wheel':[[0.1, 0.75, 0.2, 0.85], [0.8, 0.75, 0.9, 0.85]]},
  'A small vessel propelled on water by oars, sails, or an engine.':{'A small vessel propelled on water by oars, sails, or an engine.':[ [0.2, 0.5, 0.8, 0.8]],'Engine': [[0.75, 0.6, 0.8, 0.7]]},
  'A connection point by which firefighters can tap into a water supply.':{'Main Body': [[0.4, 0.4, 0.6, 0.8]],'Left Cap': [[0.35, 0.55, 0.4, 0.65]],'Right Cap': [0.6, 0.55, 0.65, 0.65],'Base': [[0.375, 0.8, 0.625, 0.85]]},
  'A machine next to a parking space in a street, into which the driver puts money so as to be authorized to park the vehicle for a particular length of time.':{'Parking Meter Post':[[0.05, 0.6, 0.075, 0.9]],'Parking Meter':[[0.025, 0.85, 0.1, 0.95]],'Parking Space': [[0.1, 0.65, 0.7, 0.85]]},
  'A device consisting of a circular canopy of cloth on a folding metal frame supported by a central rod, used as protection against rain or sometimes sun.':{'Canopy': [[0.2, 0.3, 0.8, 0.6]],'Central Rod': [[0.5, 0.6, 0.5, 0.9]],'Handle': [[0.475, 0.9, 0.525, 0.95]]},
  'A separate seat for one person, typically with a back and four legs.':{'Seat': [[0.25, 0.4, 0.75, 0.5]],'Back': [[0.25, 0.2, 0.75, 0.4]],'Leg': [[0.275, 0.5, 0.275, 0.9],[0.225, 0.5, 0.225, 0.9],[0.725, 0.5, 0.725, 0.9],[0.775, 0.5, 0.775, 0.9]]},
  'An appliance or compartment which is artificially kept cool and used to store food and drink.':{'Main Body': [[0.2, 0.3, 0.8, 0.9]],'Freezer': [[0.2, 0.15, 0.8, 0.3]],'Handle for Main Body': [[0.775, 0.55, 0.775, 0.7]],'Handle for Freezer': [[0.775, 0.2, 0.775, 0.275]]},
  'A mechanical or electrical device for measuring time.':{'A mechanical or electrical device for measuring time.':[[0.2,0.2,0.8,0.8]]},
  # 'An instrument used for cutting cloth, paper, and other thin material, consisting of two blades laid one on top of the other and fastened in the middle so as to allow them to be opened and closed by a thumb and finger inserted through rings on the end of their handles.'
  # gpt4 将下面的一些内容都划分为更细致的布局，目前效果待定(整个description)
  'A large plant-eating domesticated mammal with solid hoofs and a flowing mane and tail, used for riding, racing, and to carry and pull loads.':{'A large plant-eating domesticated mammal':[[0.1, 0.2, 0.9, 0.8]],'solid hoofs':[[0.2,0.7,0.8,0.85]],'flowing mane':[[0.2, 0.25, 0.4, 0.3]],'tail':[[0.5, 0.65, 0.55, 0.8]]},
  'A long curved fruit which grows in clusters and has soft pulpy flesh and yellow skin when ripe.':{'A long curved fruit which grows in clusters and has soft pulpy flesh and yellow skin when ripe.':[[0.3, 0.3, 0.7, 0.7]]},
  'A small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws. It is widely kept as a pet or for catching mice, and many breeds have been developed.':{'A small domesticated carnivorous mammal':[ [0.2, 0.2, 0.8, 0.8]],'soft fur':[[0.3,0.3,0.8,0.7]],'a short snout':[[0.2,0.2,0.35,0.45]],'retractable claws':[[0.2,0.7,0.8,0.8]]},
  'A domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, nonretractable claws, and a barking, howling, or whining voice.':{'A domesticated carnivorous mammal':[[0.2,0.2,0.8,0.8]],'a long snout':[[0.15,0.3,0.4,0.5]],'nonretractable claws':[[0.2,0.6,0.8,0.8]]},
  'An organ of soft nervous tissue contained in the skull of vertebrates, functioning as the coordinating center of sensation and intellectual and nervous activity.':{'An organ of soft nervous tissue contained in the skull of vertebrates':[[0.2, 0.3, 0.8, 0.7]]},
  'An American multinational technology company that focuses on artificial intelligence, search engine, online advertising, cloud computing, computer software, quantum computing, e-commerce, and consumer electronics.':{'An American multinational technology company':[[0.0,0.0,1.0,0.9]]},
  'A large keyboard musical instrument with a wooden case enclosing a soundboard and metal strings, which are struck by hammers when the keys are depressed. The strings\' vibration is stopped by dampers when the keys are released and can be regulated for length and volume by two or three pedals.':{'Piano': [[0.1, 0.3, 0.9, 0.8]],'Pedals': [[0.4, 0.7, 0.6, 0.9]]},
  # 'A type of digital currency in which a record of transactions is maintained and new units of currency are generated by the computational solution of mathematical problems, and which operates independently of a central bank.'
  'A large thick-skinned semiaquatic African mammal, with massive jaws and large tusks.':{'Hippopotamus':[[0.2, 0.3, 0.8, 0.6]]},
  'A machine resembling a human being and able to replicate certain human movements and functions automatically.':{'Humanoid Robot': [[0.1, 0.1, 0.9, 0.9]]},
  # gray marcus et al.
  'Paying for a quarter-sized pizza with a pizza-sized quarter.':{'quarter-sized pizza':[ [0, 0, 0.5, 0.5]],'pizza-sized quarter':[ [0.5, 0.5, 1, 1]]},
  'An oil painting of a couple in formal evening wear going home get caught in a heavy downpour with no umbrellas.':{'An oil painting':[[0, 0, 1, 1] ],'a couple in formal evening wear':[[0.2, 0.6, 0.8, 1]],'a heavy downpour':[[0, 0, 1, 1] ]},
  # 下面这一句需要调整
  # 'A grocery store refrigerator has pint cartons of milk on the top shelf, quart cartons on the middle shelf, and gallon plastic jugs on the bottom shelf.':{'A grocery store refrigerator':[[0.1,0.1,0.9,0.9]],'pint cartons of milk':[[0.2,0.105,0.8,0.35]],' quart cartons of milk':[[0.2,0.355,0.8,0.65]],'gallon plastic jugs':[[0.2,0.655,0.7,0.9]]},
  'In late afternoon in January in New England, a man stands in the shadow of a maple tree.':{'New England':[[0.0,0.0,1.0,1.0]],'a man':[ [0.4, 0.75, 0.5, 0.95]],'a maple tree':[[0.15, 0.4, 0.25, 1]],'the shadow':[[0.25, 0.7, 0.8, 1]]},
  'An elephant is behind a tree. You can see the trunk on one side and the back legs on the other.':{'an elephant':[[0.3, 0.5, 0.8, 1.0]],'a tree':[ [0.4, 0.2, 0.6, 1]],'elephant back leg':[[0.6, 0.6, 0.7, 1],[0.7, 0.6, 0.8, 1]],'the elephant trunk':[[0.3, 0.5, 0.4, 0.7]]},
  'A tomato has been put on top of a pumpkin on a kitchen stool. There is a fork sticking into the pumpkin. The scene is viewed from above.':{'a tomato':[ [0.45, 0.45, 0.55, 0.55]],'a pumpkin':[ [0.35, 0.35, 0.65, 0.65]],'kitchen stool':[[0.3, 0.3, 0.7, 0.7]],'a fork':[[0.25, 0.5, 0.35, 0.52]]},
  # 下面这一句也需要考虑
  # 'A pear cut into seven pieces arranged in a ring.':{'A pear cut into seven pieces arranged in a ring.':[[0.2,0.2,0.8,0.8]]},
  'A donkey and an octopus are playing a game. The donkey is holding a rope on one end, the octopus is holding onto the other. The donkey holds the rope in its mouth. A cat is jumping over the rope.':{'A donkey':[[0, 0.4, 0.25, 0.8]],'an octopus':[ [0.75, 0.4, 1, 0.8]],'a rope':[ [0.25, 0.65, 0.75, 0.7]],'a cat':[[0.45, 0.4, 0.55, 0.6]]},
  # 'Supreme Court Justices play a baseball game with the FBI. The FBI is at bat, the justices are on the field.'
  'Abraham Lincoln touches his toes while George Washington does chin-ups. Lincoln is barefoot. Washington is wearing boots.':{'Abraham Lincoln':[[0.2,0.3,0.5,0.8]],'Washington':[[0.6,0.4,0.975,0.7]]},
  # reddit
  'A church with stained glass windows depicting a hamburger and french fries.':{'a church':[[0, 0, 1, 1]],'Hamburger Window': [[0.2, 0.3, 0.5, 0.7]],'French Fries Window': [[0.5, 0.3, 0.8, 0.7] ]},
  'Painting of the orange cat Otto von Garfield, Count of Bismarck-Schönhausen, Duke of Lauenburg, Minister-President of Prussia. Depicted wearing a Prussian Pickelhaube and eating his favorite meal - lasagna.':{'Painting': [[0, 0, 1, 1]],'Otto von Garfield': [[0.1, 0.2, 0.8, 0.9]],'Prussian Pickelhaube': [[0.3, 0.2, 0.6, 0.4]],'Lasagna': [[0.4, 0.7, 0.7, 0.85]] },
  'A baby fennec sneezing onto a strawberry, detailed, macro, studio light, droplets, backlit ears.':{'a baby fennec':[[0.1, 0.1, 0.8, 0.9]],'a strawberry':[[0.65, 0.5, 0.85, 0.7]],'Droplets Area': [[0.5, 0.4, 0.85, 0.7]]},
  'A photo of a confused grizzly bear in calculus class.':{'calculus class':[[0.0,0.0,1.0,1.0]],'a confused grizzly bear':[[0.15, 0.3, 0.85, 0.9]]},
  # 下面一句 扩展成为了 丰富的描述
  # 'An ancient Egyptian painting depicting an argument over whose turn it is to take out the trash.'
  'A fluffy baby sloth with a knitted hat trying to figure out a laptop, close up, highly detailed, studio lighting, screen reflecting in its eyes.':{'A fluffy baby':[[0.1, 0.1, 0.9, 0.9]],'a knitted hat':[[0.4,0.0,0.5,0.35]],'a laptop':[[0.2,0.65,0.8,1.]]},
  'A tiger in a lab coat with a 1980s Miami vibe, turning a well oiled science content machine, digital art.':{'Tiger in a Lab Coat': [[0.2, 0.3, 0.8, 0.9]],'1980s Miami Vibe Background':[[0.0,0.0,1.0,1.0]],'Well-Oiled Science Content Machine':[[0.6, 0.5, 0.95, 0.8]]},
  'A 1960s yearbook photo with animals dressed as humans.':{'A 1960s yearbook photo':[[0.0,0.0,1.0,1.0]],'a fox in a dress': [[0.05, 0.1, 0.45, 0.5]],'a bear in a suit': [[0.55, 0.1, 0.95, 0.5]],' an owl with a shirt': [[0.05, 0.6, 0.45, 0.95]]},
  'Lego Arnold Schwarzenegger.':{'Lego Arnold Schwarzenegger':[[0.2, 0.2, 0.8, 0.8]]},
  'A yellow and black bus cruising through the rainforest.':{'A yellow and black bus':[ [0.2, 0.4, 0.6, 0.7]],'the rainforset':[[0.0,0.0,1,1.]]},
  # 'A medieval painting of the wifi not working.'
  'An IT-guy trying to fix hardware of a PC tower is being tangled by the PC cables like Laokoon. Marble, copy after Hellenistic original from ca. 200 BC. Found in the Baths of Trajan, 1506.':{'Base': [[0, 0.7, 1, 1]],'IT-Guy':[[0.3, 0.2, 0.7, 0.9]],'PC Tower': [[0.7, 0.5, 0.9, 0.9]],'Cables': [[0.3, 0.2, 0.9, 0.9]]},
  '35mm macro shot a kitten licking a baby duck, studio lighting.':{'a kitten':[[0.1, 0.2, 0.7, 0.8]],'a baby duck':[ [0.55, 0.4, 0.85, 0.7]]},
  'McDonalds Church.':{'McDonalds Church':[[0.2,0.2,0.8,0.8]]},
  'Photo of an athlete cat explaining it\'s latest scandal at a press conference to journalists.':{'Athlete Cat':[ [0.35, 0.3, 0.65, 0.7]],'Podium': [[0.4, 0.4, 0.6, 0.6]],'Microphones': [[0.45, 0.35, 0.55, 0.45]],'Group of Journalists': [[0.1, 0.65, 0.9, 0.95]]},
  'Greek statue of a man tripping over a cat.':{'Greek statue':[[0.0,0.0,1.0,1.0]],'a man':[ [0.2, 0.2, 0.8, 0.8] ],'a cat':[[0.6, 0.65, 0.75, 0.8]]},
  'An old photograph of a 1920s airship shaped like a pig, floating over a wheat field.':{'An old photograph of a 1920s':[[0.0,0.0,1.0,1.0]],'airship shaped like a pig':[ [0.2, 0.15, 0.8, 0.6]],'a wheat field':[ [0, 0.65, 1, 1]]},
  # 这一句话 gpt4理解  出了问题
  # 'Photo of a cat singing in a barbershop quartet.'
  # 详细的分词，需要进一步调整
  # Background:

  # Gothic House & Distant Sky/Space Landscape: [0, 0.1, 1, 0.7]
  # Astronaut Couple:

  # Positioned similarly to the original painting, they're the central focus:
  # Astronaut 1 (on the left): [0.3, 0.25, 0.55, 0.95]
  # Astronaut 2 (on the right): [0.45, 0.25, 0.7, 0.95]
  # Foreground:

  # Alien Terrain or Ground: [0, 0.85, 1, 1]

  # 'A painting by Grant Wood of an astronaut couple, american gothic style.'
  'An oil painting portrait of the regal Burger King posing with a Whopper.':{'Burger King': [[0.2, 0.1, 0.8, 0.9]],'Whopper': [[0.6, 0.4, 0.75, 0.6]]},
  'A keyboard made of water, the water is made of light, the light is turned off.':{'Water-formed Keyboard': [[0.15, 0.4, 0.85, 0.6]]},
  # 'Painting of Mona Lisa but the view is from behind of Mona Lisa.'
  'Hyper-realistic photo of an abandoned industrial site during a storm.':{'an abandoned industrial site':[ [0.05, 0.2, 0.95, 0.8]],'a stormy sky':[ [0, 0, 1, 0.5]]},
  # 'A screenshot of an iOS app for ordering different types of milk.'
  # 'A real life photography of super mario, 8k Ultra HD.'
  'Colouring page of large cats climbing the eifel tower in a cyberpunk future.':{'large cats':[ [0.35, 0.6, 0.65, 0.8]],'the eifel tower':[[0.1, 0.1, 0.9, 1]],'cyberpunk future':[[0.0,0.0,1.0,1.0]]},
# 细分的场景描述
# Kid's Bedroom:

# Bed & Dresser: Positioned on the left side: [0, 0.5, 0.3, 1]
# Window: On the right wall, giving a view outside: [0.7, 0.4, 0.9, 0.6]
# Mega Lego Space Station:

# Main Structure: Center and expansive, dominating the room: [0.2, 0.1, 0.8, 0.9]
# Supporting Elements:

# Astronauts & Vehicles: Scattered around the main structure but mainly at its base: [0.15, 0.05, 0.85, 0.2]
# Kid:

# Child: Positioned on the right, interacting with the Lego station: [0.7, 0.6, 0.95, 0.9]
# 'Photo of a mega Lego space station inside a kid\'s bedroom.''

  'A spider with a moustache bidding an equally gentlemanly grasshopper a good day during his walk to work.':{'a spider':[[0.2, 0.6, 0.5, 0.9]],'a spider\'s moustache':[ [0.32, 0.77, 0.38, 0.82]],'an equally gentlemanly grasshopper':[ [0.55, 0.7, 0.85, 0.9]],'pathway':[[0, 0.7, 1, 0.9]]},
  'A photocopy of a photograph of a painting of a sculpture of a giraffe.':{'Photocopy': [[0, 0, 1, 1]],'Photograph': [[0.05, 0.05, 0.95, 0.95]],'Painting': [[0.1, 0.1, 0.9, 0.9]],'a sculpture of a giraffe': [[0.2, 0.2, 0.8, 0.8]]},
# 'A bridge connecting Europe and North America on the Atlantic Ocean, bird\'s eye view.''
  'A maglev train going vertically downward in high speed, New York Times photojournalism.':{'Maglev Train': [[0.4, 0.1, 0.6, 0.7]],'Motion Streaks/Blur': [[0.38, 0, 0.62, 0.5]]},
  'A magnifying glass over a page of a 1950s batman comic.':{'A magnifying glass':[[0.3, 0.3, 0.7, 0.7]],'a page of a 1950s batman comic':[[0, 0, 1, 1]]},
  'A car playing soccer, digital art.':{'Soccer Field': [[0, 0, 1, 1]],'a car':[[0.3, 0.45, 0.7, 0.75]],'soccer':[[0.7, 0.5, 0.75, 0.55]]},
  'Darth Vader playing with raccoon in Mars during sunset.':{'Darth Vader ':[[0.35, 0.4, 0.65, 0.8]],'a raccoon':[ [0.65, 0.6, 0.75, 0.75]],'Mars Landscape': [[0, 0.3, 1, 1]],'sunset':[[0, 0, 1, 0.5]]},
  # 'A 1960s poster warning against climate change.'
  'Illustration of a mouse using a mushroom as an umbrella.':{'a mouse':[ [0.45, 0.5, 0.55, 0.8]],'a mushroom umbrella':[[0.4, 0.2, 0.6, 0.6]],'Rain': [[0, 0, 1, 1]]},
  # 'A realistic photo of a Pomeranian dressed up like a 1980s professional wrestler with neon green and neon orange face paint and bright green wrestling tights with bright orange boots.'
  'A pyramid made of falafel with a partial solar eclipse in the background.':{'A pyramid made of falafel':[[0.2, 0.5, 0.8, 0.95]],'a partial solar eclipse':[[0.35, 0.1, 0.65, 0.4]]},
  # text
  'A storefront with \'Hello World\' written on it.':{'a storefront':[[0.1, 0.1, 0.9, 0.9]],'words \'Hello World\'':[[0.2, 0.15, 0.8, 0.25]]},
  'A storefront with \'Diffusion\' written on it.':{'a storefront':[[0.1, 0.1, 0.9, 0.9]],'words \'Diffusion\'':[[0.2, 0.2, 0.8, 0.3]]},
  'A storefront with \'Text to Image\' written on it.':{'a storefront':[[0.1, 0.1, 0.9, 0.9]],'words \'Text to Image\'':[[0.15, 0.2, 0.85, 0.3]]},
  'A storefront with \'NeurIPS\' written on it.':{'a storefront':[[0.1, 0.1, 0.9, 0.9]],'words \'NeurIPS\'':[[0.15, 0.2, 0.85, 0.3]]},
  'A storefront with \'Deep Learning\' written on it.':{'a storefront':[[0.1, 0.1, 0.9, 0.9]],'words \'Deep Learning\'':[[0.15, 0.2, 0.85, 0.3]]},
  'A storefront with \'Google Brain Toronto\' written on it.':{'a storefront':[[0.1, 0.1, 0.9, 0.9]],'words \'Google Brain Toronto\'':[[0.15, 0.2, 0.85, 0.3]]},
  'A storefront with \'Google Research Pizza Cafe\' written on it.':{'a storefront':[[0.1, 0.1, 0.9, 0.9]],'words \'Google Research Pizza Cafe\'':[[0.15, 0.2, 0.85, 0.3]]},
  'A sign that says \'Hello World\'.':{'Sign': [[0.2, 0.4, 0.8, 0.6]],'\'Hello World\' Text': [[0.25, 0.45, 0.75, 0.55]]},
  'A sign that says \'Diffusion\'.':{'Sign': [[0.2, 0.4, 0.8, 0.6]],'\'Diffusion\' Text': [[0.25, 0.45, 0.75, 0.55]]},
  'A sign that says \'Text to Image\'.':{'Sign': [[0.2, 0.4, 0.8, 0.6]],'\'Text to Image\' Text': [[0.25, 0.45, 0.75, 0.55]]},
  'A sign that says \'NeurIPS\'.':{'Sign': [[0.2, 0.4, 0.8, 0.6]],'\'NeurIPS\' Text': [[0.25, 0.45, 0.75, 0.55]]},
  'A sign that says \'Deep Learning\'.':{'Sign': [[0.2, 0.4, 0.8, 0.6]],'\'Deep Learning\' Text': [[0.25, 0.45, 0.75, 0.55]]},
  'A sign that says \'Google Brain Toronto\'.':{'Sign': [[0.2, 0.4, 0.8, 0.6]],'\'Google Brain Toronto\' Text': [[0.25, 0.45, 0.75, 0.55]]},
  'A sign that says \'Google Research Pizza Cafe\'.':{'Sign': [[0.2, 0.4, 0.8, 0.6]],'\'Google Research Pizza Cafe\' Text': [[0.25, 0.45, 0.75, 0.55]]},
  'New York Skyline with \'Hello World\' written with fireworks on the sky.':{'New York Skyline':[[0, 0.6, 1, 1]],'Fireworks with \'Hello World\'':[[0.1, 0.1, 0.9, 0.5]]},
  'New York Skyline with \'Diffusion\' written with fireworks on the sky.':{'New York Skyline':[[0, 0.6, 1, 1]],'Fireworks with \'Diffusion\'':[[0.1, 0.1, 0.9, 0.5]]},
  'New York Skyline with \'Text to Image\' written with fireworks on the sky.':{'New York Skyline':[[0, 0.6, 1, 1]],'Fireworks with \'Text to Image\'':[[0.1, 0.1, 0.9, 0.5]]},
  'New York Skyline with \'NeurIPS\' written with fireworks on the sky.':{'New York Skyline':[[0, 0.6, 1, 1]],'Fireworks with \'NeurIPS\'':[[0.1, 0.1, 0.9, 0.5]]},
  'New York Skyline with \'Deep Learning\' written with fireworks on the sky.':{'New York Skyline':[[0, 0.6, 1, 1]],'Fireworks with \'Deep Learning\'':[[0.1, 0.1, 0.9, 0.5]]},
  'New York Skyline with \'Google Brain Toronto\' written with fireworks on the sky.':{'New York Skyline':[[0, 0.6, 1, 1]],'Fireworks with \'Google Brain Toronto\'':[[0.1, 0.1, 0.9, 0.5]]},
  'New York Skyline with \'Google Research Pizza Cafe\' written with fireworks on the sky.':{'New York Skyline':[[0, 0.6, 1, 1]],'Fireworks with \'Google Research Pizza Cafe\'':[[0.1, 0.1, 0.9, 0.5]]},
}

yaml_dir = 'annotations_gpt4_full.yaml'
with open(yaml_dir, 'w', encoding='utf-8', ) as f:
    yaml.dump(dicts, f, encoding='utf-8', allow_unicode=True)