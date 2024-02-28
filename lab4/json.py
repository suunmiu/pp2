
import json

# Load data from the JSON file
with open('sample-data.json', 'r') as file:
    data = json.load(file)

# Print the header
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Iterate through the interfaces and print relevant information
for interface in data['interfaces']:
    dn = interface.get('DN', '')
    description = interface.get('Description', 'inherit')
    speed = interface.get('Speed', 'inherit')
    mtu = interface.get('MTU', 'inherit')

    print("{:<50} {:<20} {:<10} {:<6}".format(dn, description, speed, mtu))
