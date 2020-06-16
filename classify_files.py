import os
import shutil

def get_studentid_and_name(f):
    " ファイル名から学籍番号と名前を抽出"
    l = f.split()
    student_id = l[0]
    name = ' '.join(l[1:-1]) + ' ' + l[-1].split("_")[0]
    return (student_id, name)

def make_ans_dir(parent_dir, student_id, name):
    "parent_dir以下にstdent_idとnameを基にディレクトリを作る"
    f1 = "{}_{}_1".format(student_id, name)
    f2 = "{}_{}_2".format(student_id, name)

    if not os.path.exists(parent_dir + os.sep + f1):
        os.mkdir(parent_dir + os.sep + f1)

    if not os.path.exists(parent_dir + os.sep + f2):
        os.mkdir(parent_dir + os.sep + f2)

if __name__ == "__main__":

    print("###################################")
    
    if not os.path.exists("question1"):
        os.mkdir("./" + os.sep + "question1")
    if not os.path.exists("question2"):
        os.mkdir("./" + os.sep + "question2")

    l = os.listdir(".")
    # ディレクトリだけをlに含める
    l = [d for d in l if "19T" in d]
    for f_name in l:
        print(get_studentid_and_name(f_name))
    # for f in l:
    #     make_ans_dir(f, *(get_studentid_and_name(f)))
    
    # ファイルが一つだけ存在する場合
    # この場合にはそれをそれぞれのファイルをコピーする

    cwd = os.getcwd()


    print("###################################")
