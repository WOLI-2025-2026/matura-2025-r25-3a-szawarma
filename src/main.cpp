//dawid szarwas

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


string z3_1_path_symbole_txt = "../zalaczniki-2025/symbole.txt";


/*
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
*/

void zadanie2_2()
{
    ifstream plik(z3_1_path_symbole_txt);
    if(!plik.is_open())
    {
        cerr << "nie mozna otworzyc pliku" << endl;
        return;
    }

    vector<string> tekst;
    string linia;
    while(getline(plik, linia))
    {
        tekst.push_back(linia);
    }

    ofstream wynik("wynik_2_2.txt");

    int wiersze = tekst.size() + 1;
    int kolumny = (wiersze > 0) ? tekst[0].length() + 1 : 0;
    int ilosc = 0;


    for(int w = 0; w <= wiersze - 3; w++)
    {
        for(int k = 0; k <= kolumny - 3; k++)
        {
            char symbol = tekst[w][k];
            bool czy_kwadrat = true;

            for(int i = 0; i < 3 && czy_kwadrat; i++)
            {
                for(int j = 0; j < 3 && czy_kwadrat; j++)
                {
                    if(tekst[w + i][k + j] != symbol)
                    {
                        czy_kwadrat = false;
                    }
                }
            }

            if(czy_kwadrat)
            {
                cout << (w + 1) << " " << (k + 1) << " " ;
                wynik << (w + 1) << " " << (k + 1) << " " ;
                ilosc++;
            }
        }
    }

    plik.close();
    wynik.close();
}


int main() 
{
    zadanie2_2();
    return 0;
}
