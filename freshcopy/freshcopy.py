import sys
import shutil
import pathlib


def parse_args(args):
    """
    Parse the terminal arguments.
    """
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
                src = arg
                dst = next(it)
                arg_dict['src'] = pathlib.Path(source)
                arg_dict['dst'] = pathlib.Path(target)
        except StopIteration:
            break

    return arg_dict


def usage():
    """
    Print out the usage of the script with an example.
    """
    return 'USAGE: freshcopy [--owner <name>] [--permissions <flags>] /path/to/source /path/to/target'


def generate_dst(src, dst):
    """
    Generate a directory in ``dst`` that does not exist yet.
    """
    stem = src.stem
    final_dst = dst.joinpath(stem)
    if not final_dst.exists():
        return final_dst

    i = 1
    while final_dist.exists():
        stem = f'{src.stem} ({i})'
        final_dst = dst.joinpath(stem)
        if not final_dst.exists():
            break

        i += 1

    return final_dst


def copy(src, dst):
    if src == dst:
        raise Exception((src, dst, "Source is identical to destination."))

    if src.exists() and dst.exists():
        if src.is_dir() and dst.is_dir():
            final_dst = generate_dst(src, dst)
            shutil.copytree(src, final_dst)
            
            return final_dst
        elif src.is_file() and dst.is_dir():
            shutil.copy(src, dst)
            
            return dst
        elif src.is_dir() and dst.is_file():
            raise Exception((src, dst, "Cannot copy directory to file."))
        else:
            raise Exception((src, dst, "Cannot copy a file into another file."))            
    else:
        raise Exception((src, dst, "Source or Destination do not exist."))
    

def chown_rec(dst, owner):
    # Verify inputs.
    # Walk the directory and chown.
    pass


def chmod_rec(dst, permissions):
    # Verify inputs.
    # Walk the directory and chmod.
    pass


def main():
    if len(sys.argv) < 3:
        print(usage())

        # An exit code of 2 is standard unix convention.
        sys.exit(2)

    args = parse_args(sys.argv)
    copy(args['src'], args['dst'])
    chown_rec(args['dst'], args['owner'])
    chmod_rec(args['dst'], args['permissions'])

    sys.exit(0)


if __name__ == 'main':
    main()
