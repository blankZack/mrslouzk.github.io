#主线剧情脚本
define config.gl2 = True

label splashscreen: #初始画面
    show prestart with dissolve
    pause(2)
    hide prestart with dissolve
    pause(1)
    $ renpy.movie_cutscene('audio/opening1.ogv') #播放reborn logo
    pause(1)
    $ renpy.movie_cutscene('audio/opening2.ogv') #播放op
    return

label main_menu: #主菜单调用
    play music "bgm/mainmenu.mp3"
    call screen main_menu with dissolve

label start:
    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。

    scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # “eileen happy.png”的文件来将其替换掉。

    show eileen happy

    # 此处显示各行对话。

    e "您已创建一个新的 Ren'Py 游戏。"

    return

label te_bie_pian:
    play music "bgm/game_music/bgm17_01.mp3" fadein 1.0
    scene ke_ting0 with dissolve
    scene black onlayer real_bg as bg_black
    define rio_loop="Ture"

    show black onlayer fade_layer at half_alpha with disv_slow
    no_person "自己究竟是不是自己，所谓的自己又会不会仅仅是他人替代"
    no_person "要问我为什么会突然想起这些事，还要从不久前说起"
    hide black onlayer fade_layer with disv_slow

    show rio wait_1 at rio_show_left with dissolve
    rio "呐，鞠亚姐姐"

    show black onlayer fade_layer at half_alpha with disv_slow
    rio "我的名字叫凛绪，是由【弗拉克西纳斯】的管理AI，鞠亚制作出的另一个AI"
    rio "虽然这么说，但我觉得我们和其他的人工智能有着一些区别"
    hide black onlayer fade_layer with disv_slow

    show mar wait_1 at mar_show_right with dissolve

    my "怎么了，凛绪？"
    rio "能再和我说一下吗，那个凛绪的事"
    my "你这么感兴趣吗？好吧。上次说到哪里来着"

    show black onlayer fade_layer at half_alpha with disv_slow
    no_person "是的，其实我早已经知道。自己的名字是以前大家一位朋友的名字。但那位“凛绪”已经因为某种原因消失了"

    hide mar with dissolve
    hide rio with dissolve
    scene memory01 with dissolve
    rio "虽然我的数据库中有模糊的相关画面，但还是需要鞠亚姐姐来叙述准确的故事"
    hide memory01 with dissolve

    no_person "至于这里，是只属于我的世界。或许这样说有些过，但这里平常确实只有我一个人"
    scene xue_xiao0 at fade_in_down with dissolve
    scene wu_he_home0 at fade_in_right with dissolve
    scene qi_ta0 at fade_in_left with dissolve
    no_person "在平常结束工作后，我就会建设这个存在于数据的世界。虽然这个世界越来越真实。但为何我却一点都高兴不起来......"
    no_person "我究竟怎么了......"
    ik "凛绪？凛绪！"
    hide qi_ta0 with dissolve

    pause 1.0
    play sound "sound/open_door.mp3"
    stop music fadeout 1.0
    scene fei_chuan0 with dissolve
    play music "bgm/game_music/bgm05_01.mp3"
    hide black onlayer fade_layer with dissolve

    show kot angry_1 at kot_show with dissolve #琴里l2d修复
    rio "欸？！"
    show kot liuhan_1 at kot_show
    ik "怎么了，你是在发呆吗？AI也会这样？"

    show black onlayer fade_layer at half_alpha with disv_slow
    no_person "五河琴里，【弗拉克西纳斯】的司令官。也是鞠亚姐姐喜欢捉弄排名第一的“被害人”"
    hide black onlayer fade_layer with disv_slow

    scene fei_chuan0 with dissolve
    show kot angry_1 at kot_show_left
    show mar wait_1 at mar_show_right with dissolve
    my "(嫌弃)只是发呆而已，琴里又在大惊小怪了"
    ik "说到底凛绪是鞠亚你制作的吧，解释一下？"
    my "即便是AI也是有自主意识和感情，是吧。凛绪"
    rio "额...嗯！凛绪可是凛绪哦！"
    ik "你们两个啊...受不了"
    hide mar with dissolve

    play sound "sound/Se_00257(dead).ogg"
    show kot shy_1 at kot_show_left
    show shd wait_1 at shd_show_right
    sd "琴里，我按时到达了"
    ik "哦，效率很高啊。不愧是士道呢～"

    show black onlayer fade_layer at half_alpha with disv_slow
    sd "五河士道，爸爸....是被称为精灵攻略使的男人，一直为了拯救作为精灵的大家所努力着"
    hide black onlayer fade_layer with disv_slow

    sd "早上好，鞠亚，还有凛绪"
    my "早上好，士道"
    rio "爸爸早上好！"
    sd "(流汗)爸爸这个称呼就不吐槽了....琴里，有什么紧急的事件吗？"
    show kot angry_1 at kot_show_left
    ik "嗯，最近雷达探索到。有一股类似【灵魂碎片】的能量体就潜伏在天宫市里"
    ik "虽然还不能完全确定....."
    ik "但为了大家的安全，不再出现四糸乃那时的情况"
    sd "我应该去照看大家的状态，对吧。正巧我们的想法一样呢。琴里～"
    stop music fadeout 1.0

    play music "bgm/game_music/bgm36_01.mp3"
    show kot shy_1 at kot_show_left
    pause 1.5
    ik "呵，不是出自责任还是什么。只是士道你想要去这么做"
    ik "怎么说呢，这就叫做成长吗"
    sd "嗯，当然。不止是我。大家都在不断前进"
    sd "事不宜迟，我出发了！"
    all_people "一路顺风"

    play sound "sound/Se_00257(dead).ogg"
    hide kot with dissolve
    hide shd with dissolve
    show mar wait_1 at mar_show_right with dissolve
    rio ".........."
    show mar happy_1 at mar_show_right
    my "说的对啊，大家都朝着自己的方向前进了呢，凛绪"
    show mar wait_1
    rio "嗯，说的对"
    rio "无论是爸爸，四糸乃酱，还是大家都因为各自经历的事情变得不一样了呢...."
    rio "鞠亚姐姐你也是，以前还总喜欢捉弄琴里酱呢"
    my "那凛绪呢，觉得自己哪里变了吗？"
    rio "欸？！我...."
    hide mar with dissolve
    stop music fadeout 1.0

    play sound "sound/Se_00057.ogg"
    hide fei_chuan0 with disv_slow2
    scene ke_ting0 with fade
    show rio wait_1 at rio_show with dissolve
    play music "bgm/game_music/rb2.mp3" fadein 1.0

    rio "成长....吗"
    rio "说的是啊，经历很多事后。大家都得到了成长！那么，为了不掉队。我也不能落后！"
    rio "今天也要继续把这个世界建设的更好，加油！"
    rio "我出门了..."

    scene ke_ting0 at bg_move_2
    show rio weiqu_1 at rio_show
    play sound "sound/0011.mp3"
    rio "好痛....忘记这个世界里，凛绪也是实体的了..."
    show rio wait_1 at rio_show
    rio "欸，这是照片吗。好像是鞠亚姐姐上次放在这里的"
    hide rio with dissolve
    hide ke_ting0 with dissolve

    show memory02 at fade_in_up with dissolve
    show black onlayer fade_layer at half_alpha with disv_slow
    rio "啊，这是凛绪和爸爸鞠亚姐姐一起出门！然后....."
    rio "然后....."
    rio "嗯，记不起来"
    rio "....或者不是我吧"
    rio "明明照片上的人与自己样子一样。却不是，这种感觉好奇怪呢..."
    rio "好奇怪....."
    rio "园神凛绪，我....真的要成为你吗？"
    stop music

    smr "如果真的只是要成为别人的话，未免太无趣了点吧"
    play music "bgm/game_music/bgm16_01.mp3"
    hide black onlayer fade_layer with disv_slow
    scene ke_ting0 with dissolve
    show rio wait_1 at rio_show
    rio "？！"
    rio "这个声音...不是鞠亚姐姐，你是谁？！"
    hide rio with dissolve

    define rio_loop="False"
    play sound "sound/Se_00042(乱码声).ogg"
    scene ke_ting1 with disv_fast
    show shen_mi0 at alpha3 onlayer fade_layer with dissolve

    smr "哦呀哦呀，把这么一个可爱的小妹妹丢在这个清冷的世界"
    smr "你的那位鞠亚姐姐还真是无趣啊~"
    show rio angry_1 at rio_show with dissolve
    rio "你...到底是谁。是敌人的话，就不要怪凛绪不欢迎你了！"
    smr "呵呵呵....我是谁并不重要，小妹妹。但我明白你的一切哦"
    smr "明明是一个独立的个体，却因为某些人可笑的执念"
    smr "让你去成为他人，他们甚至只是把你当成替代物品而已哦~"
    rio ".....才，才不是你说的那样。爸爸，鞠亚姐姐，天希。他们都！"
    smr "呵呵...我只是开个玩笑，别激动嘛~"
    smr "哦~说起来刚才对话出现一个很让人生厌的名字耶"
    smr "呵呵，算了。小妹妹，想和我玩个游戏吗"
    rio "游...戏？"
    rio "你有什么坏心思？"
    smr "我也是来实现大家的心愿的，告诉我吧。你想要玩什么？"
    rio "..........."
    hide shen_mi0 onlayer fade_layer
    scene black with dissolve

    return
