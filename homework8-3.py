def three_files_in_one():
    homework = open("homework.txt", 'a', encoding = 'utf-8')
    txt_1 = open("1.txt", 'r', encoding = 'utf-8')
    txt_2 = open("2.txt", 'r', encoding = 'utf-8')
    txt_3 = open("3.txt", 'r', encoding = 'utf-8')
    txt = [txt_1.read().split('\n'), txt_2.read().split('\n'), txt_3.read().split('\n')]
    txt_filename = ['1.txt', '2.txt', '3.txt']
    len_str = {}
    for ind, txt_ in enumerate(txt):
        len_str.update({len(txt_) : ind })
    for key, value in sorted(len_str.items()):
        x = f'\n{txt_filename[value]} \n{key}\n'
        homework.write(x)
        homework.write('\n'.join(txt[value]))   
    homework.close()
    txt_1.close()
    txt_2.close()
    txt_3.close()
    # is_closed(homework)
    # is_closed(txt_1)
    # is_closed(txt_2)
    # is_closed(txt_3)
three_files_in_one()
