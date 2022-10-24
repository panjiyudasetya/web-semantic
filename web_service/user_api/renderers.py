from rest_framework_xml.renderers import XMLRenderer


class AddressXMLRenderer(XMLRenderer):
    item_tag_name = "address"
    root_tag_name = "addresses"
