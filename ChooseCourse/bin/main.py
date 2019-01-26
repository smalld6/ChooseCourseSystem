#_author: 11013
#date: 2019/1/25
import os
import sys
BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
print(sys.path)
from core import school_view
from core import student_view
from core import teacher_view
def main():
    choice=input('请选择角色:0 学校 1教师 2 学生')
    if choice=='0':
        school_view.run()
    elif choice=='1':
        teacher_view.run()
    elif choice=='2':
        student_view.run()
    else:
        print('输入错误')
if __name__=='__main__':
    main()