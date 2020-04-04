class X16Vm:
    def __init__(self, machineCode):
        self.memory = [0] * 65535
        self.machineCode = machineCode
        # reg a1 a2 a3 c1 f1 pa
        self.reg = [0] * 6
        # self.self.reg[5] =0
        self.regSet = {
            16: 0,
            32: 1,
            48: 2,
            64: 3,
            80: 4,
            0: 5,
        }



    def run(self):
        # print('run')

        # self.reg[5] = 0
        # instruction_set = {
        #     'set': set_fuc,
        #     'save': save_fuc,
        #     'load': load_fuc,
        #     'add': add_func,
        #     'compare': compare_fuc,
        #     'jump_if_great': jump_if_great,
        # }
        mCode = self.machineCode
        # print(mCode)
        while self.machineCode[self.reg[5]] != 255:
            # print('machineCode')
            #jump
            if mCode[self.reg[5]] == 6:
                if mCode[self.reg[5]+1] == 1024:
                    self.reg[5] += 3
                else:
                    j = mCode[self.reg[5]+1]
                    self.reg[5] = j
                    # print('jump', mCode[self.reg[5]])
            #set2
            elif mCode[self.reg[5]] == 8:
                self.reg[5] += 4
                regN = self.regSet[mCode[self.reg[5]-3]]
                self.reg[regN] = mCode[self.reg[5]-2]
                # print(mCode[self.reg[5]+2])
            #load2
            elif mCode[self.reg[5]] == 9:
                self.reg[5] += 4
                regN1 = self.regSet[mCode[self.reg[5]-1]]
                self.reg[regN1] = self.memory[mCode[self.reg[5]-3]]
            #add2
            elif mCode[self.reg[5]] == 10:
                # print(10, mCode[self.reg[5]+1])
                self.reg[5] += 4
                regN1 = self.regSet[mCode[self.reg[5]-3]]
                # print(self.reg[regN1])
                regN2 = self.regSet[mCode[self.reg[5]-2]]
                regN3 = self.regSet[mCode[self.reg[5]-1]]
                reg1 = self.reg[regN1]
                reg2 = self.reg[regN2]
                self.reg[regN3] = reg1 + reg2
                # print(mCode[self.reg[5]+2])
                # print("add2", self.reg[regN3])
            #save2
            elif mCode[self.reg[5]] == 11:
                self.reg[5] += 4
                regN1 = self.regSet[mCode[self.reg[5]-3]]
                reg1 = self.reg[regN1]
                self.memory[mCode[self.reg[5]-2]] = reg1
            #subtract2
            elif mCode[self.reg[5]] == 12:
                # print(10, mCode[self.reg[5]+1])
                regN1 = self.regSet[mCode[self.reg[5]+1]]
                # print(self.reg[regN1])
                regN2 = self.regSet[mCode[self.reg[5]+2]]
                regN3 = self.regSet[mCode[self.reg[5]+3]]
                reg1 = self.reg[regN1]
                reg2 = self.reg[regN2]
                self.reg[regN3] = reg1 - reg2
                # print(mCode[self.reg[5]+2])
                self.reg[5] += 4
                # print("subtract2", self.reg[regN3])
            #compare
            elif mCode[self.reg[5]] == 4:
                self.reg[5] += 3
                regN1 = self.regSet[mCode[self.reg[5]-2]]
                # print(self.reg[regN1])
                regN2 = self.regSet[mCode[self.reg[5]-1]]
                reg1 = self.reg[regN1]
                reg2 = self.reg[regN2]
                if reg1 < reg2:
                    self.reg[3] = 1
            #jump_if_less
            elif mCode[self.reg[5]] == 5:
                # print('self.reg[3]',self.reg[3])
                if self.reg[3] == 1:
                    j = mCode[self.reg[5]+1]
                    # print('jump_if_less', j)
                    self.reg[5] = j
                else:
                    self.reg[5] += 3
                # print('jump', mCode[self.reg[5]])
            #load_from_register2
            elif mCode[self.reg[5]] == 14:
                self.reg[5] += 3
                regN1 = self.regSet[mCode[self.reg[5]-2]]
                # print(self.reg[regN1])
                regN2 = self.regSet[mCode[self.reg[5]-1]]
                reg1 = self.reg[regN1]
                self.reg[regN2] = self.memory[reg1]
            #save_from_register2
            elif mCode[self.reg[5]] == 15:
                self.reg[5] += 3
                regN1 = self.regSet[mCode[self.reg[5]-2]]
                # print(self.reg[regN1])
                regN2 = self.regSet[mCode[self.reg[5]-1]]
                reg1 = self.reg[regN1]
                reg2 = self.reg[regN2]
                self.memory[reg2] = reg1
            #jump_from_register
            elif mCode[self.reg[5]] == 16:
                regN1 = self.regSet[mCode[self.reg[5]+1]]
                # print(self.reg[regN1])
                reg1 = self.reg[regN1]
                self.reg[5] = reg1
                # print("jump_from_register", reg1)
                # print("jump halt", self.machineCode[self.reg[5]])
            # else:
            #     self.reg[5] += 1
            #     print('self.reg[5]:', self.reg[5])
