/*
  Problem:
    Given an array of integers, return indices of the two numbers such that they
    add up to a specific target.

    You may assume that each input would have exactly one solution, and you may
    not use the same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
 */

/*
  Solution:
    The brutal force method can be the first thought jump out of your head.

    Brutal force: search for list for several rounds to find a match.
    Simple, but slow.

    Using map (or hashmap): only iterate once. For each element i, look in the map
    whether there is key=(target - i), if there is, return, otherwise put this
    element in the map as (i: index)
 */




class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> container;
        vector<int> rt_v;
        map<int, int>::iterator it;
        for(int i = 0; i < nums.size(); i++){
            if((it = container.find(target - nums[i])) != container.end()){
                rt_v.push_back(it->second);
                rt_v.push_back(i);
                return rt_v;
            }
            container[nums[i]] = i;
        }
    }
};
