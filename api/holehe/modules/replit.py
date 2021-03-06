import random

from holehe.localuseragent import ua


async def replit(email, client, out):
    name = "Replit"
    domain = "replit.com"
    method = "register"
    frequent_rate_limit=True

    headers = {
        'User-Agent': random.choice(ua["browsers"]["firefox"]),
        'Accept': 'application/json',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'content-type': 'application/json',
        'x-requested-with': 'XMLHttpRequest',
        'Origin': 'https://replit.com',
        'Connection': 'keep-alive',
    }

    data = '{"email":"' + str(email) + '"}'

    response = await client.post('https://replit.com/data/user/exists', headers=headers, data=data)
    try:
        if response.json()['exists']:
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
    except:
        out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                    "rate_limit": True,
                    "exists": False,
                    "email_recovery": None,
                    "phone_number": None,
                    "others": None})
