import xml.etree.ElementTree as ET

keywords = ["phage tail fiber protein", "tail protein", "receptor-binding tail protein",
            "short tail fibers", "tail fiber protein", "putative tail fiber protein",
            "tailspike protein", "phage tailspike protein", "receptor binding protein",
            "putative receptor-binding protein"]

k_dict = {k: 0 for k in keywords}

tree = ET.parse("results.xml")
root = tree.getroot()

for child in root.iter():
    if child.tag == "Iteration_query-def":
        print(child.text)
        for k in keywords:
            if k in child.text.lower():
                k_dict[k] += 1

print(k_dict)