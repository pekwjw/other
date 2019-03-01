# -*- coding:utf-8 -*-

# reference： 
# doc： https://blog.csdn.net/asukasmallriver/article/details/74356771
# graphviz: https://graphviz.gitlab.io/_pages/Download/Download_source.html

fib = lambda n: 1 if n <= 2 else fib(n-1) + fib(n-2)

def test1():
    fib(20)

def test2():
    fib(30)

def test3():
    fib(35)

if __name__ == "__main__":
    test1()
    test2()
    test3()
    import cProfile
    cProfile.run("test1()")
    cProfile.run("test2()")
    cProfile.run("test3()")

# output:

#          13532 function calls (4 primitive calls) in 0.003 seconds
# 
#    Ordered by: standard name
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#   13529/1    0.003    0.000    0.003    0.003 cProfile_test.py:3(<lambda>)
#         1    0.000    0.000    0.003    0.003 cProfile_test.py:5(test1)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 
# 
#          1664082 function calls (4 primitive calls) in 0.329 seconds
# 
#    Ordered by: standard name
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.329    0.329 <string>:1(<module>)
# 1664079/1    0.329    0.000    0.329    0.329 cProfile_test.py:3(<lambda>)
#         1    0.000    0.000    0.329    0.329 cProfile_test.py:8(test2)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 
# 
#          18454932 function calls (4 primitive calls) in 3.642 seconds
# 
#    Ordered by: standard name
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    3.642    3.642 <string>:1(<module>)
#         1    0.000    0.000    3.642    3.642 cProfile_test.py:11(test3)
# 18454929/1    3.642    0.000    3.642    3.642 cProfile_test.py:3(<lambda>)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 图形化工具：
# pip install gprof2dot 
# tar -zxvf graphviz.tar.gz && ./configure & make & make install graphviz
# gprof2dot -f pstat result.out | dot -Tpng -o result.png
