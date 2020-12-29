from pywinauto import application
import os, time

# 프로세스 종료 명령 taskkill로 실행 중인 크레온 관련 프로세스(coStarter.exe, CpStart.exe, DibServer.exe)를 종료했다. 인수는 '이미지명이 coStarter로 시작하는 프로세스(/IM coStarter*)를 강제로(/F) 종료하라(/T)'는 뜻이다. 만일 실행 중인 크레온 관련 프로세스가 없으면 해당 프로세스를 찾을 수 없다고 오류 메시지가 발생할 수 있으나, 실행중인 프로세스를 찾아서 종료하는 것이 목적이므로 프로세스를 못 찾는다는 오류 메시지는 무시해도 된다. 
os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('taskkill /IM DibServer* /F /T')
# WMIC(Windows Management Instrumentation Command-line)는 윈도우 시스템 정보를 조회하거나 변경할 때 사용하는 명령이다. 크레온 프로그램은 가제 종료 신호를 받으면 확인 창을 띄우기 때문에 강제로 한 번 더 프로세스를 종료해야 한다. 
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
os.system('wmic process where "name like \'%DibServer%\'" call terminate')

time.sleep(5)
app = application.Application()
# 파이윈오토를 이용하여 크레온 프로그램(coStarter.exe)을 크레온 플러스 모드(/prj:cp)로 자동으로 시작한다. 사용자 ID, 암호, 공인인증서 암호를 실행 인수로 지정해 놓으면 로그인 창에 자동으로 입력된다. (* 표시를 자신의 정보로 대체하기 바란다. )
app.start('C:\CREON\STARTER\coStarter.exe /prj:cp/id:**** /pwd:**** /pwdcert:**** /autostart')
time.sleep(60)