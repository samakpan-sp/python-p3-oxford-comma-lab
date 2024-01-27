# from lib.oxford_comma import oxford_comma

def oxford_comma(elements):
    if len(elements) == 0:
        return ""
    elif len(elements) == 1:
        return elements[0]
    elif len(elements) == 2:
        # If there are only two elements, join them with "and" without a comma
        return f"{elements[0]} and {elements[1]}"
    else:
        # Join all elements except the last one with commas
        joined_elements = ", ".join(elements[:-1])
        # Add the Oxford comma before the last element and join it with the rest
        return f"{joined_elements}, and {elements[-1]}"



result = oxford_comma(["fiddleheads", "okra", "kohlrabi"])
print(result)