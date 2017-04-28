def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    import numpy as np

    ### create classifier
    # TODO
    clf = GaussianNB()


    ### fit the classifier on the training features and labels
    #TODO
    clf.fit(features_train, labels_train)

    ### use the trained classifier to predict labels for the test features
    # TODO
    pred = clf.predict(features_test)

    a = 0.
    for i in range (0, len(pred)-1):
        if pred[i] == labels_test[i]:
            a += 1
    accuracy2 = a / len(pred)
    print accuracy2


    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example,
    ### where we just print the accuracy
    ### you might need to import an sklearn module
    # TODO
    # accuracy = clf.score(features_test, labels_test)
    accuracy = accuracy_score(pred, labels_test)
    return accuracy