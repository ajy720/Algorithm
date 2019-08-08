#include <stdio.h>
#include <string.h>

int check_string(char *str, char *sch){
	int i, j;
	for(i=0;i<strlen(str);i++){
		for(j=0;j<strlen(sch);j++){
			if(str[i] == sch[j]) return 1;
		}
	}
	return 0;
}

main(){
	char pw[100];
	char aLPHA[]={"ABCDEFGHIJKLMNOPQRSTUVWXYZ"};
	char alpha[]={"abcdefghijklmnopqrstuvwxyz"};
	char number[]={"0123456789"};
	char mark[]={"!@#$%^&*()-=_+\\|;:'\"/?,.<>~[]{}`"};
	int i;
	
	scanf("%s", pw);
				
	if(strlen(pw)>=8&&strlen(pw)<=15&&check_string(pw, aLPHA)&&check_string(pw, alpha)&&check_string(pw, number)&&check_string(pw, mark)){
		for(i=0;i<strlen(pw);i++){
			if(pw[i]>=33&&pw[i]<=126);
			else{
				printf("invalid");
				return 0;
			}
		}
		printf("valid");
		return 0;
	}
	printf("invalid");
	return 0;
}

