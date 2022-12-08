screen tianxi_menu(): #天希菜单
    add gui.main_menu_background:
        zoom 1.58

    frame:
        style "main_menu_frame"

    hbox:
        add "gui/button/tianxi.png" at menu_button_move1()

    hbox:
        xcenter 0
        ycenter 0
        offset(120,640)
        spacing 1
        # imagebutton idle "gui/button/new_game.png" offset(440,10):
        #     activate_sound "sound/button_1.ogg"
        #     action [Stop("music"),Start(label="tianxi_main")]
        add "gui/button/new_game.png" offset(440,10) alpha 0.5 #TODO 天希主线待做
        imagebutton idle "gui/button/load_save.png" offset(520,5):
            activate_sound "sound/button_1.ogg"
            action [Hide("mengl_menu",transition=dissolve),ShowMenu("load")]
        imagebutton idle "gui/button/back_m.png" offset(590,5):
            activate_sound "sound/button_1.ogg"
            action [Hide("tianxi_menu",transition=dissolve),ShowMenu("main_menu")]
            # action ShowMenu("main_menu")

screen mengl_menu(): #梦璃菜单
    add gui.main_menu_background:
        zoom 1.58

    frame:
        style "main_menu_frame"

    hbox:
        add "gui/button/mengli.png" at menu_button_move2()

    hbox:
        xcenter 0
        ycenter 0
        offset(120,640)
        spacing 1
        # imagebutton idle "gui/button/new_game.png" offset(440,10)
        add "gui/button/new_game.png" offset(440,10) alpha 0.5 #TODO 梦璃待做
        imagebutton idle "gui/button/load_save.png" offset(520,5):
            activate_sound "sound/button_1.ogg"
            action [Hide("mengl_menu",transition=dissolve),ShowMenu("load")]
        imagebutton idle "gui/button/back_m.png" offset(590,5):
            activate_sound "sound/button_1.ogg"
            action [Hide("mengl_menu",transition=dissolve),ShowMenu("main_menu")]

screen tedian_menu(): #特典剧场
    add gui.main_menu_background:
        zoom 1.58

    frame:
        style "main_menu_frame"

    hbox:
        add "gui/button/tedian.png" at menu_button_move3()

    hbox:
        xcenter 0
        ycenter 0
        offset(120,640)
        spacing 1
        imagebutton idle "gui/button/new_game.png" offset(440,10):
            activate_sound "sound/button_1.ogg"
            # action [Stop("music"),Start(label="juchang_1_1")]
            action [Hide("tedian_menu",transition=dissolve),ShowMenu("tedian_menu_1")]
        # add "gui/button/new_game.png" offset(440,10) alpha 0.5
        imagebutton idle "gui/button/load_save.png" offset(520,5):
            activate_sound "sound/button_1.ogg"
            action [Hide("mengl_menu",transition=dissolve),ShowMenu("load")]
        imagebutton idle "gui/button/back_m.png" offset(590,5):
            activate_sound "sound/button_1.ogg"
            action [Hide("tedian_menu",transition=dissolve),ShowMenu("main_menu")]

screen tedian_menu_1(): #特典剧场选择
    add "gui/tedian_back.png":
        zoom 0.68

    frame:
        style "main_menu_frame"

    add "gui/button/tedian.png":
        zoom 1.0
        xcenter 0
        ycenter 0
        offset(100,30)
    
    add "images/characters/shido.png":
        zoom 0.8
        xcenter 0
        ycenter 0
        offset(160,400)

    add "gui/choice_back.jpg":
        zoom 0.25
        xcenter 0
        ycenter 0
        offset(800,400)

    add "gui/guangboju.png":
        zoom 0.37
        xcenter 0
        ycenter 0
        offset(800,75)

    # frame:
        # zoom 0.55 
    # imagebutton idle "gui/arrow_next.png" xcenter 0 ycenter 0 offset(1060,74):
    #     activate_sound "sound/button_1.ogg"
    #     action [Hide("tedian_menu_1",transition=fade),ShowMenu("tedian_menu_2")]
    add "gui/arrow_next.png" xcenter 0 ycenter 0 offset(1060,74) alpha 0.5 #TODO 剧场版剩余待做

    imagebutton idle "gui/button/back_m.png" offset(1120,30):
        activate_sound "sound/button_1.ogg"
        action [Hide("tedian_menu_1",transition=dissolve),ShowMenu("main_menu")]

    # imagebutton idle "gui/mayuri.png" offset(630,180) at button_show1:
    #     activate_sound "sound/button_1.ogg"
    #     action [Stop("music"),Start(label="juchang_1_1")]
    add "gui/mayuri.png" offset(630,180) at button_show1 alpha 0.5 #TODO 万由里约会

    # imagebutton idle "gui/ouxiang.png" offset(670,270) at button_show2:
    #     activate_sound "sound/button_1.ogg"
    #     action [Stop("music"),Start(label="juchang_1_2")]
    add "gui/ouxiang.png" offset(670,270) at button_show2 alpha 0.5 #TODO 万由里约会

    textbutton "特别篇" text_font "Gunshihei.ttf" text_size 52 text_color "#fff" text_outlines [(absolute(1),"#0909ff",absolute(0),absolute(0))] offset(720,355):
        activate_sound "sound/button_1.ogg"
        action [Stop("music"),Start(label="te_bie_pian")]

screen tedian_menu_2():
    add "gui/tedian_back.png":
        zoom 0.68

    add "gui/button/tedian.png":
        zoom 1.0
        xcenter 0
        ycenter 0
        offset(100,30)

    add "gui/choice_back.jpg":
        zoom 0.25
        xcenter 0
        ycenter 0
        offset(800,400)

    frame:
        style "main_menu_frame"

    add "images/characters/tianxi_1.png":
        zoom 0.28
        xcenter 0
        ycenter 0
        offset(205,450)

    add "gui/yuanchuangju.png":
        zoom 0.33
        xcenter 0
        ycenter 0
        offset(780,75)

    add "gui/qidai.png":
        zoom 0.3
        xcenter 0
        ycenter 0
        offset(810,375)

    # imagebutton idle "gui/arrow_next.png" xcenter 0 ycenter 0 offset(1060,71) xsize 60 ysize 60:
    #     activate_sound "sound/button_1.ogg"
    #     action [Hide("tedian_menu_1",transition=fade),ShowMenu("tedian_menu_2")]

    imagebutton idle "gui/button/back_m.png" offset(1120,30):
        activate_sound "sound/button_1.ogg"
        action [Hide("tedian_menu_1",transition=dissolve),ShowMenu("main_menu")]

    imagebutton idle "gui/arrow_back.png" xcenter 0 ycenter 0 offset(495,75):
        activate_sound "sound/button_1.ogg"
        action [Hide("tedian_menu_2",transition=fade),ShowMenu("tedian_menu_1")]

    imagebutton idle "gui/arrow_next.png" xcenter 0 ycenter 0 offset(1060,74):
        activate_sound "sound/button_1.ogg"
        action [Hide("tedian_menu_2",transition=fade),ShowMenu("tedian_menu_3")]

screen tedian_menu_3():
    add "gui/tedian_back.png":
        zoom 0.68

    add "gui/button/tedian.png":
        zoom 1.0
        xcenter 0
        ycenter 0
        offset(100,30)

    add "gui/choice_back.jpg":
        zoom 0.25
        xcenter 0
        ycenter 0
        offset(800,400)

    frame:
        style "main_menu_frame"

    add "gui/mengli.png":
        zoom 0.33
        xcenter 0
        ycenter 0
        offset(780,75)   

    add "images/characters/mengli.png":
        zoom 0.6
        xcenter 0
        ycenter 0
        offset(205,450)

    add "gui/qidai.png":
        zoom 0.3
        xcenter 0
        ycenter 0
        offset(810,375)

    imagebutton idle "gui/button/back_m.png" offset(1120,30):
        activate_sound "sound/button_1.ogg"
        action [Hide("tedian_menu_1",transition=dissolve),ShowMenu("main_menu")]
    
    imagebutton idle "gui/arrow_back.png" xcenter 0 ycenter 0 offset(495,75):
        activate_sound "sound/button_1.ogg"
        action [Hide("tedian_menu_3",transition=fade),ShowMenu("tedian_menu_2")]

# screen choice_1(gongyu=0,chezhan=0): #地图选项1
#     add "gui/school_gate.png":
#         # offset (0,0)
#         zoom 0.78

#     showif gongyu==0:
#         add "gui/sidebar/Task1.jpg":
#             xcenter 0
#             ycenter 0
#             zoom 0.8
#             offset(120,240)
#     else:
#         add "gui/sidebar/Task2.jpg":
#             xcenter 0
#             ycenter 0
#             zoom 0.22
#             offset(120,240)

#     showif gongyu == 0:
#         vbox:
#             xcenter 0
#             ycenter 0
#             offset(0,0)
#             add "images/chara/tohka/tohka_nor.png":
#                 zoom 0.5
#                 offset(1050,440)
#             textbutton "精灵公寓" offset(1140,440) text_size 35 text_color "#000" text_outlines [(absolute(1), "#ff0", absolute(0), absolute(0))]:
#                 style "text_button"
#                 #activate_sound "sound/choice_button.ogg"
#                 text_hover_color "#fff"
#                 action [Hide("choice_1",transition=dissolve),Call("tianxi_3")]
#     # showif wuhe == 0:
#     vbox:
#         xcenter 0
#         ycenter 0
#         offset(0,0)
#         add "images/chara/yoshino/四糸乃-1无帽正常.png":
#             zoom 0.5
#             offset(340,200)
#         textbutton "五河家" offset(430,200) text_size 35 text_color "#000" text_outlines [(absolute(1), "#ff0", absolute(0), absolute(0))]:
#             style "text_button"
#             #activate_sound "sound/choice_button.ogg"
#             text_hover_color "#fff"
#             action [Hide("choice_1",transition=dissolve),Call("tianxi_4")]
#     showif chezhan == 0:
#         vbox:
#             xcenter 0
#             ycenter 0
#             offset(0,0)
#             add "images/chara/others/hongren.png":
#                 zoom 0.7
#                 offset(650,502)
#             textbutton "车站" offset(700,320) text_size 35 text_color "#000" text_outlines [(absolute(1), "#ff0", absolute(0), absolute(0))]:
#                 style "text_button"
#                 #activate_sound "sound/choice_button.ogg"
#                 text_hover_color "#fff"
#                 action [Hide("choice_1",transition=dissolve),Call("tianxi_2")]
                
# screen choice_2(tiangong=0,shangye=0,bianli=0): #地图选项2
#     add "gui/school_gate.png":
#         # offset (0,0)
#         zoom 0.78

#     showif tiangong==0:
#         add "gui/sidebar/Task3.jpg":
#             xcenter 0
#             ycenter 0
#             zoom 0.22
#             offset(120,240)
#     # else:
#     #     add "gui/sidebar/Task2.jpg":
#     #         xcenter 0
#     #         ycenter 0
#     #         zoom 0.22
#     #         offset(120,240)

#     showif tiangong == 0:
#         hbox:
#             xcenter 0
#             ycenter 0
#             offset(0,0)
#             add "images/chara/nazimi/nazimi_1.png":
#                 zoom 0.37
#                 offset(1140,390)
#             add "images/chara/yoshino/四糸乃-1无帽正常.png":
#                 zoom 0.50
#                 offset(910,370)
#         vbox:
#             xcenter 0
#             ycenter 0
#             offset(0,0)
#             textbutton "天宫塔" offset(1040,540) text_size 35 text_color "#000" text_outlines [(absolute(1), "#ff0", absolute(0), absolute(0))]:
#                 style "text_button"
#                 #activate_sound "sound/choice_button.ogg"
#                 text_hover_color "#fff"
#                 # action NullAction
#                 action [Hide("choice_1",transition=dissolve),Call("tianxi_9")]
#     showif shangye == 0:
#         vbox:
#             xcenter 0
#             ycenter 0
#             offset(0,0)
#             textbutton "商业街" offset(430,200) text_size 35 text_color "#000" text_outlines [(absolute(1), "#ff0", absolute(0), absolute(0))]:
#                 style "text_button"
#                 #activate_sound "sound/choice_button.ogg"
#                 text_hover_color "#fff"
#                 # action NullAction
#                 action [Hide("choice_1",transition=dissolve),Call("tianxi_7")]
#     showif bianli == 0:
#         vbox:
#             xcenter 0
#             ycenter 0
#             offset(0,0)
#             textbutton "便利店" offset(700,500) text_size 35 text_color "#000" text_outlines [(absolute(1), "#ff0", absolute(0), absolute(0))]:
#                 style "text_button"
#                 #activate_sound "sound/choice_button.ogg"
#                 text_hover_color "#fff"
#                 # action NullAction
#                 action [Hide("choice_1",transition=dissolve),Call("tianxi_8")]
#     # add "gui/sidebar/Task3.jpg":
#     #     zoom 0.2
#     #     at left

# screen choice_3(a,b,c,d,e,f): #地图选项3
#     add "images/backim1/schoolmap.png":
#         zoom 0.667

#     showif (a+b+c+d+e+f)==6:
#         textbutton "永恒天希未完待续" offset(500,300) text_size 35 text_color "#fbff00" text_outlines [(absolute(1), "#ff0", absolute(0), absolute(0))]:
#             style "text_button"
#             #activate_sound "sound/choice_button.ogg"
#             text_hover_color "#9e2d2d"
#             action [Hide("choice_3",transition=dissolve),MainMenu(confirm=True)]

#     showif d==0:
#         textbutton "教室(四班)" offset(550,230) text_size 35 text_color "#000" text_outlines [(absolute(1), "#ff0", absolute(0), absolute(0))]:
#             style "text_button"
#             #activate_sound "sound/choice_button.ogg"
#             text_hover_color "#fff"
#             action [Hide("choice_3",transition=dissolve),Call("tianxi_12_4")]

#     showif a==0:
#         textbutton "走廊" offset(400,350) text_size 35 text_color "#000" text_outlines [(absolute(1), "#ff0", absolute(0), absolute(0))]:
#             style "text_button"
#             #activate_sound "sound/choice_button.ogg"
#             text_hover_color "#fff"
#             action [Hide("choice_3",transition=dissolve),Call("tianxi_12_1")]

#     showif f==0:
#         textbutton "教学楼后" offset(280,230) text_size 35 text_color "#000" text_outlines [(absolute(1), "#ff0", absolute(0), absolute(0))]:
#             style "text_button"
#             #activate_sound "sound/choice_button.ogg"
#             text_hover_color "#fff"
#             action [Hide("choice_3",transition=dissolve),Call("tianxi_12_6")]

#     showif b==0:
#         textbutton "保健室" offset(400,500) text_size 35 text_color "#000" text_outlines [(absolute(1), "#ff0", absolute(0), absolute(0))]:
#             style "text_button"
#             #activate_sound "sound/choice_button.ogg"
#             text_hover_color "#fff"
#             action [Hide("choice_3",transition=dissolve),Call("tianxi_12_2")]

#     showif c==0:
#         textbutton "教室(三班)" offset(600,370) text_size 35 text_color "#000" text_outlines [(absolute(1), "#ff0", absolute(0), absolute(0))]:
#             style "text_button"
#             #activate_sound "sound/choice_button.ogg"
#             text_hover_color "#fff"
#             action [Hide("choice_3",transition=dissolve),Call("tianxi_12_3")]

#     showif e==0:
#         textbutton "校门口" offset(870,450) text_size 35 text_color "#000" text_outlines [(absolute(1), "#ff0", absolute(0), absolute(0))]:
#             style "text_button"
#             #activate_sound "sound/choice_button.ogg"
#             text_hover_color "#fff"
#             action [Hide("choice_3",transition=dissolve),Call("tianxi_12_5")]

style text_button: #按钮悬浮背景
    background "#006"
    # insensitive_background "#444"
    hover_background "#ff0000"