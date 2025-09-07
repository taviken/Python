from .._bayes import p_bayes

def test_bayes():
    prob_of_disease = 1/1000 # prior
    prob_test_is_correct = 99/100

    res = p_bayes(p_h = prob_of_disease,
            p_eh= prob_test_is_correct,)
    percent = res *100

    assert round(percent,2) == 9.02

    # take second test
    new_prob = res


    new_res = p_bayes(p_h = new_prob,
            p_eh= prob_test_is_correct,)
    percent = new_res *100

    assert round(percent,2) == 90.75