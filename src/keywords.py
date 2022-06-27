import xml.etree.ElementTree as ET

def create_keywords(file_name):

    keywords = ["phage tail fiber protein", "tail protein", "receptor-binding tail protein",
            "short tail fibers", "tail fiber protein", "putative tail fiber protein",
            "tailspike protein", "phage tailspike protein", "receptor binding protein",
            "putative receptor-binding protein"]

    k_dict = {k: 0 for k in keywords}

    tree = ET.parse("file_name")
    root = tree.getroot()

    for child in root.iter():
        if child.tag == "hit-def":
            print(child.text)
            for k in keywords:
                if k in child.text.lower():
                    k_dict[k] += 1

