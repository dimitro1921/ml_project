9. This problem involves the OJ data set which is part of the ISLP
package.

(a) Create a training set containing a random sample of 800 obser-
vations, and a test set containing the remaining observations.

(b) Fit a tree to the training data, with Purchase as the response
and the other variables as predictors. What is the training error
rate?

(c) Create a plot of the tree, and interpret the results. How many
terminal nodes does the tree have?

(d) Use the export_tree() function to produce a text summary of
the fitted tree. Pick one of the terminal nodes, and interpret the
information displayed.

(e) Predict the response on the test data, and produce a confusion
matrix comparing the test labels to the predicted test labels.
What is the test error rate?

(f) Use cross-validation on the training set in order to determine
the optimal tree size.

(g) Produce a plot with tree size on the x-axis and cross-validated
classification error rate on the y-axis.

(h) Which tree size corresponds to the lowest cross-validated classi-
fication error rate?

(i) Produce a pruned tree corresponding to the optimal tree size
obtained using cross-validation. If cross-validation does not lead
to selection of a pruned tree, then create a pruned tree with five
terminal nodes.

(j) Compare the training error rates between the pruned and un-
pruned trees. Which is higher?

(k) Compare the test error rates between the pruned and unpruned
trees. Which is higher?