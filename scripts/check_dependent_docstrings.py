import argparse

CLI=argparse.ArgumentParser()
CLI.add_argument(
    "--files",
    nargs=1,
    type=str,
    default=""
)


def interesting_files(args):
    files = args.files[0].split()
    probably_cryptol = lambda f: f.endswith(".cry") \
        or f.endswith(".tex") \
        or (f.endswith(".md") and not f.endswith("README.md"))
    return filter(probably_cryptol, files)


args = CLI.parse_args()

files = interesting_files(args)
print("%r" % args.files)

