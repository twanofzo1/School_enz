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


void vierkant(){
    std::cout << "Hoe groot: ";
    int size = inputToInt();

    if (size <= 0){
        std::cout << "het getal moet groter dan 0 zijn\n";
        exit(1);
    }

    for (int i = 0; i<size;i++){
        for (int j = 0; j<size;j++){
            std::cout << "*";
        }
        std::cout << "\n";
    }
}

void rechthoek(){
    std::cout << "Hoe breed: ";
    int breedte = inputToInt();
    std::cout << "Hoe hoog: ";
    int hoogte = inputToInt();

    if (breedte <= 0 || hoogte <= 0){
        std::cout << "de getallen moeten groter dan 0 zijn\n";
        exit(1);
    }

    for (int i = 0; i<hoogte;i++){
        for (int j = 0; j<breedte;j++){
            std::cout << "*";
        }
        std::cout << "\n";
    }
}



int main(){
    std::cout << "1: vierkant\n2: rechthoek\n: ";
    int keuze = inputToInt();
    switch (keuze) // finaly after .5 years of python elif hell a switch statement
    {
    case 1:
        vierkant();
        break;
    case 2:
        rechthoek();
        break;
    
    default:
        std::cout << "Dit is geen geldige keuze\n";
        return 1;
    }
    
    return 0;
}


