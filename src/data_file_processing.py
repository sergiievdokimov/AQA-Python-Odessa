import os, json, xmltodict
from xml.etree import ElementTree
from utils import get_base_path


def data_file_processing(path_to_source_file, path_to_destination_file):
    if os.path.isfile(path_to_source_file):
        tree = ElementTree.parse(path_to_source_file)
        root = tree.getroot()
        assert check_number_of_elements_containing_text(root, 'YOUR') == 10
        for elem in root.iter():
            if elem.text.startswith('YOUR'):
                elem.text = "MY_VALUE"
        assert check_number_of_elements_containing_text(root, 'YOUR') == 0
        xml_string_for_updated_tree = ElementTree.tostring(root).decode()
        parsed_string = xmltodict.parse(xml_string_for_updated_tree)
        target_json_file = open(path_to_destination_file, 'w')
        target_json_file.write(json.dumps(parsed_string, indent=4))
        target_json_file.close()
        if not os.path.isfile(path_to_destination_file):
            raise FileNotFoundError("Result file isn't created")
    else:
        raise FileNotFoundError("Source file cannot be found by specified path")


def check_number_of_elements_containing_text(root, value):
    number = 0
    for elem in root.iter():
        if elem.text.startswith(value):
            number += 1
    return number


if __name__ == '__main__':
    path_to_data_file = os.path.join(get_base_path(), 'file_samples/xml/test_data.xml')
    path_to_target_file = os.path.join(get_base_path(), 'file_samples/json/updated_test_data.json')
    data_file_processing(path_to_data_file, path_to_target_file)
