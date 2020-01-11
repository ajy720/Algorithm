//2055 : 두 수의 약수 구하기

#include <stdio.h>

main(){
	int i, a, b, temp, rest_inv[1000], rest_a[1000], rest_b[1000], rest[2000], j=0;
	scanf("%d %d", &a, &b);
	
	for(i=1;i*i<=a;i++){
		if(a%i==0){
			rest_a[j]= i;
			rest_inv[j++] = a/i;
		}
	}temp = j-1;
	
	if(rest_a[j-1]==rest_inv[j-1]) temp--;
	
	while(temp>=0) rest_a[j++] = rest_inv[temp--];
	
	j=0;
	
	for(i=1;i*i<=b;i++){
		if(b%i==0){
			rest_b[j]= i;
			rest_inv[j++] = b/i;
		}
	}temp = j-1;
	
	if(rest_b[j-1]==rest_inv[j-1]) temp--;
	
	while(temp>=0) rest_b[j++] = rest_inv[temp--];
	
	a=0; b=0; j=0;
	while(1){
		if(rest_a[a]=='\0')	{while(rest_b[b]!='\0') rest[j++] = rest_b[b++]; break;}
		if(rest_b[b]=='\0')	{while(rest_a[a]!='\0') rest[j++] = rest_a[a++]; break;}
		if(rest_a[a] < rest_b[b]) rest[j++] = rest_a[a++];
		else if(rest_a[a] > rest_b[b]) rest[j++] = rest_b[b++];
		else{
			rest[j++] = rest_a[a];
			a++; b++;
		}
	}
	
	for(i=0;i<j;i++){
		printf("%d ", rest[i]);
	}
}
