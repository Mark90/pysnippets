"""
This benchmark is intended to discover the effectiveness of using the @lru_cache wrapper
while performing reproducible computations
"""
import platform
import timeit
from datetime import datetime
from functools import lru_cache
from utils import system

DATA = list(range(1, 100))


def calc_normal(input):
    result = float(input)
    for el in DATA:
        result *= el
    return result


@lru_cache(maxsize=8)
def calc_cache_8(input):
    result = float(input)
    for el in DATA:
        result *= el
    return result


@lru_cache(maxsize=16)
def calc_cache_16(input):
    result = float(input)
    for el in DATA:
        result *= el
    return result


@lru_cache(maxsize=32)
def calc_cache_32(input):
    result = float(input)
    for el in DATA:
        result *= el
    return result


@lru_cache(maxsize=64)
def calc_cache_64(input):
    result = float(input)
    for el in DATA:
        result *= el
    return result


def do_calc(func, input):
    for el in input:
        func(el)


if __name__ == "__main__":
    setupstr = """from benchmarks import do_calc, {method} as calc_method
input = {repetitiveness} * list(range({inputsize}))"""
    timeit_repetitions = 1000

    tests = [
        {'base': True, 'method': 'calc_normal', 'repetitiveness': 100, 'inputsize': 5},
        {'base': False, 'method': 'calc_cache_8', 'repetitiveness': 100, 'inputsize': 5},
        {'base': False, 'method': 'calc_cache_16', 'repetitiveness': 100, 'inputsize': 5},
        {'base': False, 'method': 'calc_cache_32', 'repetitiveness': 100, 'inputsize': 5},
        {'base': False, 'method': 'calc_cache_64', 'repetitiveness': 100, 'inputsize': 5},
        {'base': True, 'method': 'calc_normal', 'repetitiveness': 10, 'inputsize': 15},
        {'base': False, 'method': 'calc_cache_8', 'repetitiveness': 10, 'inputsize': 15},
        {'base': False, 'method': 'calc_cache_16', 'repetitiveness': 10, 'inputsize': 15},
        {'base': False, 'method': 'calc_cache_32', 'repetitiveness': 10, 'inputsize': 15},
        {'base': False, 'method': 'calc_cache_64', 'repetitiveness': 10, 'inputsize': 15},
        {'base': True, 'method': 'calc_normal', 'repetitiveness': 3, 'inputsize': 30},
        {'base': False, 'method': 'calc_cache_8', 'repetitiveness': 3, 'inputsize': 30},
        {'base': False, 'method': 'calc_cache_16', 'repetitiveness': 3, 'inputsize': 30},
        {'base': False, 'method': 'calc_cache_32', 'repetitiveness': 3, 'inputsize': 30},
        {'base': False, 'method': 'calc_cache_64', 'repetitiveness': 3, 'inputsize': 30},
        {'base': True, 'method': 'calc_normal', 'repetitiveness': 10, 'inputsize': 30},
        {'base': False, 'method': 'calc_cache_8', 'repetitiveness': 10, 'inputsize': 30},
        {'base': False, 'method': 'calc_cache_16', 'repetitiveness': 10, 'inputsize': 30},
        {'base': False, 'method': 'calc_cache_32', 'repetitiveness': 10, 'inputsize': 30},
        {'base': False, 'method': 'calc_cache_64', 'repetitiveness': 10, 'inputsize': 30},
        {'base': True, 'method': 'calc_normal', 'repetitiveness': 3, 'inputsize': 50},
        {'base': False, 'method': 'calc_cache_8', 'repetitiveness': 3, 'inputsize': 50},
        {'base': False, 'method': 'calc_cache_16', 'repetitiveness': 3, 'inputsize': 50},
        {'base': False, 'method': 'calc_cache_32', 'repetitiveness': 3, 'inputsize': 50},
        {'base': False, 'method': 'calc_cache_64', 'repetitiveness': 3, 'inputsize': 50},
    ]

    test_results = []

    print(
        "UTC time: {dt}\n"
        "Python build: {pybuild}\n"
        "System: {un.system} {un.release}\n"
        "Full uname: {un.version}\n"
        "CPU: {cpu}\n\n"
        "Test count: {num}\n"
        "Timeit repetitions: {trep}\n\n".format(
            num=len(tests), dt=datetime.utcnow(),
            pybuild=" ".join(platform.python_build()),
            un=platform.uname(),
            cpu=system.get_processor_name(),
            trep=timeit_repetitions,
        ))

    for cur, test in enumerate(tests):
        test_results.append((test, timeit.timeit(
            'do_calc(calc_method, input)',
            setup=setupstr.format(**test),
            number=timeit_repetitions
        )))

    column_separator = ' | '
    print("| {col2:15s}{cs}{col3:15s}{cs}{col4:15s}{cs}{col5:15s}{cs}{col6:15s} |\n{sepline}".format(
        cs=column_separator, col2='Method', col3='Repetitiveness', col4='Inputsize',
        col5='Timed result', col6='Speedup',
        sepline='-' * (5 * 15 + 4 * len(column_separator) + 4)
    ))
    for result in test_results:
        if result[0]['base'] == True:
            cur_base_result = result[1]
            speedup = ''
        else:
            speedup = "{0:10.2f}".format(cur_base_result / result[1])
        print(
            "| {params[method]:15s}{cs}{params[repetitiveness]:15d}{cs}{params[inputsize]:15d}{cs}{timeitres:15f}{cs}{speedup:15s} |".format(
                cs=column_separator,
                params=result[0],
                timeitres=result[1],
                speedup=speedup,
            ))

"""
UTC time: 2017-05-17 09:39:07.911553
Python build: v3.6.1:69c0db5050 Mar 21 2017 01:21:04
System: Darwin 16.5.0
Full uname: Darwin Kernel Version 16.5.0: Fri Mar  3 16:52:33 PST 2017; root:xnu-3789.51.2~3/RELEASE_X86_64
CPU: Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz

Test count: 25
Timeit repetitions: 10000


| Method          | Repetitiveness  | Inputsize       | Timed result    | Speedup         |
-------------------------------------------------------------------------------------------
| calc_normal     |             100 |               5 |       25.138722 |                 |
| calc_cache_8    |             100 |               5 |        0.609216 |      41.26      |
| calc_cache_16   |             100 |               5 |        0.636043 |      39.52      |
| calc_cache_32   |             100 |               5 |        0.608776 |      41.29      |
| calc_cache_64   |             100 |               5 |        0.623741 |      40.30      |
| calc_normal     |              10 |              15 |        7.563845 |                 |
| calc_cache_8    |              10 |              15 |        7.939889 |       0.95      |
| calc_cache_16   |              10 |              15 |        0.181995 |      41.56      |
| calc_cache_32   |              10 |              15 |        0.184640 |      40.97      |
| calc_cache_64   |              10 |              15 |        0.183464 |      41.23      |
| calc_normal     |               3 |              30 |        4.530677 |                 |
| calc_cache_8    |               3 |              30 |        4.788045 |       0.95      |
| calc_cache_16   |               3 |              30 |        4.737071 |       0.96      |
| calc_cache_32   |               3 |              30 |        0.109126 |      41.52      |
| calc_cache_64   |               3 |              30 |        0.110796 |      40.89      |
| calc_normal     |              10 |              30 |       14.976377 |                 |
| calc_cache_8    |              10 |              30 |       15.891499 |       0.94      |
| calc_cache_16   |              10 |              30 |       15.942704 |       0.94      |
| calc_cache_32   |              10 |              30 |        0.372963 |      40.16      |
| calc_cache_64   |              10 |              30 |        0.364354 |      41.10      |
| calc_normal     |               3 |              50 |        7.569665 |                 |
| calc_cache_8    |               3 |              50 |        7.945846 |       0.95      |
| calc_cache_16   |               3 |              50 |        7.899385 |       0.96      |
| calc_cache_32   |               3 |              50 |        7.945190 |       0.95      |
| calc_cache_64   |               3 |              50 |        0.190374 |      39.76      |
"""
