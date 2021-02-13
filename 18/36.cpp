#include <iostream>
#include <fstream>

using namespace std;

// 345 (Даже написал на плюсах, не знаю, что с ней не так)

int main()
{
  ifstream inp("dat/18-17.txt");

  double p = INT8_MAX;
  double msum = INT8_MIN;
  double sum = 0;

  while (!inp.eof())
  {
    double n;
    inp >> n;

    if (n < p)
    {
      sum += n;
      if (sum > msum)
        msum = sum;
    }
    else
      sum = 0;

    p = n;
  }

  cout << (int)msum << endl;

  return 0;
}