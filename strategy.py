from abc import ABC, abstractmethod


class CloudGitAbstrac(ABC):

    @abstractmethod
    def send_push(self):
        ...

    @abstractmethod
    def all_commits(self):
        ...

    @abstractmethod
    def commit_details(self):
        ...

    @abstractmethod
    def all_branches(self):
        ...


class GitHubCloud(CloudGitAbstrac):

    def send_push(self):
        print("Enviando push a GitHub")

    def all_commits(self):
        print("Todas los commits de GitHub")

    def commit_details(self):
        print("Detalles del últimos commit de GitHub")

    def all_branches(self):
        print("Todas las ramas de GitHub")


class GitLabCloud(CloudGitAbstrac):

    def send_push(self):
        print("Enviando push a GitLab")

    def all_commits(self):
        print("Todas los commits de GitLab")

    def commit_details(self):
        print("Detalles del últimos commit de GitLab")

    def all_branches(self):
        print("Todas las ramas de GitLab")


class BitBucketCloud(CloudGitAbstrac):

    def send_push(self):
        print("Enviando push a BitBucket")

    def all_commits(self):
        print("Todas los commits de BitBucket")

    def commit_details(self):
        print("Detalles del últimos commit de BitBucket")

    def all_branches(self):
        print("Todas las ramas de BitBucket")
