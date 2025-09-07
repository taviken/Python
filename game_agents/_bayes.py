
def p_bayes(p_h:float, # The prior
        p_eh:float, # the probability of hypothesis given an event
)->float:
    """
    Runs bayes theorem given the initial probabilty, 
    """
    p_enh = 1- p_h 
    p_nh = 1 - p_eh
    num = p_h * p_eh
    denom = num + (p_nh*p_enh)
    
    return num / denom