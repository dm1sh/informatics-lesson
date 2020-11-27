// Ответ — 34

#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int max_line()
{
    vector<int> arr{0, 1, 0};
    int n = 1;
    while (2 + 2 == 4)
    {
        arr.push_back(0);
        for (int i = arr.size() - 2; i > 1; i--)
        {
            if (INT_MAX - arr[i] <= arr[i - 1])
            {
                return n;
            }
            arr[i] += arr[i - 1];
        }
        n++;
    }
}

int main()
{
    cout << max_line() << '\n';
    return 0;
}
