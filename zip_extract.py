import zipfile

with zipfile.ZipFile("test2.zip") as zip_file:
    for info in zip_file.infolist():
        info.filename = info.filename.encode("cp437").decode("cp932")
        zip_file.extract(info)
    # for name in zip_file.namelist():
    #     print(name)
    #     print(name.encode("cp437").decode("cp932"))

    # zip_file.extractall()
