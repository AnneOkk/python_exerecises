def city_func(city, country, when=''):
    if when:
        city_country = (f"{city.title()} is in {country.title()}. I will visit it in {when.title()}.")
    else:
        city_country = (f"{city.title()} is in {country.title()}.")
    return city_country



