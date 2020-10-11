import bs4


def GetDescription(response):
    """
    :param response Response
    :return all word translations
    """
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    return [x.text for x in soup.select('.quick-results.container')[0].select('.quick-result-entry .quick-result-overview .sense-group-results a')]


def GetSamples(response, qt):
    """
    :response Response: web response
    :qt Int: How many samples do you want to get
    :return all sentences samples
    """

    soup = bs4.BeautifulSoup(response.text, 'lxml')
    example_list = []

    for example in [
            x.text.split()
            for x in soup.select('.result-block.container .sense-group .dict-entry .more-examples .dict-source')]:
        count = 0
        ret = []
        for x in example:
            if x == 'revisão':
                count = 1
                continue

            if count == 0:
                pass
            else:
                ret.append(
                    x.replace("'", "").replace('"', '').replace(';', '.')
                )
        example_list.append(ret)

    return example_list
