def func():
	for i in range (0,10):
		yield
		print(i)
		
		if(i == 5):
			return 0;


func()
print("---------")
func()