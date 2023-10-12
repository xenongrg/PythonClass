def slope_intercept_form(slope, y_intercept):
    return lambda x: slope * x + y_intercept


m = 0.5
c = 2

y = slope_intercept_form(m, c)
print(y(2))

