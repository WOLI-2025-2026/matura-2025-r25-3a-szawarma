//dawid szarwas

#include <iostream>
#include <fstream>

using namespace std;

string z3_1_path_symbole_txt = "../zalaczniki-2025/symbole.txt";

bool czy_palindrom(string slowo)
{
    int dlugosc = slowo.length();
    for(int i = 0; i < dlugosc / 2; i++)
    {
        if(slowo[i] != slowo[dlugosc - i - 1])
        {
            return false;
        }
    }
    return true;
}

void zadanie2_1()
{
    ifstream plik(z3_1_path_symbole_txt);
    if(!plik.is_open())
    {
        cerr << "nie mozna otworzyc pliku" << endl;
    }

    ofstream wynik("wynik_2_1.txt");

    string linia;
    while(plik >> linia)
    {
        if (czy_palindrom(linia))
        {
            cout << linia << endl;
            wynik << linia << endl;
        }
    }

    wynik.close();
    plik.close();

}


int main() 
{

    zadanie2_1();
    return 0;
}
