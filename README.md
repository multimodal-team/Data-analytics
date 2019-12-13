# Data-Analytics
Provide some useful tools for analizing data from charlearn NLP.

### 12.13 Update
- Bugs Fixed: The testing acc is 0.2, which means original data was wrong. After debuging I found csv misunderstanded the filename which prefix is '-' as a format. When did combine operations, it throw away 50 above datas.
- Add TryDiscretization

### Raw data
Raw data which combined everything incuding 'VideoName', 'Labels', 'context'.  
TrainSet length is 6000 and corrresponed dev is 2000.

### TryDiscretization
- Unevenly discretizate the label of dataset into 5 class
- Not make any sence, cause result is still disributed at center
  
  
Todo Memo
---

### Huber-loss
Using huber-loss

### Personality dictionary
Recommended to investigate the Personality dictionary which deeps in lingustic to preduce how words affect to the personality.
The website is 

#### Early fusion

