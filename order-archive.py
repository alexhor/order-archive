import os, re

folders = []

# go through the current directory and scan for folders
for dirname, dirnames, filenames in os.walk('.'):
    folder = dirname[2:]
    # skip parent directory
    if folder == '':
        continue
    # add the folder to the list
    folders.append(folder)

# create a folder for all unkown files
try:
    os.mkdir('special')
except OSError:
    pass

# go through every folder
for folder in folders:
    # create special direcotry
    try:
        os.mkdir('special/' + folder)
    except OSError:
        pass
    # get all files
    files = os.listdir(folder)

    # go through every file
    for file in files:
        # get the date from the fielename
        match = re.search('(20[0-2][0-9])\.([0-1]?[0-9])\.([0-3]?[0-9])', file)
        # no match found, so move to special folder
        if match is None:
            os.rename(folder + '/' + file, 'special/' + folder + '/' + file)
            continue
        # generate the dates folders name
        new_folder = folder + '/' + match.group(1) + '-' + match.group(2) + '-' + match.group(3)
        # create the dates folder
        try:
            os.mkdir(new_folder)
        except OSError:
            pass
        # move the file to the new folder
        os.rename(folder + '/' + file, new_folder + '/' + file)
