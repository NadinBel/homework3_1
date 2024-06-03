def single_root_words(root_world, *other_words):
    same_words = []
    for i in other_words:
        if root_world.lower() in i.lower() or i.lower() in root_world.lower():
            same_words.append(i)
    return(same_words)
print(single_root_words('rich', 'richest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))


def single_root_words(root_world, *other_words):
    same_words = []
    for i in other_words:
        if root_world.lower().count(i.lower()) or i.lower().count(root_world.lower()):
            same_words.append(i)
    return(same_words)
print(single_root_words('rich', 'richest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))