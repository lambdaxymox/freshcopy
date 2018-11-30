import sys
import subprocess


def parse_args(args):
    arg_dict = {}
    it = iter(args)
    while True:
        try:
            arg = next(it)
            if arg == 'freshcopy':
                continue
            elif arg == '--permissions':
                flags = next(it)
                arg_dict['permissions'] = flags
            elif arg == '--owner':
                flags = next(it)
                arg_dict['owner'] = flags
            else:
                source = arg
                target = next(it)
                arg_dict['source'] = source
                arg_dict['target'] = target
        except StopIteration:
            break

    return arg_dict


def usage():
    """
    Print out the usage of the script with an example.
    """
    return 'USAGE: freshcopy [--owner <name>] [--permissions <flags>] /path/to/source /path/to/target'


def main():
    if len(sys.argv) != 3:
        print(usage())

        # An exit code of 2 is standard unix convention.
        sys.exit(2)


    args = parse_args(sys.argv[1:])
    print(args)

    sys.exit(0)


if __name__ == 'main':
    main()
else:
    main()
