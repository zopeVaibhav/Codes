// MARETTING COMPANY
#include <iostream>
#include <string>
using namespace std;
// base class publication
class publication
{
private:
    string title;
    float prices;

public:
    publication()
    {
        title = "";
        prices = 0.0;
    }
    void get_data()
    {
        cout << "\n---------Enter Details-------";
        cout << "\nEnter Title :";
        cin.ignore(); // clear input buffer
        getline(cin, title);
        cout << "\nEnter Price : ";
        cin >> prices;
    }
    void put_data()
    {
        cout << "\n ________DSIPLAY DATA_________\n";
        cout << "\n Title is " << title;
        cout << "\n Price is " << prices << "/-";
    }
};
class book : public publication
{

private:
    int pages;

public:
    book()
    {
        pages = 0;
    }
    void get_data()
    {
        publication::get_data();
        cout << endl;
        cout << "Enter Page Count : \n";
        cin >> pages;
    }
    void put_data()
    {
        publication::put_data();
        try
        {
            if (pages < 0)
                throw pages;
        }
        catch (int f)
        {
            cout << "\n error: pages not valid :" << f;
            pages = 0;
        }
        cout << "\n Pages Are :" << pages;
    }
};
class tape : public publication
{
private:
    float playtime;

public:
    tape()
    {
        playtime = 0.0;
    }
    void get_data()
    {
        publication::get_data();
        cout << "Enter Play Time Of Cassette \n";
        cin >> playtime;
    }
    void put_data()
    {

        publication::put_data();
        try
        {
            if (playtime < 0.0)
                throw playtime;
        }
        catch (float r)
        {
            cout << "\n Error: Invalid Playtime : " << playtime;
            playtime = 0.0;
        }
        cout << "\n Playtime is : " << playtime;
    }
};
int main() // main program
{
    book b[10]; // arrray of objects
    tape t[10];
    int choice = 0, bookCount = 0, tapeCount = 0;
    do
    {
        cout << "\n-------------MARKETTING MENU-------------";
        cout << "\n 1. Add book ";
        cout << "\n 2. Add tape: ";
        cout << "\n 3. Display book ";
        cout << "\n 4. Display tape";
        cout << "\n 5. Exit:" << endl;
        cout << "\n Enter Choice : ";
        cin >> choice;
        switch (choice)
        {
        case 1:
        {
            cout << "\n------ADDING BOOK DETAILS--------\n";
            b[bookCount].get_data();
            bookCount++;
            break;
        }
        case 2:
        {
            cout << "\n-------ADDING TAPE DETAILS-------\n";
            t[tapeCount].get_data();
            tapeCount++;
            break;
        }
        case 3:
        {
            cout << "\n------BOOK DETAILS------";
            for (int j = 0; j < bookCount; j++)
            {
                b[j].put_data();
            }
            break;
        }
        case 4:
        {
            cout << "\n-------TAPE DETAILS------";
            for (int j = 0; j < tapeCount; j++)
            {
                t[j].put_data();
            }
            break;
        }
        case 5:
        {
            cout << "**********Program Exited Successfully**********" << endl;
            exit(0);
        }
        default:
        {
            cout << "\n Invalid";
        }
        }
    } while (choice != 5);
    return 0;
}
