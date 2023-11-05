#include<iostream>
#include<string>
using namespace std;

struct SV {
	string tenSV;
	double dtb;
};
void nhapSV(SV &a) {
	cout << "Ten sinh vien: ";
	cin >> a.tenSV;
	fflush(stdin);
	cout << "Diem trung binh: ";
	cin>> a.dtb;
}
void xuatSV(SV a)
{
	cout << "Ten sinh vien: " << a.tenSV << endl;
	cout << "Diem trung binh: " << a.dtb << endl;
}
void nhapLopHoc(SV a[], int& n)
{
	do
	{
		cout << "Nhap sp luong sv: ";
		cin >> n;
	} while (n <= 0);
	for (int i = 0; i < n; i++)
	{
		nhapSV(a[i]);
	}
}
void xuatLophoc(SV a[], int n)
{
	for (int i = 0; i < n; i++)
	{
		xuatSV(a[i]);
	}
}
void diemTBCaoNhat(SV a[], int n)
{
	double maxDtb = a[0].dtb;
	for (int i = 1; i < n; i++)
	{
		if (maxDtb < a[i].dtb)
			maxDtb = a[i].dtb;
	}
	cout << "Diem trung binh cao nhat: " << maxDtb << endl;
}
bool timThiSinhTheoTen(SV a[],int n, string const& ten)
{
	for (int i = 0; i < n; i++)
	{
		if (a[i].tenSV == ten)
		{
			return true;
		}
		return false;
	}
}
void sapXepSinhVien(SV a[], int n)
{
	for (int i = 0; i < n -1; i++)
	{
		for (int j = i; j < n; j ++)
			if (a[i].dtb > a[j].dtb)
			{
				SV b;
				b.tenSV = a[i].tenSV;
				b.dtb = a[i].dtb;
				a[i].tenSV = a[j].tenSV;
				a[i].dtb = a[j].dtb;
				a[j].tenSV = b.tenSV;
				a[j].dtb = b.dtb;

				
			}
	}
}
int main()
{
	int n;
	SV a[100];
	nhapLopHoc(a, n);
	xuatLophoc(a, n);
	diemTBCaoNhat(a, n);
	string ten;
	cout << "Nhap ten sinh vien can tim: ";
	cin >> ten;
	fflush(stdin);
	if (timThiSinhTheoTen(a, n, ten))
	{
		cout << "Tim thay" << endl;
	}
	else
	{
		cout << "Khong thay" << endl;
	}
	sapXepSinhVien(a, n);
	xuatLophoc(a, n);
	return 0;
}