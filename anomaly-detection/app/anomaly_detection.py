from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import normalize

def getOutliers(data, neighbors):
    if len(data) > neighbors:
        lof = LocalOutlierFactor(n_neighbors=neighbors)
        X = normalize(data)
        return set([idx for idx, e in enumerate(lof.fit_predict(X)) if e < 0])
    return set()
