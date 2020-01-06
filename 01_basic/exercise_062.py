from math import sqrt

def main():
    print("""
    1 year is %.0f seconds:
    1 month(30 days) is %.0f seconds,
    1 week is %.0f seconds,
    1 day is %.0f seconds,
    """ % (
      1 * 365 * 86400,
      1 * 30 * 86400,
      1 * 7 * 86400,
      1 * 86400,
    ))

if __name__ == '__main__': main()