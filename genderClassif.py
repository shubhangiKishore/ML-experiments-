# based on the height,weight ,shoe size, make a gender classifier using multiple classifiers in scikitlearn 
from sklearn.svm import SVC

x = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], ]

y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female']

new_x = [[159, 55, 37], [171, 75, 42], [181, 85, 43]]
res_y = ['female', 'male', 'male']


fit_svc = SVC().fit(x,y)
res_svc = fit_svc.predict(new_x)
print(res_svc)

