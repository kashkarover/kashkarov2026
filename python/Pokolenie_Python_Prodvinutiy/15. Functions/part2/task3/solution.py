def mean(*args):
    nums = [num for num in args if type(num) in (int, float)]
    
    return sum(nums) / len(nums) if len(nums) != 0 else 0.0