## 按钮变换
transform menu_button_move1(): #天希移动
    xcenter 0
    ycenter 0
    offset(320,560)
    linear 0.35 xoffset 650 yoffset 560 xcenter 0 ycenter 0

transform menu_button_move2(): #梦璃移动
    xcenter 0
    ycenter 0
    offset(610,560)
    linear 0.15 xoffset 650 yoffset 560 xcenter 0 ycenter 0

transform menu_button_move3(): #特典移动
    xcenter 0
    ycenter 0
    offset(1045,555)
    linear 0.35 xoffset 650 yoffset 560 xcenter 0 ycenter 0

transform menu_button_see(): #主界面按钮浅出
    alpha 0.2
    easeout 0.8 alpha 1

transform button_show1(): #主界面按钮调节
    zoom 0.25

transform button_show2(): #主界面按钮调节2
    zoom 0.18

## 画面变换
# 上=>下淡入
transform fade_in_down():
    xanchor 0
    yanchor 0
    offset(0,-100)
    linear 2 offset(0,0)

# 左=>右淡入
transform fade_in_right():
    xanchor 0
    yanchor 0
    offset(-50,0)
    linear 2 offset(0,0)

# 右=>左淡入
transform fade_in_left():
    xanchor 0
    yanchor 0
    offset(50,0)
    linear 2 offset(0,0)

# 下=>上淡入
transform fade_in_up():
    xanchor 0
    yanchor 0
    offset(0,100)
    linear 2 offset(0,0)

#背景左右晃动2次
transform bg_move_2():
    linear 0.05 offset(-10,0)
    linear 0.07 offset(20,0)
    linear 0.07 offset(-20,0)
    linear 0.07 offset(20,0)
    linear 0.07 offset(-20,0)
    linear 0.05 offset(0,0)

## 杂项
# 半透明显示
transform half_alpha:
    alpha 0.5

transform alpha3:
    alpha 0.3

## l2d形象显示
# 人物居中显示
transform nat_show:
    zoom 1.2
    xalign 0.55
    yoffset -170

transform may_show:
    xalign 0.55

transform kot_show:
    xalign 0.8
    yalign 0.2

transform kak_show:
    xalign 0.8
    yalign 0.2

transform muk_show:
    zoom 1.5
    xalign 0.55

transform rio_show:
    yalign 0
    yoffset 20
    xalign 0.55
    yoffset 120

transform shd_show:
    xalign 0.35

transform yuz_show:
    xalign 0.55

transform tix_show:
    xalign 0.35

transform mar_show:
    xalign 0.55
    yoffset -30

transform ori_show:
    zoom 2
    xalign 1.2
    yalign 0.5

#人物左侧显示
transform rio_show_left:
    xalign 0.00
    yalign 0
    xoffset -120
    yoffset 20

transform kot_show_left:
    xalign 0.00
    yalign 0
    xoffset -50
    yoffset 45

transform shd_show_left:
    xalign 0.00
    xoffset -50

# 人物右侧显示
transform mar_show_right:
    xalign 0.55
    yoffset -95
    xoffset 350

transform kot_show_right:
    xalign 0.00
    yoffset 80
    xoffset 350

transform shd_show_right:
    xalign 0.00
    yalign 0
    yoffset -60
    xoffset 300
