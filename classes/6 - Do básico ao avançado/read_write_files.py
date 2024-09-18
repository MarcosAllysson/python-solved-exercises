# read mode
# with open('text.txt', 'r') as file:

#     for line in file.readlines():
#         print(line.title(), end='')
#     print()

#     file.seek(0)  # cursor back to initial
#     print(f'\n{file.read()}')


# write mode
# with open('text.txt', 'w') as file:
#     try:
#         file.write('Writing a new line from function.')
#         file.write(12)
#     except TypeError:
#         print('Insert only letters.')
#     except:
#         print('An error occur, try again later.')

# with open('text.txt', 'r') as file:
#     try:
#         print(file.read())
#     except FileNotFoundError:
#         print('File not found.')
#     except:
#         print('An error occur, try again later.')

with open('new.txt', 'a') as file:
    try:
        message = 'This is a message \nAnother line \nThird line'
        file.write('Writing a in a new file')
        file.write('\n')
        file.write(message)
        file.write('\n')
        file.write('Here goes another string message')
        file.write('\n')
        file.write('With "a" mode, instead of delete everything, it appends the new text at the end')
        file.write('\n')
    except FileNotFoundError:
        print('File not found.')
    except:
        print('An error occur, try again later.')

with open('new.txt', 'r') as file:
    try:
        print(file.read())
    except FileNotFoundError:
        print('File not found.')
    except:
        print('An error occur, try again later.')
