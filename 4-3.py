def lang_genoeg(lengte):
    if lengte >= 120:
        return "Je bent lang genoeg voor de attractie!"
    else:
        return "Sorry, je bent te klein!"
    
print(f"130 cm :\n{lang_genoeg(130)}")
print(f"110 cm :\n{lang_genoeg(110)}")
