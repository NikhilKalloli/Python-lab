def max_min(arr):
    print(f"Maximum number: {max(arr)}")
    print(f"Minimum number: {min(arr)}")

def second_largest(arr):
    max_num = max(arr)
    second_largest = arr[0]
    for num in arr:
        if num < max_num and num > second_largest:
            second_largest = num
    print(f"Second largest number: {second_largest}")

def main():
    arr = list(map(int, input("Enter the numbers separated by space: ").split()))
    max_min(arr)
    second_largest(arr)

if __name__ == "__main__":
    main()