I wrote a code that can convert rank to mmr. To do this, we substitute the rank in the 1st or 2nd formula (depending on the rank). And we can see how the rank and MMR correlate. For high ranks, the error is 100-300 MMR (> rank =  <accuracy: it depends on the top, as well as a limited amount of information about the ranks, I had 15 of them). 

But in general, this can be easily corrected and the formulas can be made even more accurate, although they are already quite accurate in calculating MMR.

### MAIN
Accuracy: 95-98% | If Rank <=460

Accuracy: 98-99% | If Rank>460

### Example:
Rank 131 | ~ 11000-11150 MMR
MMR = -448.45658 * ln(9264.01245 * 131) + 17242.22337 = 10959.75 MMR
Accuracy: 98.3% 

Rank 1674 | ~ 8245 MMR
MMR = -1248.02749 * ln(1861.20536 * 1674) + 27052.29973 = 8391 MMR
Accuracy: 98.2% 

### Image for example: 
![image](https://github.com/dotabod/backend/assets/91318807/3f426227-5e00-4a10-9008-d1c6ad2b8763)
