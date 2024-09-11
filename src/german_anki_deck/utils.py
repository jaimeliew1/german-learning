def int_to_german_spelling(number):
    # Define the German words for numbers 0-19
    ones = [
        "null",
        "ein",
        "zwei",
        "drei",
        "vier",
        "fünf",
        "sechs",
        "sieben",
        "acht",
        "neun",
        "zehn",
        "elf",
        "zwölf",
        "dreizehn",
        "vierzehn",
        "fünfzehn",
        "sechzehn",
        "siebzehn",
        "achtzehn",
        "neunzehn",
    ]

    # Define the German words for multiples of 10
    tens = [
        "",
        "",
        "zwanzig",
        "dreißig",
        "vierzig",
        "fünfzig",
        "sechzig",
        "siebzig",
        "achtzig",
        "neunzig",
    ]

    # Convert the number to a string and split it into digits
    digits = [int(d) for d in str(number)]

    # Handle special cases for numbers 0-19
    if number == 1:
        return "eins"

    if number < 20:
        return ones[number]

    # Handle numbers between 20 and 99
    elif number < 100:
        if digits[1] == 0:
            return tens[digits[0]]
        else:
            return ones[digits[1]] + "und" + tens[digits[0]]

    # Handle numbers between 100 and 999
    elif number < 1000:
        if digits[1] == 0 and digits[2] == 0:
            return ones[digits[0]] + "hundert"
        else:
            return (
                ones[digits[0]] + "hundert" + ones[digits[1]] + "und" + tens[digits[0]]
            )
    # Handle numbers between 1000 and 999999
    elif number < 1000000:
        if digits[1] == 0 and digits[2] == 0 and digits[3] == 0:
            return ones[digits[0]] + "tausend"
        else:
            return (
                ones[digits[0]]
                + "tausend"
                + int_to_german_spelling(
                    int(str(digits[1]) + str(digits[2]) + str(digits[3]))
                )
            )

    # Handle numbers larger than 999999
    else:
        return "Number too large to spell in German"


if __name__ == "__main__":
    for i in range(0, 101):
        print(i, int_to_german_spelling(i))
