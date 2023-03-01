import sketch
import pandas as pd

#sales_data = pd.read_csv("https://gist.githubusercontent.com/bluecoconut/9ce2135aafb5c6ab2dc1d60ac595646e/raw/c93c3500a1f7fae469cba716f09358cfddea6343/sales_demo_with_pii_and_all_states.csv")
#res=sales_data.sketch.ask("Can you give me friendly names, Business descriptions, and flag (Yes/No) tell if there is any PII information for each column? (output as JSON)")

diabetes_data = pd.read_csv("C:\Divya_documents\Python_learning\Edureka_Python_Course\diabetes.csv")
print(diabetes_data.sketch.ask("Can you give me friendly names, Business descriptions, and flag (Yes/No) tell if there is any PII information for each column? (output as JSON)")
)
#C:\Divya_documents\Python_learning\Edureka_Python_Course

#print(res)