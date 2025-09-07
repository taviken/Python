
def bayes(p_initial:float,
        p_event_true:float,
        p_event_false:float,
        p_not_event:float):
    p_H_p_eh = p_initial * p_event_true
    p_nH_p_enh = p_not_event * p_event_false
    
    return p_H_p_eh / (p_H_p_eh + p_nH_p_enh)