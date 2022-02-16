def parse_input(data, method=None):
    data = list(map(lambda x: x.strip().lower(), data.split(',')))
    if method == 'POST':
        item = {'name': None, 'type': None, 'count': None}
        if len(data) == 1:
            item['name'] = data[0]
            return item
        if len(data) == 2:
            item['name'] = data[0]
            if data[1].isdigit():
                item['count'] = int(data[1])
            else:
                item['type'] = data[1]
            return item
        item['name'] = data[0]
        item['type'] = data[1]
        item['count'] = int(data[2])
        return item
    return data
