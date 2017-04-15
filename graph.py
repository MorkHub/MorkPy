'''
	graph.py v1.0.1 by Mark Cockburn <mork@themork.co.uk>
'''

sentinel = object()
def draw (data=[],height=10,find=lambda d: d,labels=sentinel):
    if data == []:
        return ''

    if labels is sentinel: labels = [find(x) for x in data]
    string = ''

    largest = 0
    for x in data:
        if find(x) > largest:
            largest = find(x)

    for y in range(height,0,-1):
        for x in range(len(data)):
            if round(find(data[x]) / largest * height) >= y:
                string += '█'*(len(str(labels[x])) if x < len(labels) else 1) + ' '
            else:
                string += ' '*(len(str(labels[x])) if x < len(labels) else 1) + ' '
        string += '\n'

    for label in labels[:len(data)]:
        string += str(label) + ' '
    string += '\n'

    return string
