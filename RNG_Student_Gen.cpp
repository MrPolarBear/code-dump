#include<iostream>
#include<ctime>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<ctime> // Convert time_t value to a string
#include<stdio.h>
#include<windows.h>
using namespace std;
int main()
{
	srand((unsigned) time(0));																	//without this, the rng() function calls upon the same seed. This will pull the seed from current time
	int choice;
	int rng = 0;
	string student[34];											
	student[0]="1 - Adriana (not here)";
	student[1]="2 - Morgan";
	student[2]="3 - Mea";
	student[3]="4 - Steven";
	student[4]="5 - Kayleigh";
	student[5]="6 - Isabella";
	student[6]="7 - Cayden";
	student[7]="8 - Tristan";
	student[8]="9 - Edgar";
	student[9]="10 - Matt";
	student[10]="11 - Leslie";
	student[11]="12 - Ryley";
	student[12]="13 - Trinity";
	student[13]="14 - Jordan"; 						
	student[14]="15 - Sam";
	student[15]="16 - Angie";
	student[16]="17 - Lexi";
	student[17]="18 - Ryan";
	student[18]="19 - Edwardo";
	student[19]="20 - Shane";
	student[20]="21 - Ryan";
	student[21]="22 - Aaron";
	student[22]="23 - Abigail";
	student[23]="24 - Ajai";
	student[24]="25 - Zach";
	student[25]="26 - Blake";
	student[26]="27 - Lilly";
	student[27]="28 - Warren";
	student[28]="29 - Mia";
	student[29]="30 - Emersen";
	student[30]="31 - Elijah";
	student[31]="32 - Max";
	student[32]="33 - Payton";
	student[33]="34 - Robert";
	vector<int> prev;																													//container for checking if we called a student or not
	int num_elements = sizeof( student ) / sizeof( student[0] );																		//get number of students in array, this is for debugging only
	
	time_t now = time(0);																												// Get the current date/time based on current system
	
	char* dt = ctime(&now);																												// Convert the now to a string form
	
	cout << "Date and Time is: " << dt;
	cout << "#############################################" << endl << endl;	
	//cout << num_elements <<" is how many are in the student array."<< endl;															//debugging
	
	cout <<"Oooooo weeeee rng rng we picking or are we closing? (1 for pick, 2 for close):                ";							//Prompt for picking or closing prog
	cin >> choice;																														//input of choice			
	//do{																																//beginning of dowhile loop, not used anymore
	while (choice !=2){																													//using regular while loop instead
	
		rng = rand()%33;																												//rng generator from 0-33 (34 numbers)
		
		if(find(prev.begin(),prev.end(), rng) !=prev.end() ){																			//if rng generator is within the container of called students, first {}
			cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"<<endl;
			cout << "Amount of students called so far is: " << prev.size()+1 << endl;													//had to call +1 to prev.size() so it would accurately return how many students were called
			//cout << student[rng] << " was previously picked, go again (need to retype 1):      ";										//^^^^^^since size considers 0 first rather than 1 
			cout << student[rng] << " was previously picked, prog will continue to cycle until a new student is picked"<<endl;
		}
		else{																															//if rng generator calls upon a new student, declare it
			cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"<<endl;
			cout << student[rng] << " was picked~"<<endl<<"Go again? (1 for pick, 2 for close):      ";									//declaration of new student called
			prev.push_back(rng);																										//push called student's value into the container
			cin >> choice;																												//input if we want to continue or not
		}
		/*cout << "This is a test for the prev function: " << prev[0]<<endl;*/
		
		//cin >> choice;	//old spot for cin
		
		if(prev.size()==33){																											//if container is equal to amount of students in class, then force close prog
			cout << endl << endl << endl << endl << endl<<endl<<endl;																	//^^^^^would be an infinite loop without this statement
			cout << "*****************************************************************************************************"<<endl<<endl;
			cout << "All students have been called, prog will now declare choice = 2 and close"<<endl<<endl;										
			cout << "*****************************************************************************************************";
			cout << endl << endl << endl << endl << endl<<endl<<endl;
			choice = 2;
		}
		
		
	}//while (choice !=2);																												//end of do while loop, not used anymore
	
	
	return 0;
}
