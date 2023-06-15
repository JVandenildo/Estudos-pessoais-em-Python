with open("testOpenFile.txt", "r") as rf:
    for line in rf:  # good for large file
        print(line, end="")

    sizeToRead = 10
    rf_content = rf.read(sizeToRead)
    print(rf_content, end="")

# f.close()  # a must after using the file without a context manager

with open("testWrite.txt", "w") as wf:  # write method overwrites what is in the file
    wf.write("Test!\n2nd line.")
    wf.seek(0)
    wf.write("R")

with open("testOpenFile.txt", "r") as rf:
    with open("testWrite.txt", "w") as wf:
        for line in rf:
            wf.write(line)

# so far r and w works for text not images, rb and wb is for images
