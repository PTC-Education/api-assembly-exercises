def get_ids(url, wv):
    urlArr = url.split("/")
    dIndex = urlArr.index("documents")
    DID = urlArr[dIndex + 1]
    eIndex = urlArr.index("e")
    EID = urlArr[eIndex + 1]
    wvIndex = urlArr.index(wv)
    WVID = urlArr[wvIndex + 1]

    return DID, EID, WVID