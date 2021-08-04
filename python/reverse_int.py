import sys
def reverseInt(integer):
    reverse = ''
    for i in str(integer):
        reverse += str(integer)[:-1]
    print(reverse)
# try:
integer = 321
reverse_int = reverseInt(integer)
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise