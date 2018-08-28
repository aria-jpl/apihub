__version__     = "0.0.1"
__url__         = "http://gitlab.jpl.nasa.gov:8000/browser/trunk/HySDS/hysds"
__description__ = "ApiHub"

def getHandler():
    '''
    Get the handler from this package
    '''
    #Import inside the funtion, to prevent problems loading module
    import apihub.apihub_odata_query
    return apihub.apihub_odata_query.ApiHubODATA()
