import xml.etree.ElementTree as ET


def parse_metadata(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    caption_map = {}
    calc_map = {}

    for col in root.iter("column"):
        name = col.get("name", "").strip("[]")
        caption = col.get("caption", "")
        datatype = col.get("datatype", "string")

        if name and caption:
            caption_map[name] = caption

        calc = col.find("calculation")
        if calc is not None:
            formula = calc.get("formula", "")
            calc_map[caption or name] = {
                "formula": formula,
                "datatype": datatype
            }

    return caption_map, calc_map
