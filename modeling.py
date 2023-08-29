from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neighbors import KNeighborsClassifier


#this function creates a random forest model and prints train and validation accuracy
def r_forest(X_train, y_train, X_val, y_val):
    
    rf = RandomForestClassifier(max_depth=5, random_state=42)
    
    rf.fit(X_train, y_train)

    print(f'Train Accuracy = {rf.score(X_train, y_train)}')

    print(f'Validate Accuracy = {rf.score(X_val, y_val)}')
    

#this function creates a decision tree model and prints train and validation accuracy
def d_tree(X_train, y_train, X_val, y_val):
    
    dt = DecisionTreeClassifier(max_depth=5, random_state=42)
    
    dt.fit(X_train, y_train)

    print(f'Train Accuracy = {dt.score(X_train, y_train)}')

    print(f'Validate Accuracy = {dt.score(X_val, y_val)}')
    

#this function creates a K-Nearest Neighbor model and prints train and validation accuracy    
def knn_m(X_train, y_train, X_val, y_val):
    
    knn = KNeighborsClassifier(n_neighbors=5)
    
    knn.fit(X_train, y_train)

    print(f'Train Accuracy = {knn.score(X_train, y_train)}')

    print(f'Validate Accuracy = {knn.score(X_val, y_val)}')


#this function prints out test accuracy of a decision tree module
def d_tree_test(X_train, y_train, X_test, y_test):
    
    dt = DecisionTreeClassifier(max_depth=5, random_state=42)
    
    dt.fit(X_train, y_train)

    print(f'Test Accuracy = {dt.score(X_test, y_test)}')