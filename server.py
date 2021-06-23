import socket
import threading
import cv2
import numpy

serverIP = input("Enter your friend's IP Address : ") 
serverPort = int(input("Enter your friend's Port No : "))
cap = cv2.VideoCapture(0)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("",serverPort))
os.system("cls")
print("Connected to: "+ serverIP + ":" + str(serverPort))
print("\n\n")

def send():
  while True:
    #MessageToBeSendEncode()
    ret,photo = cap.read()
    p_data = cv2.imencode('.jpg',photo)[1].tobytes()
    mbsend = p_data.encode()
    s.sendto(mbdata,(serverIP,serverPort))
cv2.destroyAllWindows()

def rec():
  while True: 
    #MessageToBeSendEncode()
    recvdata = s.recvfrom(4*1024)
    darray = np.frombuffer(data,np.uint8)
    photo = cv2.imdecode(darray,cv2.IMREAD_COLOR)
    if type(photo) is type(none):
        pass
    else:
        cv2.imshow('',photo)
        if cv2.waitKey(10)==13:
            break
            
cv2.destroyAllWindows()
cap.release()


t1 = threading.Thread(target=send)
t2 = threading.Thread(target=rec)
t1.start()
t2.start()
