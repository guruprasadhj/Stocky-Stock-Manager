from django import forms
from .models import Stock




class StockCreateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category', 'item_name', 'quantity']




class StockSearchForm(forms.ModelForm):
#	def __init__(self,*args,**kwargs):
#		super(StockSearchForm,self).__init__(*args,**kwargs)
#		self.fields['category'].required = False
#		self.fields['item_name'].required = False
	export_to_CSV = forms.BooleanField(required =False)
	class Meta:
   		model = Stock
   		fields = ['category', 'item_name']
   		widgets = {
   		'category': forms.Select(attrs={'class':'form-select form-select-lg mb-3','placeholder':'Example input placeholder'}),
   		'item_name':forms.TextInput(attrs={'class':'fform-label','z-index':'-1'})
   		}

class StockUpdateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category', 'item_name', 'quantity']

