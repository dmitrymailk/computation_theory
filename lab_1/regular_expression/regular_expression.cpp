#include <string>
#include <iostream>
#include <vector>

using namespace std;

bool FSM(string some_string)
{

	int i = 0;
	int state = 0;

	while (i < some_string.size())
	{
		char c = some_string[i];
		// cout << "\n";
		switch (c)
		{
		case 'a':
			if (state == 0)
				state = 1;
			else
				return 0;
			i += 1;
			break;
		case 'd':
			if (state == 2 || state == 1)
				state = 3;
			else
				return 0;
			i += 1;
			break;
		case 'c':
			if (state == 1 || state == 2)
				state = 2;
			i += 1;
			break;
		case 'b':
			if (state == 1 || state == 2)
				state = 2;
			i += 1;
			break;
		default:
			return 0;
			i += 1;
			break;
		}
	}

	return state == 3;
}
bool FSM_2(string some_string)
{

	int i = 0;
	int state = 0;

	while (i < some_string.size())
	{
		char c = some_string[i];
		// cout << "\n";
		switch (state)
		{
		case 0:
			if (c == 'a')
				state = 1;
			else
				return 0;
			i++;
			break;
		case 1:
			if (c == 'c' || c == 'b')
				state = 1;
			else if (c == 'd')
				state = 2;
			else
				return 0;
			i++;
			break;
		case 2:
			return 0;
			break;

		default:
			return 0;
		}
	}

	return state == 2;
}

int main(int argc, const char **argv)
{
	// a(b|c)*d
	vector<string> strings = {
		"asd",
		"sdfsfgd",
		"ad",
		"acd",
		"acbd",
		"acbbcd",
		"acbda",
		"acbd",
		"abcd",
		"abcd",
		"abacd",
	};

	for (string str : strings)
	{
		// cout << str << "\n";
		cout << str << " " << FSM_2(str) << "\n";
	}

	return 0;
}