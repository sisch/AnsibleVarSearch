from os import walk, path
import re
import sys
debug_level = 0

searchpath = "./"
variables = dict()


def find_vars():
    var_usage_re = re.compile(r"{{\s*(\S+)\s*}}")
    var_declaration_re = re.compile(r'"[^"]+"|(\w+):')
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
                    for match in var_declaration_re.findall(line):
                        variables.setdefault(match, {
                            "usage": [],
                            "declaration": []
                        })
                        p = path.join(root, file)
                        if p not in variables[match]["declaration"]:
                            variables[match]["declaration"].append(p)

    DEBUG(variables, level=2)


def print_markdown():
    for var in variables.keys():
        if not variables[var]["usage"]:
            continue
        print("## ", var)
        print("### Usage")
        for u in variables[var]["usage"]:
            print("* ", u)
        print()
        print("### Declaration")
        for d in variables[var]["declaration"]:
            print("* ", d)
        print()


def DEBUG(*args, level=1):
    if debug_level >= level:
        print(args, file=sys.stderr)


def run():
    find_vars()
    print_markdown()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        searchpath = sys.argv[1]
    debug_level = 2
    run()
