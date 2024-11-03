class Solution:
    def seats(self, seats):
        # Step 1: Find all occupied positions
        occupied_positions = [i for i, seat in enumerate(seats) if seat == 'x']

        if not occupied_positions:
            return 0  # No occupied seats

        # Step 2: Use the median position to minimize moves
        median_index = len(occupied_positions) // 2
        median_position = occupied_positions[median_index]

        # Step 3: Calculate moves to bring all 'x's around the median
        moves = 0
        for i, position in enumerate(occupied_positions):
            moves += abs(position - (median_position - median_index + i))

        return moves

# Time complexity: O(n)
# Space complexity: O(m) m is number of 'x'
seats = "..x..x.x..."
solution = Solution()
print(solution.minMovesToSeat(seats))  # Outp