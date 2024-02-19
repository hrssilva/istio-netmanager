from sklearn.neighbors import LocalOutlierFactor

def getOutliers(data, neighbors):
    if data.len > neighbors:
        lof = LocalOutlierFactor(n_neighbors=neighbors)
        return set([idx for idx, e in enumerate(lof.fit_predict(data)) if e < 0])
    return set()
