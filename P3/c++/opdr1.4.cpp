#include <iostream>

//Naam: Twan Roodenburg
//studentNummer: 1827033

int main(){
    int number = 65;
    while( number < 90){
        if(number < 70){
            number = 70;
        }else if( number < 80){
            number++;
        }
        number += 3;
        std::cout << number << "\n";
    }
}

/*
65 : begin
73 : 65->70 +3
77 : 73 + 1 + 3
81 : 77 + 1 + 3
84 : 81 + 3
87 : 84 + 3
90 : 87 + 3
*/