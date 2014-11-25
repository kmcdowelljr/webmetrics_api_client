# This client is designed to easily interact with Webmetrics' API.
# Copyright (C) 2014-2015  Keith McDowell
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
__author__ = 'kmcdowel'

import sys
import connection
import wm_api_client
from PyQt5.QtCore import  pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class editLineBox(QLineEdit):
  def __init__(self, parent =None):
   print 'Enter editlineBox'
   super(editLineBox,self).__init__(parent)
   self.userName = QLineEdit()
   #self.userName.setReadOnly(True)
   self.userName.text()
   u = self.userName
   print u



if __name__ == '__main__':
 app = QApplication(sys.argv)
 window = loadUi('uiSimpleClient.ui')
 getUser = editLineBox()
 window.show()
 getUser.show()
 print getUser
 sys.exit(app.exec_())


