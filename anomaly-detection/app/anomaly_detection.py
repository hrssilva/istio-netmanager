import sklearn as sk

def getOutliers(data):
    lof = sk.neighbor.LocalOutlierFactor()
    return set([idx for idx, e in enumerate(lof.fit_predict(data)) if e < 0])
