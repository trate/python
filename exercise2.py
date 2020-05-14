# exercise 2
# coding=utf-8
name = input("Please enter your name: ")
lastname = input("Please enter your lastname: ")
date_of_birth = input("Please enter your date of birth: ")
city = input("Please enter your home city: ")
email = input("Please enter your e-mail address: ")
phone = input("Please enter your phone number: ")

def user_info(name, lastname, date_of_birth, city, email, phone):
    """User_info - prints user's info

    name: user's name
    lastname: user's last name
    date_of_birth: user's date of the birth
    city: user's home city
    email: user's e-mail address
    phone: user's phone number

    """
    print(f"{name} {lastname}, you were born {date_of_birth} and your home city is {city}. Your e-mail address is {email} and phone number {phone}.")


user_info(name, lastname, date_of_birth, city, email, phone)