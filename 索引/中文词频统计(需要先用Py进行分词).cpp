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
	char filename1[] = "re.txt"; // ���д�뵽����ļ��� 
	ofstream fout(filename1);    //���ں���д��txt
	string filename;
	cout << "Enter the file name : ";
	cin >> filename;  //����Ҫͳ�ƴ�Ƶ���ļ�������Ҫ��py���зִʣ������֮���ÿո� 
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
		fout << a[j].first << " " << a[j].second << endl;  //�����ָ���ļ�
	return 0;
}
