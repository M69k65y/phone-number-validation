import phonenumbers

evaluate_loop = True
country_code = None
prompt_input = True

while evaluate_loop:
    if prompt_input:
        # Prompt the user to enter a phone number.
        phone_number = input("Enter a phone number: ")

    try:
        parsed_number = phonenumbers.parse(phone_number, country_code)
        evaluate_loop = False
    
    except phonenumbers.phonenumberutil.NumberParseException as e:
        # Error type 0 is raised when a number is provided without
        # the country code and a default country short code (e.g. US, DE, FR)
        # is not provided.
        if e.error_type == 0:
            # Ensure that the country short code entered by the user is in
            # upper case
            country_code = str(
                input("Enter the country short code: ")
            ).upper()

            # Set the value of prompt_input to False to ensure that the
            # original phone_number value is not overritten as the loop
            # is evaluated again.
            prompt_input = False

        # Error type 1 is raised when the parsed value is not a number.
        elif e.error_type == 1:
            print(e._msg)

# Check if phone number is valid.
is_valid = phonenumbers.is_valid_number(parsed_number)

if is_valid:
    print(phone_number + " is a valid phone number.")

    formatted_output = input(
        "Print the formatted number? Y/N: "
    )

    if formatted_output.lower() == "y":
        print(
            "National: ",
            phonenumbers.format_number(
                parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL
            )
        )
        print(
            "International: ",
            phonenumbers.format_number(
                parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL
            )
        )
        print(
            "E164: ",
            phonenumbers.format_number(
                parsed_number, phonenumbers.PhoneNumberFormat.E164
            )
        )

else:
    print(phone_number + " is an invalid phone number.")
