#各种变量的定义

##特效
define disv_fast=Dissolve(0.2) #快速溶解特效
define disv_superfast=Dissolve(0.05) #超快溶解特效
define disv_slow=Dissolve(1.0) #慢速溶解特效
define disv_slow2=Dissolve(1.5) #慢速溶解特效2
define fadewh=Fade(0.5,0.3,0.2,color="#fff") #白色fade转场
define pixel_1=Pixellate(0.5,2) #像素溶解转场

define gongyu=0 #地图1 选项变量
define chezhan=0
# define wuhe=0

define tiangong=0 #地图2 选项变量
define shangye=0
define bianli=0

define a=0
define b=0
define c=0
define d=0
define e=0
define f=0


#l2d定义
image nat = Live2D("l2ds/七罪/5七罪.model3.json", base=.75, loop=True,seamless=True)
image may = Live2D("l2ds/万由里/2万由里.model3.json", base=.75, loop=True,seamless=True)
image kot = Live2D("l2ds/五河/五河.model3.json",base=.73,loop=True,seamless=True,update_function=kot_mouth_close)
image kak = Live2D("l2ds/八舞/3八舞耶.model3.json", base=.75, loop=True,seamless=True)
image muk = Live2D("l2ds/六喰/六喰立绘.model3.json", base=.75, loop=True,seamless=True)
image rio = Live2D("l2ds/园神/4园神凛绪.model3.json", base=.75,loop=True,seamless=True,update_function=rio_z)
image shd = Live2D("l2ds/士道/士道.model3.json", base=.7, loop=True,seamless=True)
image yuz = Live2D("l2ds/夕弦/6八舞夕弦.model3.json", base=.75, loop=True,seamless=True)
image tix = Live2D("l2ds/天希/男主.model3.json", base=.75, loop=True,seamless=True)
image mar = Live2D("l2ds/或守/7或守鞠亚.model3.json", base=.62, loop=True,seamless=True)
image ori = Live2D("l2ds/折纸/折纸.model3.json", base=.75, loop=True,seamless=True)
