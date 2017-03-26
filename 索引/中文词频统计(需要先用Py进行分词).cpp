#include<iostream>
#include<map>
#include<vector>
#include<algorithm>
#include <fstream>  
#include <string> 
using namespace std; 
   
typedef pair<string, int> PAIR;
struct CmpByValue
{
	bool operator()(const PAIR& lhs, const PAIR& rhs)
	{
		return lhs.second > rhs.second;
	}

};
int main()
{
	char filename1[] = "re.txt"; // 结果写入到这个文件名 
	ofstream fout(filename1);    //用于后面写入txt
	string filename;
	cout << "Enter the file name : ";
	cin >> filename;  //输入要统计词频的文件名，需要用py进行分词，词与词之间用空格 
	cin.get();
	ifstream fin(filename.c_str());      //  read  in  str[]  
	string  temp;
	map<string, int> p;
	vector<pair<string, int> > a;
	map<string, int>::iterator iter;
	while (fin >> temp)
		p[temp]++;

	for (iter = p.begin(); iter != p.end(); iter++)
	{

		a.push_back(make_pair(iter->first, iter->second));
	}
	sort(a.begin(), a.end(), CmpByValue());
	for (int j = 0; j<a.size(); j++)
		fout << a[j].first << " " << a[j].second << endl;  //输出到指定文件
	return 0;
}
