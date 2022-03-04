# DSC 510
# Week 12
# Programming Assignment Week 12
# Author Venkata Kanaparthi
# 03/04/2021

# Change#:0
# Change(s) Made: Original Version
# Date of Change: 03/04/2021
# Author: Venkata Kanaparthi
# Change Approved by:
# Date Moved to Production: 03/04/2021


import requests
from requests.exceptions import HTTPError

# Accepting the user choice and validating the input
def validateChoice():
    val = True
    while val:
        try:
           userChoice = input("Would you like to lookup weather data by US City or zip code.\nEnter 1 for US City 2 for zip: ")
           val = False
        except:
            print('The input you entered was not a number. Please enter a valid Number.')
            val = True
    return userChoice

# Accepting the user choice of units and validating the input
def validateUnitsChoice():
    val = True
    while val:
        try:
           userUntChoice = input("Would you like to view temps in Fahrenheit, Celsius, or Kelvin.\nEnter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin: ")
           val = False
        except:
            print('The input you entered was not a String. Please enter a valid value.')
            val = True
    return userUntChoice

# Validating the input choice of City or Zip
def validateInput(userChoice):
    while userChoice != '1' and userChoice != '2':
        userChoice = input("Please enter a valid value to continue. It should be either (1/2):")
    if userChoice == '1' or userChoice == '2':
        valStat = 'S'
    return valStat, userChoice

# Validating the input choice of units for temperature
def validateUntInput(userUntChoice):
    while userUntChoice != 'F' and userUntChoice != 'C' and userUntChoice != 'K':
        userUntChoice = input("Please enter a valid value to continue. It should be either (F/K/C):")
    if userUntChoice == 'F' or userUntChoice == 'C' or userUntChoice == 'K':
        valUntStat = 'S'
    return valUntStat, userUntChoice

# populating weather conditions into variables
def getWeatherCond(option, cityOrZip, userUntChoice):
    errorReason = ''
    city_name = ''
    current_temp = ''
    temp_min = ''
    temp_max = ''
    pressure = ''
    humidity = ''
    description = ''
    if userUntChoice == 'C':
        userUntChoice = "&units=metric"
    elif userUntChoice == 'F':
        userUntChoice = "&units=imperial"
    else:
        userUntChoice = ''
    if option == "q":
        url = "http://api.openweathermap.org/data/2.5/weather?q="+cityOrZip+userUntChoice+"&appid=148bb8b76a45beaba44ab7e607f1229e"
    if option == "zip":
        url = "http://api.openweathermap.org/data/2.5/weather?zip="+cityOrZip+userUntChoice+"&appid=148bb8b76a45beaba44ab7e607f1229e"
    #print(url)
    error = "N"
    try:
        r = requests.get(url)
        r.raise_for_status()
    except HTTPError as http_err:
        #print(f'HTTP error occurred: {http_err}')
        #print(http_err)
        error = "Y"
    except Exception as err:
        #print(f'Other error occurred: {err}')
        error = "O"
        errorReason = 'Connection Error Occured'
    #print(error)
    #print(errorReason)
    if error == 'O':
        #errorReason = err
        print(errorReason)
    else:
        events = r.json()
        #print(type(events['main']))
        if error == 'Y':
            for key, value in events.items():
                if key == 'message':
                    errorReason = value
                    #print(errorReason)
        else:
            city_name = events['name']
            #print(city_name)
            for weathercond in events['main']:
                #print(events['main'][weathercond])
                if weathercond == 'temp':
                    current_temp = events['main'][weathercond]
                    #print(current_temp)
                if weathercond == 'temp_min':
                    temp_min = events['main'][weathercond]
                    #print(temp_min)
                if weathercond == 'temp_max':
                    temp_max = events['main'][weathercond]
                    #print(temp_max)
                if weathercond == 'pressure':
                    pressure = events['main'][weathercond]
                    #print(pressure)
                if weathercond == 'humidity':
                    humidity = events['main'][weathercond]
                    #print(humidity)
            for weathercond in events['weather']:
                #print(weathercond)
                for details in weathercond:
                    #print(details)
                    if details == 'description':
                        #print(weathercond[details])
                        description = weathercond[details]
                        #print(description)
    return city_name, current_temp, temp_min, temp_max, pressure, humidity, description, errorReason

# Printing the weather data
def prntFormat(city_name, current_temp, temp_min, temp_max, pressure, humidity, description, errorReason):
    if errorReason == '':
        print('-'*50)
        print('Current Weather Conditions For {:11}'.format(city_name).title())
        print('-'*50)
        print('Current Temp     :{:11} degress'.format(current_temp))
        print('High Temp        :{:11} degress'.format(temp_min))
        print('Low Temp         :{:11} degress'.format(temp_max))
        print('Pressure         :{:11} hpa'.format(pressure))
        print('Humidity         :{:11} %'.format(humidity))
        print('Cloud Cover      :{:>16} '.format(description).title())
        print('-'*50)
    else:
        print('-'*50)
        print('Error Reason     :{:>16} '.format(errorReason).title())
        print('-'*50)

# Validate the input to check whether the retry option provided is valid or not
def validateContInput(operation):
    while operation != 'Y' and operation != 'N' and operation != 'y' and operation != 'n':
        operation = input("Please enter a valid value to continue. It should be either (Y/y/N/n):")
    if operation == 'Y' or operation == 'N' or operation == 'y' or operation == 'n':
        valContStat = 'S'
    return valContStat, operation

# Main function which will call the weather function with the values provided by user
def processinglogic(valStat,userChoice):
    if valStat == "S":
        #print(0)
        if userChoice == '1':
            #print(1)
            option = "q"
            #print(2)
            cityName = input("Please enter the City Name: ")
            userUntChoice = validateUnitsChoice()
            valUntStat, userUntChoice = validateUntInput(userUntChoice)
            if valUntStat == "S":
                city_name, current_temp, temp_min, temp_max, pressure, humidity, description, errorReason=getWeatherCond(option, cityName, userUntChoice)
        elif userChoice == '2':
            option = "zip"
            zipCode = input("Please enter the Zip Code: ")
            userUntChoice = validateUnitsChoice()
            valUntStat, userUntChoice = validateUntInput(userUntChoice)
            if valUntStat == "S":
                city_name, current_temp, temp_min, temp_max, pressure, humidity, description, errorReason=getWeatherCond(option, zipCode, userUntChoice)
    return city_name, current_temp, temp_min, temp_max, pressure, humidity, description, errorReason


# Initialising Welcome Message to Customer
welcomeMsg = 'Welcome to the Weather App!'
# Displaying Welcome Message to Customer
print(welcomeMsg)
userChoice = validateChoice()
valStat, userChoice = validateInput(userChoice)
city_name, current_temp, temp_min, temp_max, pressure, humidity, description, errorReason = processinglogic(valStat,userChoice)
prntFormat(city_name, current_temp, temp_min, temp_max, pressure, humidity, description, errorReason)
# Asking the Customer to provide whether to continue or not
operation = input("Would you like to perform another weather lookup? (Y/y/N/n):")
valContStat, operation = validateContInput(operation)
if valContStat == 'S':
    itr = 1
    # Checking for Sentinel value to break the while loop
    while operation != 'N' and operation != 'n':
        if valContStat == 'S' and (operation == 'Y' or operation == 'y'):
            if itr == 1:
                #print(5)
                userChoice = validateChoice()
                valStat, userChoice = validateInput(userChoice)
                city_name, current_temp, temp_min, temp_max, pressure, humidity, description, errorReason = processinglogic(valStat,userChoice)
                prntFormat(city_name, current_temp, temp_min, temp_max, pressure, humidity, description, errorReason)
            operation = 'N'
            # Asking the Customer to provide whether to continue or not
            operation = input("Would you like to perform another weather lookup? (Y/y/N/n):")
            valContStat, operation = validateContInput(operation)
            if valContStat == 'S' and (operation == 'Y' or operation == 'y'):
                userChoice = validateChoice()
                valStat, userChoice = validateInput(userChoice)
                city_name, current_temp, temp_min, temp_max, pressure, humidity, description , errorReason= processinglogic(valStat,userChoice)
                prntFormat(city_name, current_temp, temp_min, temp_max, pressure, humidity, description, errorReason)
                itr = 2

