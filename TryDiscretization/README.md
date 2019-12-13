# Discrete Label(Using Bert-model)
This trial aims to mapping continuous label into discrete class.Used 0-4 as five label classification.All classes are 0.2 distence
except for :  
0.4 < label < 0.55 as class 2  
0.55 < label < 0.7 as class 3  

### Results
Evenly divide data makes result even.  
For example, There are 35% of label 2 in DataSet. Then model **Acc is 0.38**  
Confusely, model love predicting label 2.  
  
Consider the prediction of regression, model also love predicted data in range 0.4-0.6.
That trail don't make any sence

12.13
