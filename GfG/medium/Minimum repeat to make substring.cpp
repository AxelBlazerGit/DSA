// User function Template for C++

class Solution {
  public:
    int minRepeats(string& s1, string& s2) {
        // code here
        unordered_set<char> s1_chars(s1.begin(), s1.end());
        for (char c : s2) {
            if (s1_chars.find(c) == s1_chars.end()) {
                return -1;
            }
        }

        int min_repeats = (s2.size() + s1.size() - 1) / s1.size();
        
        string repeated_s1 = "";
        for (int i = 0; i < min_repeats; i++) {
            repeated_s1 += s1;
        }

        if (repeated_s1.find(s2) != string::npos) {
            return min_repeats;
        }

        repeated_s1 += s1;
        if (repeated_s1.find(s2) != string::npos) {
            return min_repeats + 1;
        }
        
        return -1;
    }
};
