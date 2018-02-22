from django import forms
from django.utils.translation import gettext_lazy as _
from froala_editor.widgets import FroalaEditor
from codemirror2.widgets import CodeMirrorEditor
import os
from django.conf import settings

from .models import Okapi_bm25, Jelinek_mercer, Dirichlet_prior, Pivoted_length, Absolute_discount, Code, Own_retrieval


class bm25Form(forms.ModelForm):
    class Meta:
        model = Okapi_bm25
        fields = ('p_k1', 'p_b', 'p_k3',)
        labels = {
            'p_k1': _('Doc term smoothing'),
            'p_b': _('Length normalization'),
            'p_k3': _('Query term smoothing'),
        }


class jmForm(forms.ModelForm):
    class Meta:
        model = Jelinek_mercer
        fields = ('p_lambda',)
        labels = {
            'p_lambda': _('Lamda'),
        }


class dpForm(forms.ModelForm):
    class Meta:
        model = Dirichlet_prior
        fields = ('p_mu',)
        labels = {
            'p_mu': _('Mu'),
        }


class plForm(forms.ModelForm):
    class Meta:
        model = Pivoted_length
        fields = ('p_s',)
        labels = {
            'p_s': _('Pivoted length normalization '),
        }


class adForm(forms.ModelForm):
    class Meta:
        model = Absolute_discount
        fields = ('p_delta',)
        labels = {
            'p_delta': _('Absolute discounting parameter '),
        }


class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ('text',)


class OwnRetrievalForm(forms.Form):
    sample = ''
    sample_file = 'IRLab/uploads/sample.py'
    cfg = os.path.join(settings.BASE_DIR, sample_file)
    with open(sample_file) as f:
        sample = f.readlines()

    sample = ''.join(sample)

    code = forms.CharField(
        label='Or implement your retrieval function here',
        initial=sample,
        widget=CodeMirrorEditor(options={'mode': 'python', 'theme': 'eclipse', 'lineNumbers': True, }))