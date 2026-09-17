#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        return atMost(nums, k) - atMost(nums, k - 1);
    }

    int atMost(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        int left = 0;
        int count = 0;

        for (int right = 0; right < nums.size(); right++) {
            map[nums[right]]++;

            while (map.size() > k) {
                map[nums[left]]--;

                if (map[nums[left]] == 0) {
                    map.erase(nums[left]);
                }

                left++;
            }

            count += right - left + 1;
        }

        return count;
    }
};
