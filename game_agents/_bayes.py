def bayes(
    p_h: float,  # The prior
    p_eh: float,  # the probability of hypothesis given an event
    p_enh: float = None,
    p_nh: float = None,
) -> float:
    """
    Runs bayes theorem given the initial probabilty,
    """
    if p_enh is None:
        p_enh = 1 - p_h
    if p_nh is None:
        p_nh = 1 - p_eh
    num = p_h * p_eh
    denom = num + (p_nh * p_enh)

    return num / denom
