from os import environ

SOAP_11 = "http://schemas.xmlsoap.org/wsdl/soap/"
SOAP_12 = "http://schemas.xmlsoap.org/wsdl/soap12/"
SOAP_ENV_11 = "http://schemas.xmlsoap.org/soap/envelope/"
SOAP_ENV_12 = "http://www.w3.org/2003/05/soap-envelope"

XSI = "http://www.w3.org/2001/XMLSchema-instance"
XSD = "http://www.w3.org/2001/XMLSchema"

WSDL = "http://schemas.xmlsoap.org/wsdl/"
HTTP = "http://schemas.xmlsoap.org/wsdl/http/"
MIME = "http://schemas.xmlsoap.org/wsdl/mime/"

# Default current WSA namespace can be overriden to the old version by the env. var. WSA_NS
if environ.get('WSA_VERSION') == 'V2004.08':
    WSA = "http://schemas.xmlsoap.org/ws/2004/08/addressing"
else:
    WSA = "http://www.w3.org/2005/08/addressing"

DS = "http://www.w3.org/2000/09/xmldsig#"
WSSE = (
    "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
)
WSU = (
    "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
)

NAMESPACE_TO_PREFIX = {XSD: "xsd"}
