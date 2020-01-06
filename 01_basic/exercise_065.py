def main():
    seconds = float(input("Seconds:"))
    print("""
    %.0f seconds are %f years,
    %.0f seconds are %f months,
    %.0f seconds are %f weeks,
    %.0f seconds are %f days
    """ % (
      seconds,
      seconds / 365 / 86400,
      seconds,
      seconds / 30 / 86400,
      seconds,
      seconds / 7 / 86400,
      seconds,
      seconds / 86400,
    ))

if __name__ == '__main__': main()