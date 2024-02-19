import sklearn as sk

def getOutliers(data):
    lof = sk.neighbor.LocalOutlierFactor()
    return [idx for idx, e in enumerate(lof.fit_predict(data)) if e < 0]
