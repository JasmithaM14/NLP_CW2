import xml.etree.ElementTree as ET

def split_xml(input_file, output_dir, articles_per_file):
    # Parse the input XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Create the root element for the new XML files
    articles_tag = root.tag
    article_tag = root[0].tag

    total_articles = len(root)
    num_files = (total_articles // articles_per_file) + (1 if total_articles % articles_per_file != 0 else 0)

    for i in range(num_files):
        # Create a new XML root
        new_root = ET.Element(articles_tag)

        # Add articles to the new XML root
        for article in root[i * articles_per_file: (i + 1) * articles_per_file]:
            new_root.append(article)

        # Write the new XML file
        new_tree = ET.ElementTree(new_root)
        new_tree.write(f"{output_dir}/split_{i+1}.xml", encoding='utf-8', xml_declaration=True)

    print(f"Split into {num_files} files.")

# Example usage
input_file = r'C:\NLP_CW2\INPUT\SPLITS\GROUNDTRUTH\ground-truth-validation-bypublisher-20181122\split_1.xml'
output_dir = r'C:\NLP_CW2\OUTPUT\1500\groundtruth_validation_bypublisher'
articles_per_file = 1500  # Adjust this number based on your memory capacity

split_xml(input_file, output_dir, articles_per_file)