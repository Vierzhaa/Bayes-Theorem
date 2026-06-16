def bayes(ph,accuracy):
    pnh=1-ph
    f_accuracy = 1-accuracy

    real_pos=ph*accuracy
    false_pos=pnh*f_accuracy

    total_pos=real_pos+false_pos

    r_sick=real_pos/total_pos
    print(f"sick : {r_sick * 100:.2f}%")
    return r_sick

bayes(0.001,0.99)
