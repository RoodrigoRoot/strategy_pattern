from functions import get_class_strategy_git
import sys


def choice_git_cloud():
    cloud = input("Ingrese la nube con la que desea trabajar: ")
    if not cloud:
        sys.exit()

    cloud_git = get_class_strategy_git(cloud)

    cloud_git.send_push()
    cloud_git.all_branches()
    cloud_git.all_commits()
    cloud_git.commit_details()
    choice_git_cloud()

if __name__ == '__main__':
    choice_git_cloud()