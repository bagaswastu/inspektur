import hashlib


async def gravatar(email, client, out):
    name = "Gravatar"
    domain = "en.gravatar.com"
    method="other"
    frequent_rate_limit=False

    hashed_name = hashlib.md5(email.encode()).hexdigest()
    r = await client.get(f'https://en.gravatar.com/{hashed_name}.json')
    if r.status_code != 200:
        out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                    "rate_limit": False,
                    "exists": False,
                    "email_recovery": None,
                    "phone_number": None,
                    "others": None})
        return None
    else:
        try:
            data = r.json()
            FullName = data['entry'][0]['displayName']

            others = {
                'FullName': str(FullName)+" / "+str(data['entry'][0]["profileUrl"]),
            }

            out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                        "rate_limit": False,
                        "exists": True,
                        "email_recovery": None,
                        "phone_number": None,
                        "others": others})
            return None
        except BaseException:
            out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                        "rate_limit": True,
                        "exists": False,
                        "email_recovery": None,
                        "phone_number": None,
                        "others": None})
            return None
