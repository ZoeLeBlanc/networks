import json

def parseData(file):
    with open("{}".format(file), "r") as json_file:
        data = json.load(json_file)
        new_data = dict()
        links = dict()
        nodes = dict()
        each_link = dict()
        each_node = dict()
        final_link = list()
        final_node = list()
        final_dict = dict()
        for each, item in data.items():
            # print(data['links'])
            links = data['links']
            nodes = data['nodes']
            for node in nodes:
                node['Id'] = (float(node['Id']))
                node['ModularityClass'] = (int(node['ModularityClass']))
                each_node[node['Id']] = node
                for link in links:
                    link['Id'] = (float(link['Id']))
                    link['Source'] = (float(link['Source']))
                    link['Target'] = (float(link['Target']))
                    link['Weight'] = (float(link['Weight']))
                    each_link[link['Id']] = link
        # print(each_link)
        for each, item in each_node.items():
            for each, value in each_link.items():
                if item['Id'] == value['Source']:
                    value['Source'] = (str(value['Source']))
                    value['Source'] = item['Label']
                if item['Id'] == value['Target']: 
                    value['Target'] = (str(value['Target']))
                    value['Target'] = item['Label']
                
            
        for each, item in each_node.items():
            item['id'] = item.pop('Label')
            final_node.append(item)
        for each, value in each_link.items():
            value['source'] = value.pop('Source')
            value['target'] = value.pop('Target')
            final_link.append(value)
            
        final_dict['nodes'] = []
        final_dict['nodes'].extend(final_node)
        final_dict['links'] = []
        final_dict['links'].extend(final_link)
        # print(final_dict['links'])
        return final_dict
        json_file.close()


def writeData():
    results = parseData('latest_data.json')
    with open("finalData.json", "w+") as final_file:
        json.dump(results, final_file)
        final_file.close()

writeData()