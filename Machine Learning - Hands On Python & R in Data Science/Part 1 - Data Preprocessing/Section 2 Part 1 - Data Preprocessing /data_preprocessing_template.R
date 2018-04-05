# Data Preprocessing Template


# Importing the dataset
dataset = read.csv('Data.csv') #USE
#dataset = dataset[ , 2:3] #FOR FUTURE USE

# Taking care of the missing data
dataset$Age = ifelse(is.na(dataset$Age), 
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age
                     )

dataset$Salary = ifelse(is.na(dataset$Salary), 
                     ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Salary
                     )

# Encoding categorical data
dataset$Country = factor(dataset$Country,
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1, 2, 3)
                         )

dataset$Purchased = factor(dataset$Purchased,
                         levels = c('No', 'Yes'),
                         labels = c(0, 1)
                         )

# Splitting the dataset into the Training set and Testing set
# install.packages('package name') <- for installing packages
# library(libraryname) <-to include libraries
set.seed(123) #USE
split = sample.split(dataset$Purchased, SplitRatio = 0.8) #USE
training_set = subset(dataset, split == TRUE) #USE
test_set = subset(dataset, split == FALSE) #USE

# Feature Scaling
training_set[, 2:3] = scale(training_set[, 2:3]) #USE
test_set[, 2:3] = scale(test_set[, 2:3]) #USE