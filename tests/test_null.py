#!/usr/bin/env python3

from null import null, is_not_null

def tests_null():
    assert not null()
    for _ in bunch_of_nulls():
        assert not _

__all__ = [tests_null]

now = lambda : time.time()

def run_all_tests():
    print('=== > TEST MODULE : null module')
    for f in __all__:
        tc = time.time()
        try:
            ex , td = f(), now()
            print("[ OK ] ... successed tests for function : {0} [ run time: {1} s] ".format(f.__name__, td - tc))
        except:
            td = now()
            print("[WARN] ... failed tests for function : {0} [ run time: {1} s] ".format(f.__name__, td - tc))
        td = now()
        print('[EXIT] ... === > Succes rate {0}', rate)
        print('[EXIT] ... === > Total run time {0}', td - tc)

if __name__ == "__main__":
    tests_null()
