##琴里模型修复
init python:
    def kot_mouth_close(l2d,time):
        l2d.blend_parameter("ParamMouthOpenY","Overwrite",0)
        return None


#blend_parameter(update_function,add,kot_mouth_close,weight=0.9)

##摇头修复
init python:
    def rio_z(l2d,time):
        #头
        l2d.blend_parameter("ParamAngleZ","Overwrite",0)
        #后发
        l2d.blend_parameter("Param_Angle_Rotation_1_ArtMesh40","Overwrite",0)
        l2d.blend_parameter("Param_Angle_Rotation_2_ArtMesh40","Overwrite",0)
        l2d.blend_parameter("Param_Angle_Rotation_3_ArtMesh40","Overwrite",0)
        l2d.blend_parameter("Param_Angle_Rotation_4_ArtMesh40","Overwrite",0)
        #辫子
        l2d.blend_parameter("Param_Angle_Rotation_1_ArtMesh6","Overwrite",0)
        l2d.blend_parameter("Param_Angle_Rotation_2_ArtMesh6","Overwrite",0)
        l2d.blend_parameter("Param_Angle_Rotation_3_ArtMesh6","Overwrite",0)
        l2d.blend_parameter("Param_Angle_Rotation_4_ArtMesh6","Overwrite",0)
        l2d.blend_parameter("Param_Angle_Rotation_5_ArtMesh6","Overwrite",0)
        l2d.blend_parameter("Param_Angle_Rotation_6_ArtMesh6","Overwrite",0)
        #前发
        l2d.blend_parameter("ParamHairFront","Overwrite",0)
        l2d.blend_parameter("ParamHairSide","Overwrite",0)
        return None
