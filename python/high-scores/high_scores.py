def latest(scores):
    return scores[len(scores) - 1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    return sorted([x for x in scores], reverse=True) [:3]
