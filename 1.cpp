// Ответ — 34

#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int max_line()
{
    vector<int> arr{1};
    int n = 1;
    while (2 + 2 == 4)
    {
        arr.insert(arr.begin(), 0);
        for (int j = 0; j < arr.size(); j++)
        {
            if (INT_MAX - arr[j + 1] <= arr[j])
            {
                return n;
            }
            arr[j] += arr[j + 1];
        }
        n++;
    }
}

int main()
{
    cout << max_line() << '\n';
    return 0;
}
