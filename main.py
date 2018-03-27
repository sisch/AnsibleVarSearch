from os import walk, path
import re
import sys
debug_level = 0

searchpath = "./"
variables = dict()


def find_usage():
    var_usage_re = re.compile(r"{{\s*(\S+)\s*}}")
    for root, subdirs, files in walk(path.relpath(searchpath)):
        for file in files:
            # TODO: reduce files to templates/ and *.yml
            DEBUG(root, ":", file)
            with open(path.join(root, file), "r") as f:
                for line in f:
                    for match in var_usage_re.findall(line):
                        if "|" in match:
                            match = match.split("|")[0]
                        variables.setdefault(match, {
                            "usage": [],
                            "declaration": []
                        })
                        p = path.join(root, file)
                        if p not in variables[match]["usage"]:
                            variables[match]["usage"].append(p)
    DEBUG(variables, level=2)


def DEBUG(*args, level=1):
    if debug_level >= level:
        print(args)


def run():
    find_usage()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        searchpath = sys.argv[1]
    debug_level = 2
    run()
