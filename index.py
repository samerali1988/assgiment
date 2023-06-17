from fnmatch import filter
from os import path
from os.path import isdir, join
from shutil import copytree, rmtree
import glob

src_directory = 'orginal_directory/'
dst_directory = 'new_directory/'

def include_patterns(*patterns):
    def _ignore_patterns(path, names):
        keep = set(name for pattern in patterns
                            for name in filter(names, pattern))
        ignore = set(name for name in names
                        if name not in keep and not isdir(join(path, name)))
        return ignore
    return _ignore_patterns

try:
    get_file_from_each_languages = glob.glob(src_directory + '*-1.txt')
    for file in get_file_from_each_languages:
        language = path.basename(file).split('-', 1)[0]
        if isdir(dst_directory + language + '/'):
            rmtree(dst_directory + language + '/')
        temp_dst_directory = dst_directory + language + '/'
        copytree(src_directory, temp_dst_directory, "false"
                , ignore = include_patterns(language + '-*.txt'))
        print(language + ' files moved to the right directory')
except:
    print("I don't found new files in the source directory")


