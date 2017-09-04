/*
  Problem:
    Given an array S of n integers, are there elements a, b, c in S such that
    a + b + c = 0? Find all unique triplets in the array which gives the sum of
    zero.

    Note: The solution set must not contain duplicate triplets.

    For example, given array S = [-1, 0, 1, 2, -1, -4],

    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]

  Solution:
    Although I have done this before, I got stuck. Well, not stuck, but a period
    of time of holding an obvious false solution. This problem is kinda diff
    from 2Sum since there will be duplication, therefore map cannot be used. The
    right way to do this is to using double pointers. Sort the list, then fix
    the first the number, use low pointer and high pointer. Remember to jump
    over those numbers being scanned for either low, high and i.
 */


class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> rt;

        for(int i = 0; i < nums.size(); i++){
            while((i != 0) && nums[i]==nums[i-1]) i++;
            int low = i + 1;
            int high = nums.size() - 1;
            while(low < high){
                if(nums[low] + nums[high] + nums[i] == 0){
                    vector<int> tmp;
                    tmp.push_back(nums[i]);
                    tmp.push_back(nums[low]);
                    tmp.push_back(nums[high]);
                    rt.push_back(tmp);
                    while((low < high) && nums[low] == nums[low+1]) low++;
                    while((low < high) && nums[high] == nums[high-1]) high--;
                    low++;
                    high--;
                }else if(nums[low] + nums[high] + nums[i] < 0){
                    while((low < high) && nums[low] == nums[low+1]) low++;
                    low++;
                }else{
                    while((low < high) && nums[high] == nums[high-1]) high--;
                    high--;
                }
            }

        }
        return rt;
    }
};
