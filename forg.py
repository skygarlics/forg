from chosung import chosung
import re
import sys
import os
import shutil

def searchFile(dirname, func, *args, recur = 0):
    """search for file and do something.
    """
    files = os.listdir(dirname)
    for file in files:
        fullpath = os.path.join(dirname, file)
        if os.path.isfile(fullpath):
            func(file, *args)
        elif recurr and os.path.isdir(fullpath):
            searchfile(dirname, 1)

def organizeFile(filename, dir_from, dir_to):
    """organize file to folder by its name
    """
    fname, ext = splitExt(filename)
    if ext in ['txt', 'TXT']:
        typ = 'TXT'
    else:
        typ = 'SCAN'

    name = normalizeName(fname)

    cho = chosung(name[0])
    if cho not in u'ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ':
        cho = 'A~9'

    # make directory
    to_new = os.path.join(dir_to, cho, name, typ)
    if not os.path.isdir(to_new):
        os.makedirs(to_new)

    # move file
    shutil.move(os.path.join(dir_from, filename), to_new)

def normalizeName(name):
    """nomalize novel's name
    """
    # remove author...maybe
    title_l = name.split(' - ')
    if len(title_l) == 1:
        title = title_l[0]
    else:
        title = ' - '.join(title_l[:-1])
        if len(title_l) > 2:
            notifyMistake(name, title)

    # remove series number
    title_exp = re.compile('^(.*?)(\d+)(\D*)$')
    match = title_exp.match(title)
    if match and (match.group(3) in ['', u'권', u'券']):
        title = match.group(1)

    # remove illegal characters
    title = re.sub('[\/:*?"<>|]', '', title)
    if '+' in title:
        tmp = title
        title.replace('+', ' ')
        notifyMistake(tmp, title)

    return title.strip()

def notifyMistake(before, after):
    """notify possible mistake
    """
    print('It can be mistake :')
    print('before: {}'.format(before))
    print('after : {}\n'.format(after))

def splitExt(filename):
    """split filename to [name, extension]
    """
    split = filename.split('.')
    return [''.join(split[:-1]),split[-1]]

def main():
    argc = len(sys.argv)

    if (argc < 2) or (argc > 3):
        print("usage: forg source [dest]")
    else:
        dir_from = sys.argv[1]
        if argc == 2:
            dir_to = dir_from
        else:
            dir_to = sys.argv[2]
        searchFile(dir_from, organizeFile, dir_from, dir_to)

if __name__=='__main__':
    main()