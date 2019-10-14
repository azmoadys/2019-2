#include<iostream>
#include<vector>
#include<time.h>
#include<fstream>
#include<string>
#include<string.h>
using namespace std;
int Big_O_6(int rows, int cols, vector<vector<int> > mat);
int Big_O_4(int rows, int cols, vector<vector<int> > mat);
int Big_O_3(int rows, int cols, vector<vector<int> > mat);

int main(int argc, char **argv)
{
	int rows, cols;
	int result;
	ifstream fin;
	fin.open(argv[1]);
	if(fin.is_open() != true) // exception: when there is no such file.
	{
		cout << "No file!\n";
		return 0;
	}
	fin >> rows >> cols;
	vector<vector<int> > mat;
	mat.assign(rows, vector<int>(cols, 0));
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++)
		{
			fin >> mat[i][j];
		}
	}
	// save file in matrix
	clock_t start, end;
	start = clock();
	// check which algorith to use
	if(*argv[2] =='1')
		result = Big_O_6(rows, cols, mat);
	else if(*argv[2] == '2')
		result = Big_O_4(rows, cols, mat);
	else if(*argv[2] == '3')
		result = Big_O_3(rows, cols, mat);
	else
	{
		cout<<"Wrong Algorithm Index\n";
		return 0;
	}
	end = clock();
	double tm = (double)(end-start)/CLOCKS_PER_SEC*1000; // time measure

	ofstream fout;
	char output[1000] = "result_";
	strcat(output,argv[1]); // set name as result_inputXXXXX.txt
	fout.open(output);
	if(fout.is_open()){
		fout <<argv[1] << "\n"<< *argv[2]<<"\n"<<rows<<"\n"<<cols<<"\n"<<result<<"\n"<<tm;
	}// make output.
	return 0;
}

int Big_O_6(int rows, int cols, vector<vector<int> > mat)
{
	int max_val = mat[0][0];
	for (int row_len = 0; row_len < rows; row_len++)
	{
		for (int col_len = 0; col_len < cols; col_len++) // set cover length
		{
			for (int row = 0; row < rows - row_len; row++)
			{
				for (int col = 0; col < cols - col_len; col++) // Starting point
				{
					int temp = 0;
					for (int row_num = row; row_num < row + row_len + 1; row_num++)
					{
						for (int col_num = col; col_num < col + col_len + 1; col_num++)
						{
							temp += mat[row_num][col_num]; // sum
						}
					}
					if (max_val < temp) // check max value
					{
						max_val = temp;
					}
				}
			}
		}
	}
	return max_val;
}
int Big_O_4(int rows, int cols, vector<vector<int> > mat)
{
	vector<vector<int> > dp;
	dp.assign(rows, vector<int>(cols, 0));
	for (int row = 0; row < rows; row++)
	{
		for (int col = 0; col < cols; col++)
		{
			if (row == 0 && col == 0)
				dp[row][col] = mat[row][col];
			else if (row == 0)
				dp[row][col] = dp[row][col - 1] + mat[row][col];
			else if (col == 0)
				dp[row][col] = dp[row - 1][col] + mat[row][col];
			else
				dp[row][col] = dp[row - 1][col] + dp[row][col - 1] - dp[row - 1][col - 1] + mat[row][col];
		}
	} // make a sum (0,0) to (i,j) in matrix
	int max_val = mat[0][0];
	for (int end_row = 0; end_row < rows; end_row++)
	{
		for (int end_col = 0; end_col < cols; end_col++) // end point
		{
			for (int start_row = 0; start_row <= end_row; start_row++)
			{
				for (int start_col = 0; start_col <= end_col; start_col++) // start point
				{
					int temp = 0;
					if (start_row == 0 && start_col == 0)
						temp = dp[end_row][end_col];
					else if (start_row == 0)
						temp = dp[end_row][end_col] - dp[end_row][start_col - 1];
					else if (start_col == 0)
						temp = dp[end_row][end_col] - dp[start_row - 1][end_col];
					else
						temp = dp[end_row][end_col] - dp[end_row][start_col - 1] - dp[start_row - 1][end_col] + dp[start_row - 1][start_col - 1];
					// check (x1,y1) to (x2,y2) sum by differenciate (0,0) to (x1-1,y1-1) and (0,0) to (x2,y2)
					if (max_val < temp)
					{
						max_val = temp;

					}
				}
			}
		}
	}
	return max_val;
}
int Big_O_3(int rows, int cols, vector<vector<int> > mat)
{
	vector<int> kadane;
	int max_val = mat[0][0];

	for (int start = 0; start < cols; start++)
	{
		kadane.assign(rows, 0); // initialization the sums
		for (int end = start; end < cols; end++)
		{
			for (int i = 0; i < rows; i++)
			{
				kadane[i] += mat[i][end]; //save it as a row by column
			}
			int temp;
            int temp_sum=0, max_sum=0; // check a sum(temp_sum) and max value of it
            bool finish = false;

            for(int i=0;i<rows;i++)
            {
                temp_sum += kadane[i];
                if(temp_sum<0)
                    temp_sum =0;
                else if (temp_sum>max_sum)
                {
                    max_sum = temp_sum;
                    finish = true;
                }
            }
            if(finish)
            {
                temp = max_sum;
            }
            else //if this part runs, it means none of temp_sum is bigger max_sum
            {
                max_sum=kadane[0];
                for(int i=1;i<rows;i++)
                {
                    if(kadane[i]>max_sum) //check max_sum is bigger than sum of cols.
                        max_sum = kadane[i];
                }
                temp = max_sum;
            }
			if (max_val < temp) 
			{
				max_val = temp;
			}
		}
	}

	return max_val;
}
