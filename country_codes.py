from pygal_maps_world import i18n

def get_country_code(country_name):
    for code,name in i18n.COUNTRIES.items():
        if country_name == 'Yemen, Rep.' :
            return 'ye'
        elif country_name == 'Vietnam' :
            return 'vn'
        elif country_name == 'Korea, Dem. Rep.' :
            return 'kp'
        elif country_name == 'Korea, Rep.' :
            return 'kr'
        elif name == country_name:
            return code
    return None

