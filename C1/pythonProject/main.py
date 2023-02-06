# class FamilyViewer:
#     def __init__(self, name="", age=0):
#         self.name = name
#         self.age = age
#
#
# family = [
#     {"name": "Oleg", "age": 34},
#     {"name": "Oleg", "age": 4},
#     {"name": "Nelly", "age": 46},
# ]
#
# for member in family:
#     member_subj = FamilyViewer(name=member.get("name"), age=member.get("age"))
#     print(member_subj.name)
#     print(member_subj.age)

class FamilyViewer:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def init_from_dict(self, family_dict):
        self.name = family_dict.get("name")
        self.age = family_dict.get("age")


family = [
    {"name": "Oleg", "age": 34},
    {"name": "Oleg", "age": 4},
    {"name": "Nelly", "age": 46},
]


for member in family:
    member_subj = FamilyViewer()
    member_subj.init_from_dict(member)
    print(member_subj.name)
    print(member_subj.age)
