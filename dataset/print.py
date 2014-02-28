import json

dataset = []
dataset_files = ['dataset_item.json']

for f in dataset_files:
    with open(f) as file:
        for line in file:
            dataset.append(json.loads(file))

for i in range(len(dataset)):
    if 'Continual' == dataset[i]['frequency']:
        print dataset[i]['name']

