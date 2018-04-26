def extract_input_from_json(filename):
    """
    From the original json file downloaded from :
    https://opendata.rapid7.com/sonar.fdns_v2/2018-03-30-1522396861-fdns_aaaa.json.gz

    Ran the following scripts:
    curl --silent https://opendata.rapid7.com/sonar.fdns_v2/2018-03-30-1522396861-fdns_aaaa.json.gz | pigz -dc |
    grep "aaaa" > dns_records_aaaa.json

    On this file, converted it to a name value pair as line files.
    :param filename:File name of the dataset.
    """
    file = open(filename)
    writer = open('dns_name_value.txt', 'w')
    for line in file.readlines():
        tuples = line.strip()[1:-1].split(',')
        name = tuples[1].split('":"')[1][:-1]
        value = tuples[-1].split('":"')[1][:-1]
        writer.write(name + ' ' + value + '\n')
    writer.close()


def get_records_array(filename):
    """
    Get records from array
    :param filename: filename which to read. It must have 'name value' pairs seperated by space.
    :return: Return an array
    """
    records = []
    with open(file=filename) as file:
        for ln in file.readlines():
            records.append(tuple(ln.strip().split(' ')))
    return records
