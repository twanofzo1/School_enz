def H5Opdr5():
    def convert(celsius):
        return celsius * 1.8 + 32

    def table():
        result = "  F       C\n"
        for celsius in range(-30, 41, 10):
            fahrenheit = convert(celsius)
            result += f"{fahrenheit:6.1f}   {celsius:6.1f}\n"
        return result
