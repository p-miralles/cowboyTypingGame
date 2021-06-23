import sys
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import Qt
from PySide2.QtCore import QThread, QFile
from PySide2.QtUiTools import QUiLoader

from pathlib import Path
import json

from tcpclient import TCPClient
from udp import UDPServer

targetIP= '25.107.188.70' #Pablo
#targetIP= '25.52.119.35'
#targetIP= '25.57.178.133' #Tomas
#targetIP = '192.168.100.6' #noblex lan
targetPort = 4004

cmd_getRooms = '{"cmd":"getRooms"}'
cmd_selectRoom = '{"cmd":"selectRoom","roomID",x}'
cmd_startGame = '{"cmd":"startGame"}'
cmd_leaveRoom = '{"cmd":"leaveRoom"}'
cmd_update = '{"cmd":"update","Name":"Jack","Status":"Playing","Score":5000}'

QtWidgets.QApplication.setAttribute(
    QtCore.Qt.AA_EnableHighDpiScaling, True)  # enable highdpi scaling
QtWidgets.QApplication.setAttribute(
    QtCore.Qt.AA_UseHighDpiPixmaps, True)  # use highdpi icons


class MyApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyApp, self).__init__()
        # super(QtWidgets.QMainWindow, self).__init__()

        self.status_message = ['● Idle', '● Idle', '● Idle', '● Idle', '● Idle', '']

        config_file = Path('config.json')
        # config_file = open('config.json', 'w+')
        if config_file.exists():
            self.config = json.load(open('config.json', 'r'))
        else:
            self.config = dict()
            json.dump(self.config, open('config.json', 'w+'))

        """Load UI"""
        ui_file_name = "mainwindow.ui"
        ui_file = QFile(ui_file_name)
        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        # self.ui = uic.loadUi('mainwindow.ui', self)
        ui_file.close()
        self.init_ui()

        self.udp_send = UDPServer(
            '0.0.0.0',
            1234)

        #self.ui.show()
        print("Starting APP")
        self.on_tcp_client_connect_button_clicked()
        getRoomsCMD = '{"cmd":"getRooms"}'
        self.tcp_client.send(getRoomsCMD)
        self.send_update_to_server("Tom","Playing",5500)

    def save_config(self):
        try:
            json.dump(self.config, open('config.json', 'w+'))
        except PermissionError as err:
            pass

    def init_ui(self):

        # TCP Client
        tcp_client_ip = self.config.get('TCP_Client_IP', '127.0.0.1')
        tcp_client_port = self.config.get('TCP_Client_Port', '1234')

        # UDP
        udp_listen_port = self.config.get('UDP_Listen_Port', '1234')
        udp_target_ip = self.config.get('UDP_Target_IP', '127.0.0.1')
        udp_target_port = self.config.get('UDP_Target_Port', '1234')

    # TCP Client
    def on_tcp_client_connect_button_clicked(self):
            print("Connecting to "+str(targetIP))
            self.tcp_client_thread = QThread()
            self.tcp_client = TCPClient(targetIP,targetPort)

            self.tcp_client_thread.started.connect(self.tcp_client.start)
            self.tcp_client.status.connect(self.on_tcp_client_status_update)
            self.tcp_client.message.connect(self.on_tcp_client_message_ready)

            self.tcp_client.moveToThread(self.tcp_client_thread)

            self.tcp_client_thread.start()

            #self.config['TCP_Client_IP'] = self.ui.lineEdit_TcpClientTargetIP.text()
            #self.config['TCP_Client_Port'] = self.ui.lineEdit_TcpClientTargetPort.text()
            #self.save_config()

           # self.tcp_client.close()

    def on_tcp_client_status_update(self, status, addr):
        if status == TCPClient.STOP:
            self.tcp_client.status.disconnect()
            self.tcp_client.message.disconnect()

            self.tcp_client_thread.quit()

            #self.status_message[0] = '● Idle'
            #self.on_tab_changed(0)

        elif status == TCPClient.CONNECTED:
            print('Connected to ' +\
                   str(targetIP) +\
                     ':'+str(targetPort))
           
    def on_tcp_client_message_ready(self, source, msg):
        print(source)
        print(msg)

    def on_tcp_client_message_send(self,data):
        self.tcp_client.send(data)
        
    def on_udp_server_message_ready(self, source, msg):
        print(source)
        print(msg)

    def on_udp_message_send(self):
        self.udp_send.send(targetIP,targetPort)
        self.config['UDP_Target_IP'] = targetIP
        self.config['UDP_Target_Port'] = targetPort
        self.save_config()

    def send_update_to_server(self,name,status,score):
        update = '{"cmd":"update","Name":"'+str(name)+'","Status":"'+str(status)+'","Score":'+str(score)+'}'
        self.tcp_client.send(update)




if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    # window.show()
    sys.exit(app.exec_())
