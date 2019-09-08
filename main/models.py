from django.db import models

class Voucher(models.Model):
	voucher_code = models.CharField(max_length=8)
	discount = models.CharField(max_length=3)
	uses = models.IntegerField(default=0)

	def __str__(self):
		return self.voucher_code + ' - ' + self.discount + '%' + ' discount (Used ' + str(self.uses) +' times)'