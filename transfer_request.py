
class Building(object):
    def __init__(self):
        super().__init__()
        self.in_request = 0
        self.out_request = 0
        self.acceptable_request = 0
    def increase_in_request(self):
        self.in_request += 1
        self._get_acceptable_request()

    def  increase_out_request(self):
        self.out_request += 1
        self._get_acceptable_request()
    
    def _get_acceptable_request(self):
        self.acceptable_request = min(self.in_request, self.out_request)

    def __repr__(self):
        return "[In request {}, out request {}, acceptable request {}]\n".format(self.in_request, self.out_request, self.acceptable_request)

class Solution:
    def maximumRequests(self, n, requests):
        buildings = []
        sum = 0
        for i in range(n):
            buildings.append(Building())
        # print(buildings)
        for request in requests:
            buildings[request[0]].increase_out_request()
            buildings[request[1]].increase_in_request()
        print(buildings)
        for b in buildings:
            sum += b.acceptable_request
        return sum

sol = Solution()
print(sol.maximumRequests(3, [[0,0],[1,1],[0,0],[2,0],[2,2],[1,1],[2,1],[0,1],[0,1]]))
# print("Expected {}".format(5))
# print(sol.maximumRequests(5, [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]))

# print("Expected {}".format(3))
# print(sol.maximumRequests(3, [[0,0],[1,2],[2,1]]))

# print("Expected {}".format(4))
# print(sol.maximumRequests(4, [[0,3],[3,1],[1,2],[2,0]]))
