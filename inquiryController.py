from customerInquiries import Inquiry

inquiry = Inquiry()


def createInquiry(inquiryData):
    return inquiry.createInquiry(inquiryData)


def getAllInquiries():
    return inquiry.getAllInquiries()


def sendInquiryReply(data):
    return inquiry.sendInquiryReply(data)
