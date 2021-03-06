import bs4
import requests


def periksa_data(email):
    """
    Check data breach from periksadata.com
    :param email
    :return: dict
    """

    url = 'https://periksadata.com/'
    payload = {
        'email': email,
    }
    response = requests.post(url, data=payload)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    info = soup.select_one('.text-center.col-md-6.col-lg-5 > div > h2')
    if info is not None:
        if info.text == 'WAH SELAMAT!':
            return

    # Get data
    breaches = []
    list = soup.select('div.col-md-6')
    for data in list:
        try:
            img = data.select_one('div > div > img').attrs['src']
            title = data.select_one('div.feature__body > h5').text
            date = data.select_one('div.feature__body > p > b').text
            breached_data = data.select('div.feature__body > p > b')[1].text
            total_breach = data.select('div.feature__body > p > b')[2].text

            breaches.append({
                'img': img,
                'title': title,
                'date': date,
                'breached_data': breached_data,
                'total_breach': total_breach
            })
        except Exception as e:
            pass

    return breaches

