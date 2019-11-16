def slices(series, length):
    if length > len(series) or length < 1:
        raise ValueError("Length is greater than the string length")
    return [series[i:i+length] for i in range(len(series)) if not i + length > len(series)]