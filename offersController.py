from offersModel import Offer

offer = Offer()


def createOffer(offerData):
    return offer.createOffer(offerData)


def getAllOffers():
    return offer.getAllOffers()


def updateOffer(offerData):
    return offer.updateOffer(offerData)


def activateOffer(offerData):
    return offer.handleActivateOffer(offerData)


def deleteOffer(offerId):
    return offer.deleteOffer(offerId)
