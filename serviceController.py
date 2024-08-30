from serviceModel import Service

service = Service()


def createService(serviceData):
    return service.createService(serviceData)


def getAllService():
    return service.getAllServices()


def updateService(serviceData):
    return service.updateService(serviceData)


def activateService(serviceData):
    return service.handleActivateService(serviceData)


def deleteService(offerId):
    return service.deleteService(offerId)
