import os
import zipfile
import shutil

def get_studentid_and_name(f):
    " ファイル名から学籍番号と名前を抽出"
    l = f.split()
    student_id = l[0]
    name = ' '.join(l[1:-1]) + ' ' + l[-1].split("_")[0]
    return (student_id, name)

def make_ans_dir(parent_dir1, parent_dir2, student_id, name):
    "parent_dir以下にstdent_idとnameを基にディレクトリを作る"
    f1 = "{}_{}_1".format(student_id, name)
    f2 = "{}_{}_2".format(student_id, name)

    if not os.path.exists(parent_dir1 + os.sep + f1):
        os.mkdir(parent_dir1 + os.sep + f1)

    if not os.path.exists(parent_dir2 + os.sep + f2):
        os.mkdir(parent_dir2 + os.sep + f2)

def extract_zip(path_to_zipfile, dst):
    with zipfile.ZipFile(path_to_zipfile) as zip_file:
        for info in zip_file.infolist():
            info.filename = info.filename.encode("cp437").decode("cp932")
            zip_file.extract(info, dst)

if __name__ == "__main__":
    if not os.path.exists("question1"):
        os.mkdir("./" + os.sep + "question1")
    if not os.path.exists("question2"):
        os.mkdir("./" + os.sep + "question2")

    l = os.listdir(".")

    # ディレクトリだけをlに含める
    l = [d for d in l if "19T" in d]

    # question1とquestion2以下に学生のフォルダを作る
    for f in l:
        make_ans_dir("question1", "question2", *(get_studentid_and_name(f)))

    # zipファイルが存在すれば名前以下のフォルダに展開する展開する
    for f in l:
        zip_files = os.listdir(f)
        zip_files = [f_name for f_name in zip_files if ".zip" in f_name]
        if zip_files:
            print(f)
            try:
                extract_zip(os.path.join(f, zip_files[0]), f)
            except UnicodeEncodeError as e:
                print("\n#########################")
                print("文字コードの問題が発生した")
                print("{}に関しては手動で行ってください".format(f))
                print("#########################\n")

    # ファイルをquestion1とquestion2以下にコピーする

    cwd = os.getcwd()

