class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        a = [0] * (n + 1)
        S = [0]
        for change in bookings:
            first, last, inc = change[0], change[1], change[2]
            a[first - 1] += inc
            a[last] -= inc
        for i in range(1, n + 1):
            S.append(S[i - 1] + a[i - 1])
        return S[1:]
