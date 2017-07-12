#!/usr/bin/python
# -*- coding: utf-8 -*-


from pysettings import conf

import pyforms.utils.tools as tools

if conf.PYFORMS_USE_QT5:
	from PyQt5 import uic

else:
	from PyQt4 import uic

from pyforms.gui.Controls.ControlBase import ControlBase


class ControlNumber(ControlBase):
	def __init__(self, label="", default=0, minimum=0, maximum=100, decimals=0):
		self._min = minimum
		self._max = maximum
		self._decimals = decimals
		self._updateSpinner = True
		ControlBase.__init__(self, label, default)

	def init_form(self):
		control_path = tools.getFileInSameDirectory(__file__, "number.ui")
		self._form = uic.loadUi(control_path)
		self.label = self._label
		self.value = self._value
		self.form.label.setAccessibleName('ControlNumber-label')
		self.form.spinBox.valueChanged.connect(self.value_changed)
		self.form.spinBox.setDecimals(self._decimals)
		self.min = self._min
		self.max = self._max

	def value_changed(self, value):
		self._updateSpinner = False
		self.value = value
		self._updateSpinner= True

	############################################################################
	############ Properties ####################################################
	############################################################################

	@property
	def label(self): return self.form.label.text()

	@label.setter
	def label(self, value): self.form.label.setText(value)

	@property
	def value(self):
		self._value = self.form.spinBox.value()
		return self._value

	@value.setter
	def value(self, value):
		ControlBase.value.fset(self, value)
		if self._updateSpinner:
			self.form.spinBox.setValue(value)

	@property
	def min(self): return self.form.spinBox.minimum()

	@min.setter
	def min(self, value): self.form.spinBox.setMinimum(value)

	@property
	def max(self): return self.form.spinBox.maximum()

	@max.setter
	def max(self, value): self.form.spinBox.setMaximum(value)

	@property
	def decimals(self): return self.form.spinBox.decimals()

	@decimals.setter
	def decimals(self, value): self.form.spinBox.setDecimals(value)
