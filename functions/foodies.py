def foods(*foods):
	for food in foods:
		print(f"You want to eat {food}")

foods('rice','yam','kenkey')


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('Dankyi', 'Ben-Oni',
                             location='Amasaman',
                             field='IT',
                             course = 'Computer Science')
print(user_profile)