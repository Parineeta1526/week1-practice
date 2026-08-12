def analyze_numbers(numbers):
    total=sum(numbers)
    average=total/len(numbers)
    highest=max(numbers)
    lowest=min(numbers)
    even_count=0
    odd_count=0
    for num in numbers:
      if num % 2 == 0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
    return total,average,highest,lowest,even_count,odd_count
total,average,highest,lowest,even_count,odd_count=analyze_numbers(numbers)
print(f"Total: {total}")
print(f"Average: {average}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Even Count: {even_count}")
print(f"Odd Count: {odd_count}")