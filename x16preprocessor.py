class X16Preprocessor:
    def __init__(self, asmStr):
        self.asmStr = asmStr


    def pretreat(self):
        # preAsmStr = """"""
        self.asmStr = self.asmStr.replace(".return", """set2 a3 2
subtract2 f1 a3 f1
load_from_register2 f1 a2
jump_from_register a2""")
        self.asmStr = self.asmStr.replace(".call", """set2 a3 14
add2 pa a3 a3
save_from_register2 a3 f1
set2 a3 2
add2 f1 a3 f1
jump""")
#         for s in self.asmStr.split():
#             if s == ".return":
#                 preAsmStr += """set2 a3 2
# subtract2 f1 a3 f1
# load_from_register2 f1 a2
# jump_from_register a2
# """
#             elif s == ".call":
#                 preAsmStr += """set2 a3 14
# add2 pa a3 a3
# save_from_register2 a3 f1
# set2 a3 2
# add2 f1 a3 f1
# jump
# # """
#             else:
#                 print("1",s)
#                 preAsmStr += s + '\n'
        # print(preAsmStr)
        # str = "this is string example....wow!!! this is really string"
        # print(str.replace(" is ", " was "))
        return self.asmStr