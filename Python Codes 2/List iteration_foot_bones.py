foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform",
            "intermediate cuneiform", "medial cuneiform"]
longer_names = ""
shorter_names = ""
for bone_name in foot_bones:
    if len(bone_name) < 10:
        shorter_names += bone_name + "\n"
    else:
        longer_names += bone_name + "\n"
print(shorter_names, "\n")
print(longer_names, "\n")