/*
  Problem:
      Given a roman numeral, convert it to an integer.
      Input is guaranteed to be within the range from 1 to 3999.

  Solution:
      For the Roman numerals, it is from biggest to the smallest. Small numerals
      before larger numerals only happens when things like IX to represent 4 and
      nothing like IIX to represent 3. Therefore we only need to iterate the
      string once, add the number first, if this number is larger than previous
      one, just minus 2 * prev, since we have add an additional prev number.
 */

lass Solution {
public:
    // I 1, V 5, X 10, L 50, C 100, D 500, M 1000
    int romanToInt(string s) {
        int lastNum = 4000;
        int rt_num = 0;
        for(int i = 0; i < s.length(); i++){
            int currNum = roman2num(s[i]);
            rt_num += currNum;
            if(currNum > lastNum){
                rt_num -= 2 * lastNum;
            }
            lastNum = currNum;
        }
        return rt_num;
    }

    int roman2num(char r){
        switch (r){
            case 'I':
                return 1;
            case 'V':
                return 5;
            case 'X':
                return 10;
            case 'L':
                return 50;
            case 'C':
                return 100;
            case 'D':
                return 500;
            case 'M':
                return 1000;
            default:
                return 0;
        }
    }
};
