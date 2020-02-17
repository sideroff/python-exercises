import xml.etree.ElementTree as etree


tree = etree.parse('./feed.xml')

root = tree.getroot()



print('root {}'.format(root))
print('root tag {}'.format(root.tag))

print('root length {}'.format(len(root)))

for child in root:
    print('\troot child {}'.format(child.tag))

print('root atributes {}'.format(root.attrib))

# findall looks at .children NOT RECURSIVLY
print('finding all entry element {}'.format(root.findall(('{http://www.w3.org/2005/Atom}entry'))))

print('finding first entry element {}'.format(root.find('{http://www.w3.org/2005/Atom}entry')))

print('finding first foo element {}'.format(root.find('{http://www.w3.org/2005/Atom}foo')))
