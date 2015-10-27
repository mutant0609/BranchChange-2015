from django import forms

from .models import Post

PREF = (
	('AE B.Tech','AE B.Tech'),
	('CL B.Tech','CL B.Tech'),
	('CE B.Tech','CE B.Tech'),
	('CS B.Tech','CS B.Tech'),
	('EE B.Tech','EE B.Tech'),
	('EP B.Tech','EP B.Tech'),
	('ME B.Tech','ME B.Tech'),
	('MM B.Tech','MM B.Tech'),
	('EE Dual Deg E1','EE Dual Deg E1'),
	('EE Dual Deg E2','EE Dual Deg E2'),
	('EN Dual Deg','EN Dual Deg'),
	('EP Dual Deg N1','EP Dual Deg N1'),
	('ME Dual Deg M2','ME Dual Deg M2'),
	('MM Dual Deg Y1','MM Dual Deg Y1'),
	('MM Dual Deg Y2','MM Dual Deg Y2'),
	('CL Dual Deg','CL Dual Deg'),
	('CH','CH'),
        ('None',''),

	)

CAT=(
	('GE','GE'),
	('OBC','OBC'),
	('SC','SC'),
	('ST','ST'),
	('PwD','PwD'),

	)


class PostForm(forms.Form):

	error_css_class = 'error'
	Roll_Number = forms.RegexField(label='Roll_Number',max_length=9,min_length=9,regex=r'^15[D0-9]*$')
	CPI = forms.DecimalField(max_value=10,min_value=0,max_digits=2,decimal_places=2)
	Pref1 = forms.ChoiceField(choices=PREF, required=True )
	Pref2 = forms.ChoiceField(choices=PREF, required=False )
	Pref3 = forms.ChoiceField(choices=PREF, required=False )
	Pref4 = forms.ChoiceField(choices=PREF, required=False )
	Pref5 = forms.ChoiceField(choices=PREF, required=False )
	Pref6 = forms.ChoiceField(choices=PREF, required=False )
	Pref7 = forms.ChoiceField(choices=PREF, required=False )
	Pref8 = forms.ChoiceField(choices=PREF, required=False )
	Pref9 = forms.ChoiceField(choices=PREF, required=False )
	Pref10 = forms.ChoiceField(choices=PREF, required=False )
	Pref11= forms.ChoiceField(choices=PREF, required=False )
	Pref12= forms.ChoiceField(choices=PREF, required=False )
	Pref13= forms.ChoiceField(choices=PREF, required=False )
	Pref14= forms.ChoiceField(choices=PREF, required=False )
	Pref15= forms.ChoiceField(choices=PREF, required=False )
	Pref16= forms.ChoiceField(choices=PREF, required=False )
	Pref17= forms.ChoiceField(choices=PREF, required=False )

	CurrentBranch = forms.ChoiceField(choices=PREF, required=True )
	def extra_answers(self):
		for name, value in self.cleaned_data.items():
			if name.startswith('custom_'):
				yield (self.fields[name].label, value)
	def __init__(self, *args, **kwargs):
		extra = kwargs.pop('extra')
		super(PostForm, self).__init__(*args, **kwargs)

		for i, question in enumerate(extra):
			self.fields['custom_%s' % i] = forms.CharField(label=question)





	class Meta:
		model = Post
		fields = ('Roll_Number','Name','CurrentBranch','CPI','Category','Pref1','Pref2','Pref3','Pref4','Pref5','Pref6','Pref7','Pref8','Pref9','Pref10','Pref11','Pref12','Pref13','Pref14','Pref15','Pref16','Pref17')
	#fields = ('Name','CurrentBranch','CPI','Category','Pref1','Pref2','Pref3','Pref4')

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )