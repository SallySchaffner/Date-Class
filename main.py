from Date import Date

def main():
    print("=== Date Class Demo ===")
    
    # Create some sample dates
    d1 = Date()  # Default date
    d2 = Date(2, 29, 2008)  # Leap year date
    d3 = Date(12, 31, 2024)  # Year end date
    
    print(f"Default date: {d1}")
    print(f"Leap year date: {d2}")
    print(f"Year end date: {d3}")
    
    print("\n=== Date Operations ===")
    
    # Test increment/decrement
    d2_copy = Date(2, 29, 2008)
    d2_copy.increment()
    print(f"After incrementing leap day: {d2_copy}")
    
    d2_copy.decrement()
    print(f"After decrementing back: {d2_copy}")
    
    # Test date arithmetic
    d4 = d2 + 10
    print(f"Adding 10 days to {d2}: {d4}")
    
    # Test date difference
    diff = d3 - d2
    print(f"Days between {d2} and {d3}: {diff}")
    
    print("\n=== Date Formats ===")
    print(f"Format 1 (MM/DD/YYYY): {d2.print_format_1()}")
    print(f"Format 2 (Month DD, YYYY): {d2.print_format_2()}")
    print(f"Format 3 (DD Month YYYY): {d2.print_format_3()}")
    
    print("\n=== Leap Year Tests ===")
    test_years = [2000, 1900, 2004, 2023, 2024]
    for year in test_years:
        is_leap = Date.is_leap_year_static(year)
        print(f"{year}: {'Leap year' if is_leap else 'Not a leap year'}")

if __name__ == "__main__":
    main()