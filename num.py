// C++ program for the above approach

#include "bits/stdc++.h"
using namespace std;

vector<int> Ans;

// Function to generate all numbers
// having "01" and "10" as a substring
void populateNumber()
{
	// Insert 2 and 5
	Ans.push_back(2);
	Ans.push_back(5);

	long long int x = 5;

	// Iterate till x is 10 ^ 15
	while (x < 1000000000001) {

		// Multiply x by 2
		x *= 2;
		Ans.push_back(x);

		// Update x as x*2 + 1
		x = x * 2 + 1;

		Ans.push_back(x);
	}
}

// Function to check if binary representation
// of N contains only "01" and "10" as substring
string checkString(long long int N)
{
	// Function Call to generate all
	// such numbers
	populateNumber();

	// Check if a number N
	// exists in Ans[] or not
	for (auto& it : Ans) {

		// If the number exists
		if (it == N) {
			return "Yes";
		}
	}

	// Otherwise
	return "No";
}

// Driver Code
int main()
{
	long long int N = 5;

	// Function Call
	cout << checkString(N);

	return 0;
}
