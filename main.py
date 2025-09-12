#!/usr/bin/env python3
"""
Main entry point for the Python Date Class project.
Demonstrates the functionality of the custom Date class.
"""

from Date import Date

def main():
    print("=== Python Date Class Demonstration ===\n")

    # Create some sample dates
    print("1. Creating dates:")
    d1 = Date()  # Default date
    d2 = Date(2, 29, 2008)  # Leap year date
    d3 = Date(12, 25, 2024)  # Christmas 2024

    print(f"   Default date: {d1}")
    print(f"   Leap year date: {d2}")
    print(f"   Christmas 2024: {d3}")

    # Test different formats
    print("\n2. Date formatting:")
    print(f"   Format 1 (MM/DD/YYYY): {d2.print_format_1()}")
    print(f"   Format 2 (Month DD, YYYY): {d2.print_format_2()}")
    print(f"   Format 3 (DD Month YYYY): {d2.print_format_3()}")

    # Test date arithmetic
    print("\n3. Date arithmetic:")
    print(f"   Original date: {d2}")
    d2.nextDay()
    print(f"   After increment: {d2}")
    d2.previousDay()
    print(f"   After decrement: {d2}")

    # Test adding days
    d4 = d2 + 10
    print(f"   {d2} + 10 days = {d4}")

    # Test date difference
    diff = d3 - d2
    print(f"   Days between {d2} and {d3}: {diff}")

    # Test leap year functionality
    print("\n4. Leap year testing:")
    print(f"   Is {d2.year} a leap year? {Date.isLeapYear(d2.year)}")
    print(f"   Is 2024 a leap year? {Date.isLeapYear(2024)}")
    print(f"   Is 2023 a leap year? {Date.isLeapYear(2023)}")

    # Test year rollover
    print("\n5. Year rollover test:")
    d5 = Date(12, 31, 2023)
    print(f"   New Year's Eve: {d5}")
    d5.nextDay()
    print(f"   After increment: {d5}")

    print("\n=== End Demonstration ===")

if __name__ == "__main__":
    main()