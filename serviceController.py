from serviceModel import Service

service = Service()


def createService(serviceData):
    return offer.createService(serviceData)


def getAllService():
    return offer.getAllService()


def updateService(serviceData):
    return offer.updateService(serviceData)


def activateService(serviceData):
    return offer.handleActivateService(serviceData)


def deleteService(offerId):
    return offer.deleteService(offerId)
