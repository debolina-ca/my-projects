# Foot Bones Quiz Function
def foot_bones_search(search_item, foot_bones):
    for bone in foot_bones:
        if bone.lower() == search_item.lower():
            foot_bones.remove(bone)
            return "correct"
        else:
            pass
    return "incorrect"


x = 0
count = 0
while x < 2:
    foot_bones1 = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate cuneiform",
                    "medial cuneiform"]
    search_item1 = input("Enter the name of a foot bone:\n")
    rtn = foot_bones_search(search_item1, foot_bones1)
    print(search_item1, "is", rtn)
    if rtn == "correct":
        count += 1
    x += 1
print(foot_bones1)
print("Total number of foot bones identified is: ", count)
