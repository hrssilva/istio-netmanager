from sklearn.neighbors import LocalOutlierFactor

def getOutliers(data):
    lof = LocalOutlierFactor()
    return set([idx for idx, e in enumerate(lof.fit_predict(data)) if e < 0])
