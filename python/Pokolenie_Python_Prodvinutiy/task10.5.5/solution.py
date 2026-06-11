def add_query_string(url, query):
    url_text = url

    if len(query) == 0:
        return url
    else:
        url_text += '?'
        for key, value in query.items():
            url_text += key + '=' + str(value) +'&'

    return url_text[:len(url_text) - 1]