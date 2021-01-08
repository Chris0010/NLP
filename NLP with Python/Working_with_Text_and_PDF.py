with open('test.txt', mode='a+') as newfile:
    newfile.write('This is a new first line\n'
                  'This line is being appended to test.txt\n'
                  'And another line here.\n'
                  'This is more text being appended to test.txt\n'
                  'And another line here.')
