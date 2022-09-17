#include <stdio.h>

int main(void) {
	// your code goes here
	int t; 
	scanf("%d",&t);
	while(t--){
	    int a;
	    scanf("%d",&a);
	    if(a <= 15)
	        printf("Yes\n");
	    else printf("No\n");
	}
	return 0;
}
