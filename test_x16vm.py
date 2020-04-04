from axe7.x16asm import X16Asm
from axe7.x16vm import X16Vm
from axe7.x16preprocessor import X16Preprocessor


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
    Asm = X16Asm(asmStrs)
    # assert testL == Asm.machine_code()
    vm = X16Vm(Asm.machine_code())
    vm.run()
    assert vm.reg[0] == 3000



def test2():
    asmStrs = """set2 a1 300
set2 a2 10
set2 a3 14
add2 pa a3 a3
halt"""
    Asm = X16Asm(asmStrs)
    # assert testL == Asm.machine_code()
    vm = X16Vm(Asm.machine_code())
    vm.run()
    assert vm.reg[1] == 10
    assert vm.reg[2] == 30


def test3():
    asmStrs = """set2 a1 300
set2 a2 10
set2 a3 14
subtract2 a1 a2 a3
halt"""
    Asm = X16Asm(asmStrs)
    # assert testL == Asm.machine_code()
    vm = X16Vm(Asm.machine_code())
    vm.run()
    assert vm.reg[1] == 10
    assert vm.reg[2] == 290


def test4():
    asmStrs = """set2 a1 300
set2 a2 10
save2 a1 @65534
load2 @65534 a2
halt"""
    Asm = X16Asm(asmStrs)
    # assert testL == Asm.machine_code()
    vm = X16Vm(Asm.machine_code())
    vm.run()
    assert vm.reg[0] == 300
    print("a2",vm.reg[1])
    assert vm.reg[1] == 300


def test5():
    asmStrs = """set2 a1 1
set2 a2 2
compare a1 a2
jump_if_less @label1
set2 a2 1
@label1
add2 a2 a1 a2
halt"""
    Asm = X16Asm(asmStrs)
    # assert testL == Asm.machine_code()
    vm = X16Vm(Asm.machine_code())
    vm.run()
    assert vm.reg[0] == 1
    print("if", vm.reg[1])
    assert vm.reg[1] == 3


def test6():
    asmStrs = """set2 a1 16
save2 a1 @65534
set2 a1 65534
load_from_register2 a1 a2
halt"""
    Asm = X16Asm(asmStrs)
    # assert testL == Asm.machine_code()
    vm = X16Vm(Asm.machine_code())
    vm.run()
    assert vm.reg[0] == 65534
    assert vm.reg[1] == 16


def test7():
    asmStrs = """set2 a2 16
set2 a1 65534
save_from_register2 a1 a2
halt"""
    Asm = X16Asm(asmStrs)
    # assert testL == Asm.machine_code()
    vm = X16Vm(Asm.machine_code())
    vm.run()
    assert vm.memory[16] == 65534


def test8():
    asmStrs = """set2 a1 10
jump_from_register a1
set2 a1 1
halt"""
    Asm = X16Asm(asmStrs)
    # assert testL == Asm.machine_code()
    vm = X16Vm(Asm.machine_code())
    vm.run()
    assert vm.reg[0] == 10


def test9():
    asmStrs = """set2 f1 3
jump @function_end
@function_add
add2 a1 a2 a1
set2 a3 2
subtract2 f1 a3 f1
load_from_register2 f1 a2
jump_from_register a2
@function_end
set2 a1 7
set2 a2 8
set2 a3 14
add2 pa a3 a3
save_from_register2 a3 f1
set2 a3 2
add2 f1 a3 f1
jump @function_add
halt"""
    Asm = X16Asm(asmStrs)
    print(len(Asm.machine_code()))
    # assert testL == Asm.machine_code()
    vm = X16Vm(Asm.machine_code())
    vm.run()
    assert vm.reg[0] == 15


def test10():

    preAsmStr = """jump @1024
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
.return
@function_end
set2 a1 300
set2 a2 10
.call @function_multiply
halt"""
    Preprocessor = X16Preprocessor(asmStrs)
    # Preprocessor.pretreat()
    assert preAsmStr.split() == Preprocessor.pretreat().split()
    # print(Preprocessor.pretreat())
    Asm = X16Asm(Preprocessor.pretreat())
    # assert testL == Asm.machine_code()
    vm = X16Vm(Asm.machine_code())
    vm.run()
    assert vm.reg[0] == 3000


def __main():
    # machine_code(asm)
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()
    # test8()
    # test9()
    test10()


__main()
