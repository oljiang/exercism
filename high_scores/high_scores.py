def latest(scores):
    return scores[-1]


def personal_best(scores):
    return sorted(scores, key=None, reverse=True)[0]


def personal_top_three(scores):
    return sorted(scores, key=None, reverse=True)[:3]
