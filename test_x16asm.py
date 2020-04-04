from axe7.x16asm import X16Asm


def test1():
    asmStrs = """jump @1024
set2 f1 3
jump @function_end
@function_multiply
set2 a3 2
save2 a1 @65534
@while_start
compare a2 a3
jump_if_less @while_end
save2 a2 @65532
set2 a2 1
add2 a3 a2 a3
load2 @65534 a2
add2 a1 a2 a1
load2 @65532 a2
jump @while_start
@while_end
set2 a3 2
subtract2 f1 a3 f1
load_from_register2 f1 a2
jump_from_register a2
@function_end
set2 a1 300
set2 a2 10
set2 a3 14
add2 pa a3 a3
save_from_register2 a3 f1
set2 a3 2
add2 f1 a3 f1
jump @function_multiply
halt"""
    testL = [6, 1024, 8, 80, 3, 6, 52, 8, 48, 2, 11, 16, 65534, 4, 32, 48, 5, 40, 11, 32, 65532, 8, 32, 1, 10, 48, 32, 48, 9, 65534, 32, 10, 16, 32, 16, 9, 65532, 32, 6, 13, 8, 48, 2, 12, 80, 48, 80, 14, 80, 32, 16, 32, 8, 16, 300, 8, 32, 10, 8, 48, 14, 10, 0, 48, 48, 15, 48, 80, 8, 48, 2, 10, 80, 48, 80, 6, 7, 255]

    # testL = [
    #     6, 1024,
    #     8, 80, 3,
    #     6, 55,
    #     7,
    #     8, 48, 2,
    #     11, 16, 65534,
    #     14,
    #     4, 32, 48,
    #     5, 42,
    #     11, 32, 65532,
    #     8, 32, 1,
    #     10, 48, 32, 48,
    #     9, 65534, 32,
    #     10, 16, 32, 16,
    #     9, 65532, 32,
    #     6, 14,
    #     42,
    #     8, 48, 2,
    #     12, 80, 48, 80,
    #     14, 80, 32,
    #     16, 32,
    #     55,
    #     8, 16, 300,
    #     8, 32, 10,
    #     8, 48, 14,
    #     10, 0, 48, 48,
    #     15, 48, 80,
    #     8, 48, 2,
    #     10, 80, 48, 80,
    #     6, 7,
    #     255,
    # ]

    Asm = X16Asm(asmStrs)
    # print(Asm.machine_code())
    # mix = list(zip(testL, Asm.machine_code()))
    # i = 0
    # for s1, s2 in mix:
    #     i+=1
    #     if s1 != s2:
    #         print(i, s1, s2)
    #     print(i, s1, s2)
    # print(testL)
    assert testL == Asm.machine_code()


def test1():
    asmStrs = """jump @1024
set2 f1 3
jump @function_end
@function_multiply
set2 a3 2
save2 a1 @65534
@while_start
compare a2 a3
jump_if_less @while_end
save2 a2 @65532
set2 a2 1
add2 a3 a2 a3
load2 @65534 a2
add2 a1 a2 a1
load2 @65532 a2
jump @while_start
@while_end
set2 a3 2
subtract2 f1 a3 f1
load_from_register2 f1 a2
jump_from_register a2
@function_end
set2 a1 300
set2 a2 10
set2 a3 14
add2 pa a3 a3
save_from_register2 a3 f1
set2 a3 2
add2 f1 a3 f1
jump @function_multiply
halt"""
    testL = []
    Asm = X16Asm(asmStrs)
    assert testL == Asm.machine_code()


def __main():
    # machine_code(asm)
    test1()
    # test2()
# __main()
