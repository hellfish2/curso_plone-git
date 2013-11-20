
from german import German

class John(German):

	def suma(self):

	  self.variable1 = 2
          self.variable2 = 2
          self.total = self.variable1 + self.variable2

        def imp_total(self):
          print "el total es:", self.total

j = John()
j.suma()
j.imp_total()

	

