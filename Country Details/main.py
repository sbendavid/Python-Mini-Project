from countryinfo import CountryInfo

country = CountryInfo(input("Enter Country Name: "))

# Get country details

print(f"Country Name: {country.name()}")
print(f"Capital: {country.capital()}")
print(f"Population: {country.population()}")
print(f"Area (in square kilometers): {country.area()}")
print(f"Currency: {country.currencies()}")
print(f"Languages: {country.languages()}")
print(f"Region: {country.region()}")
print(f"Subregion: {country.subregion()}")
print(f"Demonym: {country.demonym()}")
print(f"Borders: {country.borders()}")
