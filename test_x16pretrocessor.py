from axe7.x16preprocessor import X16Preprocessor


def test1():
    asmStrs = """set2 f1 3
jump @function_end
@function_add
add2 a1 a2 a1
.return
@function_end
set2 a1 7
set2 a2 8
.call @function_add
halt"""
    preAsmStr = """set2 f1 3
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
    Preprocessor = X16Preprocessor(asmStrs)
    print(preAsmStr)
    print(Preprocessor.pretreat())
    assert preAsmStr.split() == Preprocessor.pretreat().split()

def __main():
    # machine_code(asm)
    # test1()
    test1()

    # test9()

__main()