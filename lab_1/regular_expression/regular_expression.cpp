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
				state = 0;
			i += 1;
			break;
		case 'd':
			if (state == 2 || state == 1)
				state = 3;
			else
				state = 0;
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
			state = 0;
			i += 1;
			break;
		}
	}

	return state == 3;
}

int main(int argc, const char **argv)
{
	vector<string> strings = {
		"asd",
		"sdfsfgd",
		"ad",
		"acd",
		"acbd",
		"acbbcd",
		"acbda"};

	for (string str : strings)
	{
		// cout << str << "\n";
		cout << FSM(str) << "\n";
	}
	return 0;
}