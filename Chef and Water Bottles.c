#include <stdio.h>

int main(void) {
	// your code goes here
	int t,sum=0;
	scanf("%d",&t);
	while(t--){
	    int n,x,k;
	    scanf("%d %d %d",&n,&x,&k);
	    sum = k/x;
	    if(sum >= n){
	        printf("%d\n",n);
	    }
	    else printf("%d\n",sum);
	}
	return 0;
}
