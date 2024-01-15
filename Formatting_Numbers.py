# F-Strings with format specifications
fp_number = 12345.6789
fp_number2 = 1234512345.6789
fp_number3 = .6789

dc_number = 6789

# [field width][comma].[decimal places][type-code]

print(f"{fp_number:.2f}")
print("{:.2f}".format(fp_number))

# Adding commas
print(f"{fp_number:,.2f}")

# Justification
print(f"{fp_number:15,.2f}")
print(f"{fp_number2:15,.2f}")

# Different type codes
print(f"{fp_number3:.0%}")
print(f"{fp_number3:.1%}")

"""
f = floating point number
d = integer
% = percentage
e = scientific notation
"""

print(f"{dc_number:d}")
print(f"{dc_number:,d}")
print(f"{dc_number:10,d}")

# Formatting String Literals
print(f"{'Description':15} {'Price':>10} {'Qty':>5}")
print(f"{'Legend of Zelda':15} {10.99:10.2f} {3:5d}")

# Locales
import locale as lc

lc.setlocale(lc.LC_ALL, "de")
print(lc.currency(12345.6789, grouping=True))