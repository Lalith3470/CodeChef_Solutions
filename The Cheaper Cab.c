#include <stdio.h>

int main(void) {
	// your code goes here
	int n;
	scanf("%d",&n);
	while(n--){
	    int a,b;
	    scanf("%d %d",&a,&b);
	    if(a > b)
	        printf("SECOND\n");
	    else if(a == b)
	        printf("ANY\n");
	    else   printf("FIRST\n");
	}
	return 0;
}
