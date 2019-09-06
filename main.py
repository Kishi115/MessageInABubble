# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                                 Imports
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# import image_loading
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                              Global Variables
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
greet = '''
Hello! Welcome to the command line. DEBUG MODE!

Debug sets default picture to debug\\img\\09_060.jpg

Select the image you'd like to use (/debug/img/...): '''
image = "debug\\img\\"
parameters = []
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                                   Main
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Greeting user and asking for input and recieving input.
image += input(greet)
print(image)

# Sending data off to the image loader
# image_loading.load(image)
