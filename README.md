# MMS_Syntactical
Syntactical approach to identifying MMS data.

## Input/Output
- Assumes sourced data from OCR tool (e.g. Texteract).
- Predicts whether each identification number is a model or serial number. 

## Functionality
- Start with huge dataset of 15000-20000 entries, and extract all serial and model numbers.
- Narrow down to about 1800 entries by only taking model/serial numbers that appeared 2 or more times.
- Convert reduced dataset into multiple columns. The first column would identify the row as a model or serial number.
  The second column and beyond would each contain the scaled ASCII value of a single character in the number.
- Separate the scaled, reduced dataset into a training set and testing set. The training set is fed to the model with some
  hyperparameters such as # of intermediate layers of the neural network, what activation functions to use (e.g. sigmoid, softmax),
  how many neurons to use, etc.
  
## Issues
- Not enough data to properly train on such a wide array of identification numbers.
- Overfitting.
- There is an imbalance between the ratio of model and serial numbers (there are simply far more model numbers than serial numbers).
   -> as a direct result of this, it just tries to predict model number more frequently because are more model numbers.
