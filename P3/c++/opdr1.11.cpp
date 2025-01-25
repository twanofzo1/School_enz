#include <iostream>
#include <string>

//Naam: Twan Roodenburg
//studentNummer: 1827033


int inputToInt(){
    std::string input;
    std::cin >> input;
    int size;

    try{
        size = std::stoi(input);
    }
    catch(std::invalid_argument){
        std::cout << "Dit is geen getal\n";
        exit(1);
    }
    return size;
}

void driehoek_for(){ // 100% mijn prefference for loops > while loops
    std::cout<<"Hoe groot?: ";
    int size = inputToInt();

    if (size <= 0){
        std::cout << "het getal moet groter dan 0 zijn\n";
        exit(1);
    }

    for(int i = 1; i < size; i++){
        for (int j = 0; j<i; j++){
            std::cout<<"*";
        }
        std::cout<<"\n";
    }
    for(int i = size; i > 0; i--){
        for (int j = 0; j<i; j++){
            std::cout<<"*";
        }
        std::cout<<"\n"; 
    }
}

void driehoek_while(){
    std::cout<<"Hoe groot?: ";
    int size = inputToInt();

    if (size <= 0){
        std::cout << "het getal moet groter dan 0 zijn\n";
        exit(1);
    }

    int i = 0;
    while(i < size){
        i++;
        int j = 0;
        while (j < i){
            j++;
            std::cout<<"*";
        }
        std::cout<<"\n";
    }
    while(i > 1){
        i--;
        int j = 0;
        while (j < i){
            j++;
            std::cout<<"*";
        }
        std::cout<<"\n";
    }
}


int main(){
    std::cout << "1: driehoek met for loop\n2: driehoek met while loop\n: ";
    int keuze = inputToInt();
    switch (keuze) // finaly after .5 years of python elif hell a switch statement
    {
    case 1:
        driehoek_for();
        break;
    case 2:
        driehoek_while();
        break;

    
    default:
        std::cout << "Dit is geen geldige keuze\n";
        return 1;
    }
    
    return 0;
}


