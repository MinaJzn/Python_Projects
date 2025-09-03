UNDER_20 = [
    "Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine",
    "Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen",
]

TENS = [
    "","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"
]

ABOVE_100 = {
    100: "Hundred",
    1000: "Thousand",
    1000000: "Million",
    1000000000: "Billion",
}


def num_to_word(num :int)->str:
    """
    Function converts an integer into words.

    :param int num: The number to be converted to words.
    :return: The word representation of the number.
    :rtype: str
    """
    if num<20:
        return UNDER_20[num]
    elif num<100:
        if num%10==0:
            return TENS[num//10] 
        return TENS[num//10]+" "+UNDER_20[num%10]
    
    pivot=max([key for key in ABOVE_100 if key<=num])
    p1 = num_to_word(num // pivot)
    p2 = ABOVE_100[pivot]
    
    if num % pivot == 0:
        return f'{p1} {p2}'

    return f'{p1} {p2} {num_to_word(num % pivot)}'

        


if __name__ == "__main__":
    
    num = int(input("Enter a Number: "))
    if num >= 0 and num <= 999_999_999_999:
        print(num_to_word(num))
    else:
        print("Number out of range")