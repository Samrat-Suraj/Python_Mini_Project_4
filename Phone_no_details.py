import requests


def get_phone_number_details(phone_number):
  try:
    # You need to sign up and get an API key from NumVerify (https://numverify.com/)
    api_key = '72ff4c65f44f5351b565d39cc3a6bda4'
    base_url = f'http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}'

    response = requests.get(base_url)
    data = response.json()

    return data

  except Exception as e:
    print("Error:", e)
    return None

ph=int(input("Enter Phone Number Here With Country Code \n"))
user_phone_number = ph

phone_number_details = get_phone_number_details(user_phone_number)

if phone_number_details:
  print("Phone Number Details:")
  for key, value in phone_number_details.items():
    print(f"{key}: {value}")
else:
  print("No details found for the phone number.")