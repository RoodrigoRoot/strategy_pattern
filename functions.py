from strategy import CloudGitAbstrac, GitHubCloud, GitLabCloud, BitBucketCloud


def get_class_strategy_git(option: str) -> CloudGitAbstrac:

    dict_git = {
        'hub': GitHubCloud(),
        'lab': GitLabCloud(),
        'bit': BitBucketCloud(),
    }

    return dict_git[option]

