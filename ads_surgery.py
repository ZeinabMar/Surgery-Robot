import win32api
import pyads
import time
import socket
import threading
import sys
import csv
import win32gui, win32con
ToMinimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(ToMinimize , win32con.SW_SHOWMINIMIZED)

with open('C:\RequiredFiles\LocalNetID') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        NetID = row[0]
        break

# Deactivate close button


def on_exit(signal_type):
    try:
        ads.Close_ads()
    except:
        pass
    try:
        tcp.Close_tcp()
    except:
        pass


win32api.SetConsoleCtrlHandler(on_exit, True)


class ADS_CONNECTION():
    def __init__(self, netID, port):
        self.netID = netID  # string type
        self.port = port  # int type
        self.recieved_data = []
        self.ads = []

    def Ads_connect(self):
        ads = pyads.Connection(self.netID, self.port)
        self.ads = ads

    def Open_ads(self):
        self.ads.open()

    def Close_ads(self):
        self.ads.close()

    def Read_data(self):
        try:
            xleft = self.ads.read_by_name(
                'Global.TeleDataSlave.HL_X', pyads.PLCTYPE_LREAL)           #xleft = 120.0 + xleft*120.0
        except:
           self.ads.close()
           return xleft,yleft,xright,yright,Clutch,SlvCntrl,LeftLoadCell,RightLoadCell,SystemState,LeftConstWrist,RightConstWrist,PositionSound,er,RGraspLck,LGraspLck
       
        xleft = self.ads.read_by_name(
            'Global.TeleDataSlave.HL_X', pyads.PLCTYPE_LREAL)
        yleft = self.ads.read_by_name(
            'Global.TeleDataSlave.HL_Y', pyads.PLCTYPE_LREAL)
        xright = self.ads.read_by_name(
            'Global.TeleDataSlave.HR_X', pyads.PLCTYPE_LREAL)
        yright = self.ads.read_by_name(
            'Global.TeleDataSlave.HR_Y', pyads.PLCTYPE_LREAL)
        SlvCntrl = self.ads.read_by_name(
            'Global.TeleDataSlave.SlaveCntrl', pyads.PLCTYPE_BOOL)
        LeftLoadCell = self.ads.read_by_name(
            'Global.TeleDataSlave.HL_LoadCell', pyads.PLCTYPE_LREAL)
        RightLoadCell = self.ads.read_by_name(
            'Global.TeleDataSlave.HR_LoadCell', pyads.PLCTYPE_LREAL)
        SystemState = self.ads.read_by_name(
            'MAIN.SystemState', pyads.PLCTYPE_INT)
        LeftConstWrist = self.ads.read_by_name(
            'Global.TeleDataSlave.HL_ConstWrist', pyads.PLCTYPE_BOOL)
        RightConstWrist = self.ads.read_by_name(
            'Global.TeleDataSlave.HR_ConstWrist', pyads.PLCTYPE_BOOL)
        Clutch = self.ads.read_by_name('Global.Clutch', pyads.PLCTYPE_BOOL)
        SemiClutch = self.ads.read_by_name(
            'Global.SemiClutch', pyads.PLCTYPE_BOOL)
        Clutch = Clutch or SemiClutch
        LeftVirtualClutch = self.ads.read_by_name(
            'Global.TeleDataSlave.HL_VirtualClutch', pyads.PLCTYPE_BOOL)
        RightVirtualClutch = self.ads.read_by_name(
            'Global.TeleDataSlave.HR_VirtualClutch', pyads.PLCTYPE_BOOL)
        LeftSafetyButton = self.ads.read_by_name(
            'MAIN.ML.SafetyButton', pyads.PLCTYPE_BOOL)
        RightSafetyButton = self.ads.read_by_name(
            'MAIN.MR.SafetyButton', pyads.PLCTYPE_BOOL)
        Distance = self.ads.read_by_name(
            'Global.Distance', pyads.PLCTYPE_LREAL)
        scale = self.ads.read_by_name(
            'Global.Scale', pyads.PLCTYPE_LREAL)
        timer = 1# self.ads.read_by_name(
           # 'Global.counter', pyads.PLCTYPE_INT)
        RGraspLck =  self.ads.read_by_name(
            'MAIN.MR.GrspLck', pyads.PLCTYPE_BOOL)
        LGraspLck =  self.ads.read_by_name(
            'MAIN.ML.GrspLck', pyads.PLCTYPE_BOOL)
        ArmsAreClosToEachother =  self.ads.read_by_name(
            'Global.TeleDataSlave.ArmsAreClosToEachother', pyads.PLCTYPE_BOOL)
        RightArmIsCloseToLens =  self.ads.read_by_name(
            'Global.TeleDataSlave.RightArmIsCloseToLens', pyads.PLCTYPE_BOOL)
        LeftArmIsCloseToLens =  self.ads.read_by_name(
            'Global.TeleDataSlave.LeftArmIsCloseToLens', pyads.PLCTYPE_BOOL)

        
        er = 0.0
        PositionSound= 0.0

        self.recieved_data = {'xleft': xleft, 'yleft': yleft, 'xright': xright, 'yright': yright, 'Clutch': Clutch, 'LeftVirtualClutch': LeftVirtualClutch,
                              'RightVirtualClutch': RightVirtualClutch, 'SlvCntrl': SlvCntrl,
                              'LeftLoadCell': LeftLoadCell, 'RightLoadCell': RightLoadCell, 'SystemState': SystemState,
                              'LeftConstWrist': LeftConstWrist, 'RightConstWrist': RightConstWrist, 'Distance': Distance, 'scale':scale,'RGraspLck':RGraspLck,'LGraspLck':LGraspLck,'ArmsAreClosToEachother':ArmsAreClosToEachother,'RightArmIsCloseToLens':RightArmIsCloseToLens,'LeftArmIsCloseToLens':LeftArmIsCloseToLens,'er':er}

    def Write_data(self, x):
        self.ads.write_by_name('Global.TeleDataMaster.RaspberryScale', x, pyads.PLCTYPE_LREAL)
    def Write_data2(self, x):
        self.ads.write_by_name('Global.TeleDataMaster.RaspberryNotConnected', x, pyads.PLCTYPE_BOOL)


class TCP_CONNECTION():
    def __init__(self, port):
        self.header = 256
        self.SERVER = socket.gethostbyname('192.168.17.2')
        self.port = port  # int type
        self.ADDR = (self.SERVER, self.port)
        self.format = 'utf_8'
        self.DISCONNECT_MASSAGE = "!DISCONNECT"
        self.server = []
        self.conn = []
        self.addr = []
        self.string_data = []
        self.scaleTemp = 1

    def TCP_connect(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #socket.setsocketopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        socket.setdefaulttimeout(5)
        self.server.bind(self.ADDR)
        print(self.ADDR)
    def TCP_listen(self):
        self.server.listen(10)
        self.conn, self.addr = self.server.accept()
        self.server.settimeout(2)

    def Send_data(self, S,T):
        self.Sum_data(S,T)
        self.sring_data = S
        self.conn.send(self.string_data.encode(self.format))
    
    def dataspilit(data):
        a=data.split(str.encode("[END]"))
        n=0
        if datarecv!=str.encode(""):
            while n<1:
                b[n]=a[n].split(str.encode("/"))
                n=n+1
            #return b

    def Recieve_data(self):
        
        
        datarecv=self.conn.recv(28)
        #datarecv=datarecv.decode('utf_8')
        
        #return datarecv
        a=datarecv.split(str.encode("[END]"))
        n=0
        b=[0]
        if datarecv!=str.encode(""):
            
            while n<1:
                
                b[n]=a[n].split(str.encode("/"))
                n=n+1
        return b
        

        #if datarecv!=str.encode(""):
           # b=dataspilit(datarecv)
        #self.scTemp = float(self.conn.recv(64).decode(self.format))

    def Sum_data(self, S,T):
        string_data = str(S['xleft'])+"/"+str(S['yleft'])+"/"+str(S['xright'])+"/"+str(S['yright'])+"/"+str(int(S['Clutch']))+"/"+str(int(S['SlvCntrl']))+"/"+str(S['LeftLoadCell'])+"/"+str(
            S['RightLoadCell'])+"/"+str(S['SystemState'])+"/"+str(int(S['LeftConstWrist']))+"/"+str(int(S['RightConstWrist']))+"/"+str(int(S['LeftVirtualClutch']))+"/"+str(int(S['RightVirtualClutch']))+"/"+str(S['Distance'])+"/"+str(S['scale'])+"/"+str(int(S['RGraspLck']))+"/"+str(int(S['LGraspLck']))+"/"+str(int(S['ArmsAreClosToEachother']))+"/"+str(int(S['RightArmIsCloseToLens']))+"/"+str(int(S['LeftArmIsCloseToLens']))+"/"+str(S['er'])+"[END]"
        self.string_data = string_data
        #print(string_data)

    def Close_tcp(self):
        self.conn.close()


# MAIN
stage = 1
while 1 > 0:
    # Create Object from Classes
    if stage == 1:
        try:
            ads = ADS_CONNECTION(NetID, 851)
            #ads = ADS_CONNECTION('192.168.120.146.1.1', 851)
            tcp = TCP_CONNECTION(9996)
            print("[GENERATE OBJECTS] DONE (stage 1)")
            stage = stage + 1
            e=0
        except:
            print("[ERROR] Error in create object from classes (stage 1)")
            time.sleep(1)

    # Create ads Connection
    elif stage == 2:
        try:
            
            ads.Ads_connect()
            print("[GENERATE ADS CONNECTION] DONE (stage 2)")
            stage = stage + 1
        except:
            print("[ERROR] Error in generate ADS connection (stage 2)")
            time.sleep(1)

    # Open Connection
    elif stage == 3:
        try:
            ads.Open_ads()
            print("[OPEN ADS CONNECTION] DONE (stage 3)")
            stage = stage + 1
        except:
            print("[ERROR] Error in open ADS connection (stage 3)")
            time.sleep(1)

    # Create TCP Connection
    elif stage == 4:
        try:
            tcp.TCP_connect()
            print("[GENERATE TCP CONNECTION] DONE (stage 4)")
            stage = stage + 1
        except:
            print("[ERROR] Error in generate TCP connection (stage 4)")
            time.sleep(1)

    # Waiting for Server to Find Client
    elif stage == 5:
        try:

            print(f"[LISTENING] Server is listening on {tcp.SERVER} (stage 5)")
            tcp.TCP_listen()
      
            print("[STARTING] server is starting... (stage 5)")
            print(f"[NEW CONNECTION] {tcp.addr} CONNECTED (stage 5).")
            stage = stage + 1
        except:
            print("[ERROR] Error in listening to client (stage 5)")
           
            print("please chek your connection or cable......")
            time.sleep(1)
            print("Make sure the the program on rasbery is runing")
            time.sleep(1)
            print("Retrying for connection....")
            ads.Close_ads()
            tcp.Close_tcp()
            stage=2
            print("conection stablish sending data...........")
            

    # Data Exchange Between Twincat and Python Server
    elif stage == 6:
        try:
            ads.Read_data()
            stage = 7
        except:

            print("[ERROR] Error in ADS exchanging data (stage 6)")
            
            print("please chek your connection or cable......")
            time.sleep(1)
            print("Make sure the the program on rasbery is runing")
            time.sleep(1)
            print("Retrying for connection....")
            ads.Close_ads()
            tcp.Close_tcp()
            stage=2
            print("conection stablish sending data...........")
           

    # Data Exchange Between Python Server and Python Client
    elif stage == 7:

        try:
            tcp.Send_data(ads.recieved_data,tcp.addr)
            
        
            b=tcp.Recieve_data()
            
            if b[0]!=0:
                
                ads.Write_data(float(b[0][0].decode('utf_8')))
        
            ads.Write_data2(0)
            if e !=0:
                print("problem has been solved (stage 7)")
            e=0
            stage = 6
            

        except:
            print("[ERROR] Error in TCP exchanging data (stage 7)")
            e=1
            print("please chek your connection or cable......")
            time.sleep(1)
            print("Make sure the the program on rasbery is runing")
            time.sleep(1)
            print("Retrying for connection....")
            try:
                ads.Write_data2(1)
                ads.Close_ads()
                tcp.Close_tcp()
                stage=2
                print("conection stablish sending data...........")
            except:
                ads.Close_ads()
                tcp.Close_tcp()
                stage=2
                print("conection stablish sending data...........")
            

            

