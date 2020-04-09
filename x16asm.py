class X16Asm:
    def __init__(self, asmStr):
        self.asmStr = asmStr
        self.labels = {}
        self.pa = 0
        self.tranSet = {
            'set': 0,
            'load': 1,
            'add': 2,
            'save': 3,
            'compare': 4,
            'jump_if_less': 5,
            'jump': 6,
            'save_from_register': 7,
            'halt': 255,
            'set2': 8,
            'load2': 9,
            'add2': 10,
            'save2': 11,
            'subtract2': 12,
            'load_from_register': 13,
            'load_from_register2': 14,
            'save_from_register2': 15,
            'jump_from_register': 16,
            'a1': 16,
            'a2': 32,
            'a3': 48,
            'c1': 64,
            'f1': 80,
            'pa': 0,
        }


    def find_label(self, asmStrs):
        for Str in asmStrs:
            if Str[0] == '@':
                # print(s[1:])
                self.labels[Str[1:]] = self.pa
                # self.pa = self.pa + 1
            else:
                for s in Str.split():

                    if s[0] == '@':
                        self.pa = self.pa + 2
                    else:
                        try:
                            int(s)
                            self.pa = self.pa + 2
                        except:
                            self.pa = self.pa + 1
            # print(self.labels)
        self.pa = 0


    def machine_code(self):
        asmStrs = self.asmStr.split('\n')
        self.find_label(asmStrs)
        instructionL = []
        for asm_str in asmStrs:
            ops = asm_str.split()
            #省略开头的@
            if ops[0][0] == '@':
                continue
            for op in ops:
                if self.tranSet.get(op) != None:
                    instructionL.append(self.tranSet[op])
                else:
                    if op[0] == '@':
                        try:
                            instructionL.append(int(op[1:]))
                            instructionL.append(0)
                        except:
                            instructionL.append(self.labels[op[1:]])
                            instructionL.append(0)
                    else:
                         instructionL.append(int(op))
                         instructionL.append(0)
        # print(instructionL)
        return instructionL


# def __main():
#     # machine_code(asm)
#     instructionL = machine_code(asm)
#     testL = [0, 16, 1, 0, 32, 2, 3, 16, 100, 3, 32, 101, 1, 100, 16, 1, 101, 32, 2, 16, 32, 48, 3, 48, 102, 4, 16, 32, 5, 11, 2, 48, 32, 16, 11, 2, 48, 16, 32]
#     if testL == instructionL:
#         print("success")


# __main()