def metadata_sum(data):
    data_sum_combined = 0
    child_nodes = int(data[0])
    metadata_entries = int(data[1])
    data = data[2:]

    for i in range(child_nodes):
        data_sum, data = metadata_sum(data)
        data_sum_combined += data_sum

    for i in data[:metadata_entries]:
        data_sum_combined += int(i)

    return data_sum_combined, data[metadata_entries:]


def metadata_value(data):
    data_sum_combined = 0
    child_nodes = int(data[0])
    metadata_entries = int(data[1])
    data = data[2:]
    values_of_children = []

    for i in range(child_nodes):
        data_sum, data = metadata_value(data)
        values_of_children.append(data_sum)
        print(values_of_children)
    if child_nodes == 0:
        for i in data[:metadata_entries]:
            data_sum_combined += int(i)
    else:
        for i in data[:metadata_entries]:
            if 0 < int(i) <= child_nodes:
                print("meta: " + i)
                print(values_of_children[int(i)-1])
                data_sum_combined += values_of_children[int(i)-1]
    return data_sum_combined, data[metadata_entries:]


f = open("input8.txt", "r")
d = f.read().split(" ")

licence = metadata_sum(d)[0]
print("license is: " + str(licence))

licence = metadata_value(d)[0]
print(licence)
