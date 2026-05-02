class Solution:
    def rotatedDigits(self, n: int) -> int:
        """
        Calculates the number of 'good' integers in [1, n] using 
        combinatorial counting over valid digit sets.
        """
        s = str(n)
        length = len(s)
        
        # S_id: {0, 1, 8} (3 choices)
        # S_valid: {0, 1, 8, 2, 5, 6, 9} (7 choices)
        
        def count_combinations(limit_str, digit_set):
            """
            Generalized function to count numbers <= limit_str 
            composed only of digits in the provided set.
            """
            count = 0
            allowed = sorted(list(digit_set))
            
            for i in range(len(limit_str)):
                current_digit = int(limit_str[i])
                
                # Count options for the current position that are strictly 
                # less than the digit in n
                for d in allowed:
                    if d < current_digit:
                        # For the remaining positions, all combinations are valid
                        count += len(allowed) ** (len(limit_str) - 1 - i)
                    else:
                        break
                
                # If the current digit itself is not allowed, 
                # we cannot form any more numbers with this prefix
                if current_digit not in digit_set:
                    return count
                    
            # Add 1 to include the number 'n' itself if it is valid
            return count + 1

        # V: Total numbers in [0, n] that rotate to a valid number
        total_valid = count_combinations(s, {0, 1, 2, 5, 6, 8, 9})
        
        # S: Total numbers in [0, n] that rotate to themselves (Identity)
        total_identity = count_combinations(s, {0, 1, 8})
        
        # The result is Valid - Same. 
        # Note: 0 is counted in both (0-0=0), so it correctly excludes 0.
        return total_valid - total_identity        