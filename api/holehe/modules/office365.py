import random
import string


async def office365(email, client, out):
    name = "office365"
    domain = "office365.com"
    method = "other"
    frequent_rate_limit=False

    user_agent = 'Microsoft Office/16.0 (Windows NT 10.0; Microsoft Outlook 16.0.12026; Pro)'
    headers = {'User-Agent': user_agent, 'Accept': 'application/json'}
    def get_random_string(length):
        letters = string.digits
        result_str = ''.join(random.choice(letters) for i in range(length))
        return(result_str)
    r = await client.get(
        'https://outlook.office365.com/autodiscover/autodiscover.json/v1.0/{}?Protocol=Autodiscoverv1'.format(
            get_random_string(30)+"@"+email.split('@')[1]),
        headers=headers,
        allow_redirects=False)
    if r.status_code != 200:
        r = await client.get(
            'https://outlook.office365.com/autodiscover/autodiscover.json/v1.0/{}?Protocol=Autodiscoverv1'.format(
                email),
            headers=headers,
            allow_redirects=False)
        if r.status_code == 200:
            out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                        "rate_limit": False,
                        "exists": True,
                        "email_recovery": None,
                        "phone_number": None,
                        "others": None})
        else:
            out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                        "rate_limit": False,
                        "exists": False,
                        "email_recovery": None,
                        "phone_number": None,
                        "others": None})
    else:
        out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                    "rate_limit": True,
                    "exists": False,
                    "email_recovery": None,
                    "phone_number": None,
                    "others": None})
