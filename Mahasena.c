#include <stdio.h>

int main(void) {
	// your code goes here
	int n,evn=0,odd=0;
	scanf("%d",&n);
	for(int i =0; i<n; i++){
	    int a;
	    scanf("%d",&a);
	    if(a%2 == 0)
	        evn += 1;
	    else 
	        odd +=1;
	}
	if(evn > odd)
	        printf("READY FOR BATTLE\n");
	    else printf("NOT READY\n");
	return 0;
}
