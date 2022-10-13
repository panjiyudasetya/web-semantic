from rest_framework_xml.renderers import XMLRenderer


class UserXMLRenderer(XMLRenderer):
    item_tag_name = "user"
    root_tag_name = "users"
