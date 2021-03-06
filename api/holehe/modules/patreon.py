import random

from holehe.localuseragent import ua


async def patreon(email, client, out):
    name = "Patreon"
    domain = "patreon.com"
    method = "login"
    frequent_rate_limit=True

    headers = {
        'User-Agent': random.choice(ua["browsers"]["chrome"]),
        'Accept': '*/*',
        'Accept-Language': 'en,en-US;q=0.5',
        'Referer': 'https://www.patreon.com/signup?ru=%2Fcreate%3Fru%3D%252Feurope',
        'Content-Type': 'application/vnd.api+json',
        'Origin': 'https://www.patreon.com',
        'DNT': '1',
        'Connection': 'keep-alive',
    }

    params = {
        'json-api-version': '1.0',
        'include': '[]',
    }

    data = '{"data":{"attributes":{"email":"'+email+'"},"relationships":{}}}'
    try:
        response = await client.post('https://www.patreon.com/api/email/available', headers=headers, params=params, data=data)
        if response.json()["data"]["is_available"] == True :
            out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                        "rate_limit": False,
                        "exists": False,
                        "email_recovery": None,
                        "phone_number": None,
                        "others": None})
        else:
            out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                        "rate_limit": False,
                        "exists": True,
                        "email_recovery": None,
                        "phone_number": None,
                        "others": None})
    except :
            out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                        "rate_limit": True,
                        "exists": False,
                        "email_recovery": None,
                        "phone_number": None,
                        "others": None})
