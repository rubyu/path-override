#!/usr/bin/python3

import sys
import os
import subprocess


def read_path_file(path):
    with open(path, "r") as f:
        return ";".join(f.readlines())


def get_override_env(path_value):
    env = os.environ
    env["PATH"] = path_value
    return env


def execute_program(exec_list, path_value):
    env = get_override_env(path_value)
    proc = subprocess.Popen(args=exec_list,
                            env=env,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    stdout, _ = proc.communicate()
    return proc.returncode, stdout


def main():
    path_file = sys.argv[1]
    exec_file = sys.argv[2]
    args = sys.argv[3:]
    print(f"exec_file: {exec_file}")
    print(f"path_file: {path_file}")
    print(f"args: {args}")
    return_code, stdout = execute_program([exec_file] + args, read_path_file(path_file))
    print(f"return_code: {return_code}")
    print(stdout.decode(sys.getdefaultencoding()))


if __name__ == "__main__":
    main()
