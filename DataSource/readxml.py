from xml.etree import ElementTree as ET


class read_xml():

    def read_tag_attribute_from_xml(doc_location, requested_tag):
        document = ET.parse(doc_location)
        root = document.getroot()
        url_tag = root.find(requested_tag)
        data = url_tag.get('path')
        return data

    def read_tag_text_from_xml(doc_location,section, requested_tag):

        document = ET.parse(doc_location)
        root = document.getroot()
        for customer in root.findall('customer'):
            for section in customer.findall(section):
               tag_text = section.find(requested_tag).text
        return tag_text