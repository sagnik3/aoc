from __future__ import annotations 
import os
import argparse
import time
import collections 

INPUT = os.path.join(os.path.dirname(__file__),'input.txt')


def compute(s: str) -> int:
    coords =  




def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file',nargs='?',default=INPUT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        t_start = time.perf_counter_ns()
        print(compute(f.read()))
        t_stop = time.perf_counter_ns()
        print(t_stop-t_start)

    return 0


if __name__=='__main__':
    raise SystemExit(main())
