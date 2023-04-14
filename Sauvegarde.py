import xml.etree.ElementTree as ET

def save_to_file(data, filename, file_format):
    if file_format == 'xml':
        root = ET.Element("viscosity_data")
        for index, value in enumerate(data):
            ET.SubElement(root, "measurement", index=str(index), value=str(value))
        tree = ET.ElementTree(root)
        tree.write(filename + '.xml')
    elif file_format == 'txt':
        with open(filename + '.txt', 'w') as f:
            for index, value in enumerate(data):
                f.write('Measurement ' + str(index) + ': ' + str(value) + '\n')
    else:
        print("Invalid file format. Please enter either 'xml' or 'txt'.")

# Example usage:
data = [1.2, 2.1, 3.4, 4.5]
filename = input("Enter a file name: ")
directory = input("Enter a directory path to save the file: ")
file_format = input("Enter a file format (xml or txt): ")

save_to_file(data, directory + '/' + filename, file_format)



