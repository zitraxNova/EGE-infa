#include <iostream>                                                                 
#include <fstream>
#include <string>
using namespace std;

int maxSequenceWithLimitedPairs(const string &filename) {
    ifstream file(filename);
    
    if (!file.is_open()) {
        cerr << endl;
        return -1;
    }

    int max_length = 0;
    int left = 0;
    int bc_count = 0;

    string line;
    while (getline(file, line)) {
        for (size_t right = 0; right < line.length(); ++right) {
            if (line[right] == 'B' && right + 1 < line.length() && line[right + 1] == 'C') {
                bc_count++;
            }
            
            while (bc_count > 180) {
                if (left < line.length() - 1 && line[left] == 'B' && line[left + 1] == 'C') {
                    bc_count--;
                }
                left++;
            }
            
            max_length = max(max_length, static_cast<int>(right - left + 1));
        }
    }

    file.close();
    return max_length;
}

int main() {
    const string filename = 'input.txt';
    int result = maxSequenceWithLimitedPairs(filename);
    
    cout << 'Максимальная длина:' << result << endl;
    return 0;
}