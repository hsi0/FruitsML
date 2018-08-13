
from sklearn import tree
features=[[140,1],[130,1],[150,0],[170,0]]
labels=['Apple','Avocado','Banana','Orange']
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
print(clf.predict([[130,1]]+[[170,0]]))