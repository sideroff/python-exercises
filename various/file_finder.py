import os

# print( os.path.expanduser('~'))

home_dir = os.path.expanduser('~')

desktop_dir = os.path.join(home_dir, 'Desktop')

# print(desktop_dir)

# print(os.listdir(desktop_dir))


def write_to_file(data):
    f = open('walked.txt', 'w+')
    for line in data:
        f.write(str(line) + '\n')
    f.close()

def find_files_recursive(path: str, wanted_file_extensions: list, excluded_dirs: list):
    dirs = os.listdir(path)
    files = []

    # print(dirs)
    for dir in dirs:
        joined = os.path.join(path, dir)
        if (os.path.isdir(joined) and not any(excluded in joined for excluded in excluded_dirs)):
            # print('path found - ' + dir)
            files.extend(find_files_recursive(
                joined, wanted_file_extensions, excluded_dirs))
        else:
            split_by_dot = dir.split('.')
            if (len(split_by_dot) > 1):
                extension = split_by_dot[-1]
                if (extension in wanted_file_extensions):
                    files.append(joined)

    return files


wanted_file_extensions = ['jpg', 'jpeg', 'png', 'pdf']

excluded_dirs = ['node_modules', 'esoTrace']


# print(any(excluded in 'asdsada\sa\sa\d\dsdsds\\node_modules\\' for excluded in excluded_dirs ))

write_to_file(find_files_recursive(
    desktop_dir, wanted_file_extensions, excluded_dirs))


#print( list(os.walk(desktop_dir)))
