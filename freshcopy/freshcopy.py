import sys
import shutil


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


copy_source_to_target(source, target):
    pass

chown_rec(target, owner):
    pass

chmod_rec(target, permissions):
    pass


def main():
    if len(sys.argv) < 3:
        print(usage())

        # An exit code of 2 is standard unix convention.
        sys.exit(2)

    args = parse_args(sys.argv[1:])
    copy_source_to_target(args['source'], args['target'])
    chown_rec(args['target'], args['owner'])
    chmod_rec(args['target'], args['permissions'])    

    sys.exit(0)


if __name__ == 'main':
    main()
