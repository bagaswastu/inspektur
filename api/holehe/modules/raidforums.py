import random

from holehe.localuseragent import ua


async def raidforums(email, client, out):
    name = "Raidforums"
    domain = "raidforums.com"
    method= "register"
    frequent_rate_limit=True

    headers = {
        'User-Agent': random.choice(ua["browsers"]["chrome"]),
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en,en-US;q=0.5',
        'Referer': 'https://raidforums.com/member.php',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://raidforums.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }
    try:
        r = await client.get("https://raidforums.com/member.php", headers=headers)
        if "Your request was blocked" in r.text or r.status_code != 200:
            out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                        "rate_limit": True,
                        "exists": False,
                        "email_recovery": None,
                        "phone_number": None,
                        "others": None})
            return None
    except BaseException:
        out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                    "rate_limit": True,
                    "exists": False,
                    "email_recovery": None,
                    "phone_number": None,
                    "others": None})
        return None

    headers['X-Requested-With'] = 'XMLHttpRequest'

    params = {
        'action': 'email_availability',
    }

    data = {
        'email': email,
        'my_post_key': r.text.split('var my_post_key = "')[1].split('"')[0]
    }

    response = await client.post('https://raidforums.com/xmlhttp.php', headers=headers, params=params, data=data)
    if "Your request was blocked" not in response.text and response.status_code == 200:
        if "email address that is already in use by another member." in response.text:
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
