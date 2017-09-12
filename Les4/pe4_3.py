lengte = input('Wat is je lengte?')

def lang_genoeg():
    res = int(lengte) >= int(120)
    return res

if lang_genoeg():
    print('Je bent lang genoeg voor de attractie!')

else:
    print('Helaas je bent te klein!')