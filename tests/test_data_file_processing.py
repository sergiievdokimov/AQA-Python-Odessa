from xml.etree import ElementTree

from src.data_file_processing import data_file_processing
import pytest
import json
import filecmp
import os
from utils import get_base_path

path_to_data_file = os.path.join(get_base_path(), 'file_samples/xml/test_data.xml')
path_to_target_file = os.path.join(get_base_path(), 'file_samples/json/updated_test_data.json')
path_to_result_template_file = os.path.join(get_base_path(), 'file_samples/json/result_file_template.json')
wrong_path = os.path.join(get_base_path())
path_to_xml_for_comparison = os.path.join(get_base_path(), 'file_samples/xml/updated_data.xml')


def test_valid_file_processing_and_content_of_result_file():
    data_file_processing(path_to_data_file, path_to_target_file)
    with open(path_to_target_file, 'r') as file1:
        data1 = json.load(file1)
    with open(path_to_result_template_file, 'r') as file2:
        data2 = json.load(file2)
    assert data1 == data2


def test_invalid_path_to_source_file():
    with pytest.raises(FileNotFoundError):
        data_file_processing(wrong_path, path_to_target_file)


def test_original_xml_content_is_correct():
    tree = ElementTree.parse(path_to_data_file)
    root = tree.getroot()
    xml_string = ElementTree.tostring(root).decode()
    serialized_xml_file = open(path_to_xml_for_comparison, 'w')
    serialized_xml_file.write(xml_string)
    return filecmp.cmp(path_to_data_file,
                       path_to_xml_for_comparison)
