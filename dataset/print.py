import json

with open('dataset_item.json') as dataset_file:
    dataset = json.load(dataset_file)

for i in range(len(dataset)):
    if 'Continual' == dataset[i]['frequency']:
        print dataset[i]['name']

