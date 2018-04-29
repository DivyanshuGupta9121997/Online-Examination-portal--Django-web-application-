from tkinter import messagebox, scrolledtext, simpledialog
from tkinter import *
import random
import tkinter as tk
import classes.client as client
import classes.server as server
import sys
DEFAULT_PORT = 10000
class P2pChat(tk.Frame):
    def __init__(self, master=None):
        global DEFAULT_PORT
        
        master.wm_title("P2P Chat")
        master.protocol("WM_DELETE_WINDOW", self.close_app)
        
        tk.Frame.__init__(self, master)
        self.pack(fill=tk.BOTH, expand=1)
        self.createWidgets()
        
        if not messagebox.askyesno("", "Are you giving the test ?"):
            self.chat = server.Server(DEFAULT_PORT)
            self.ip_entry.delete(0, tk.END)
            self.ip_entry.insert(0, self.chat.host_ip)
            self.ip_entry.config(state='readonly')
            self.ip_entry.bind('<FocusIn>', self.remove_host_instr)
            
            self.port_entry.delete(0, tk.END)
            self.port_entry.insert(0, self.chat.host_port)
            self.port_entry.config(state='readonly')
            self.port_entry.bind('<FocusIn>', self.remove_host_instr)
            self.host_instr_label.pack(side=tk.LEFT)
        else:
            self.chat = None
            self.connect_btn.pack(side=tk.LEFT)
        master.bind('<Return>', self.send_msg)
        master.bind('<KP_Enter>', self.send_msg)
        self.display_new_msg()

    def connect_to_host(self):
        host_ip = self.ip_entry.get()
        if not self.validate_ip(host_ip):
            self.show_sys_msg("ip format is invalid")
            return
        port_entry_val = self.port_entry.get()
        if not self.validate_port(port_entry_val):
            msg = "port must be an integer where 1024 < port <= 65535"
            self.show_sys_msg(msg)
            return
        try:
            self.chat = client.Client(host_ip, int(port_entry_val))
            self.connect_btn.pack_forget()
            self.ip_entry.config(state='readonly')
            self.port_entry.config(state='readonly')
            self.send_msg1("Kindly Change YOUR NAME from DROP-DOWN menu")
        except Exception as e:
            msg = "Check the ip and port. Check host's firewall settings"
            self.show_sys_msg(repr(e) + '\n' + msg)
   
    def validate_ip(self, ip):
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            try:
                part = int(part)
                if part < 0 or part > 255:
                    return False
            except:
                return False
        return True

    def validate_port(self, port):
        try:
            port = int(port)
            if port > 1024 and port <= 65535:
                return True
            return False
        except:
            return False

    def createWidgets(self):
        global DEFAULT_PORT

        # Menu
        menubar = tk.Menu(self)
        
        menu = tk.Menu(menubar, tearoff=0)
        menu.add_command(label="Change user name", \
                         command=self.prompt_new_name)
        menu.add_separator()
        menu.add_command(label="Exit", command=self.close_app)
        menubar.add_cascade(label="Menu", menu=menu)

        self.master.config(menu=menubar)

        # IP and Port Frame
        ip_port_frame = tk.Frame(self, relief=tk.RAISED, bd=1)
        ip_port_frame.pack(side=tk.TOP, fill=tk.X)

        # IP Frame
        ip_frame = tk.Frame(ip_port_frame)
        ip_frame.pack(side=tk.LEFT)
        
        ip_label = tk.Label(ip_frame, text="ip:")
        ip_label.pack(side=tk.LEFT)
       
        vcmd = (self.register(self.validate_entry_len), '%P', '%W')
       
        ip_max_len = 15
        ip_entry = tk.Entry(ip_frame, width=ip_max_len, \
                            validate='key', vcmd=vcmd)
        ip_entry.pack(side=tk.LEFT)
        ip_entry.insert(0, '') 
        self.ip_entry = ip_entry

        # Port Frame
        port_frame = tk.Frame(ip_port_frame)
        port_frame.pack(side=tk.LEFT)

        port_label = tk.Label(port_frame, text="port:")
        port_label.pack(side=tk.LEFT)

        port_max_len = 5
        port_entry = tk.Entry(port_frame, width=port_max_len, \
                              validate='key', vcmd=vcmd)
        port_entry.pack(side=tk.LEFT)
        port_entry.insert(0, DEFAULT_PORT)
        self.port_entry = port_entry

        # Host Instruction Label
        self.host_instr_label = tk.Label(ip_port_frame, \
            text="<-- Tell your students this ip and port")
       
        # msg dialogue and entry frame 
        msg_frame = tk.Frame(self)
        msg_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        msg_window = scrolledtext.ScrolledText(msg_frame, height=10, width=80)
        msg_window.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        msg_window.config(state=tk.DISABLED)
        self.msg_window = msg_window

        # msg entry frame
        msg_entry_frame = tk.Frame(msg_frame, relief=tk.RAISED, bd=1)
        msg_entry_frame.pack(side=tk.BOTTOM, fill=tk.X)

        msg_entry = tk.Entry(msg_entry_frame)
        msg_entry.pack(side=tk.LEFT, fill=tk.X, expand=1)
        msg_entry.focus()
        self.msg_entry = msg_entry
        
        send_btn = tk.Button(msg_entry_frame)
        send_btn["text"] = "Send"
        send_btn["command"] = self.send_msg
        send_btn.pack(side=tk.RIGHT)
        
        #-------------start----------------------
        
    
        #set paper
        def setpaper():
            radio1['state']=DISABLED
            radio2['state']=DISABLED
            radio3['state']=DISABLED
            send_set_btn['state']=DISABLED
            top=tk.Toplevel(root)
            top.minsize(800,800)
            
            #overall frame
            f1=tk.Frame(top)
            f1.pack()
            label=tk.Label(f1)
            label.pack()

            #---stoptest-------
            def stoptest():
                global running
                running=False
                messagebox.showinfo("Submission Successful","You have completed your test in " + str(time[0]) + ":" + str(time[1]) + ":" + str(time[2]) )
                name=self.promptname()
                self.send_msg1("The "+name+" has completed the test")#--------------------------------------------------------------------------------------------------------
                
            ###-------------timer------------
            timeText = Label(f1, text="00 : 00 : 00",relief=RAISED)
            timeText.pack(anchor=NE,fill=X)
            
            submit_button=tk.Button(f1,text="Final Complete Submission",command=stoptest)
            submit_button.pack(side=BOTTOM,fill=X)
            
            global running
            running = False
            global time 
            time = [0,0,0] ##if time[1]==5

            def update_time():
                if(running):
                    global time
                    time[2]+=1
                    if(time[2]>=60):
                        time[2]=0
                        time[1]+=1
                    if(time[1]>=60):
                        time[1]=0
                        time[0]+=1
                    tempTime = str(time[0]) + ":" + str(time[1]) + ":" + str(time[2])
                    timeText.configure(text=tempTime)
                    
                    if(time[2]%2==0):
                        self.send_msg1("Time completed is : "+tempTime)
                    
                root.after(1000,update_time)
             ###timer
                
            if(self.var.get()!=0):
                d=tk.messagebox.askyesno("Confirmation","Are you ready to get into the test ?")
                #global running
                if d:
                    selection = "You selected the option " + str(self.var.get())
                    self.setsel(f1,self.var.get())
                    running=True
                    update_time()
                    
                    #-------------------------------------------------------------------------------------------
                    
                else:
                    selection="You are not ready yet"
                    top.withdraw()
            else:
                selection = "You have not selected anything"
                top.withdraw()
                tk.messagebox.showwarning("Warning","Set Not Selected")
            label.config(text = selection)
            #------------main initial framework-------------
        if messagebox.askyesno("", "Are you ready for TEST ?"):
            label1=tk.Label(msg_frame,text="Select the set from the following :")
            label1.pack()
            self.var = IntVar()
            radio1=tk.Radiobutton(msg_frame,text="Set-1",variable=self.var,value=1)
            radio1.pack()
            radio2=tk.Radiobutton(msg_frame,text="Set-2",variable=self.var,value=2)
            radio2.pack()
            radio3=tk.Radiobutton(msg_frame,text="Set-3",variable=self.var,value=3)
            radio3.pack()
            send_set_btn=tk.Button(msg_frame,text="Set_Paper",command=setpaper)    
            send_set_btn.pack()

        # client connect to host button
        connect_btn = tk.Button(ip_port_frame)
        connect_btn["text"] = "Connect"
        connect_btn["command"] = self.connect_to_host
        self.connect_btn = connect_btn

        master = self.master
        master.update()
        # Looks like master.winfo_height() doesn't include menubar height
        temporary_menubar_height = 30
        min_height = master.winfo_height() + temporary_menubar_height
        master.minsize(master.winfo_width(), min_height)

    

    def remove_host_instr(self, event=None):
        if self.host_instr_label is not None:
            self.host_instr_label.pack_forget()
            self.host_instr_label = None

    def prompt_new_name(self):
        self.new_name = simpledialog.askstring("Name Change", "New name")
        if self.new_name is not None:
            self.request_name_change(self.new_name)
    
    def promptname(self):
        return(self.new_name)

    def request_name_change(self, new_name):
        if self.chat is not None:
            self.chat.send_msg("/nc " + new_name)
        else:
            self.show_sys_msg("Can't change name until connected to a host")

    def display_new_msg(self):
        if self.chat is not None:
            msgs = self.chat.get_new_msgs()
            for msg in msgs:
                self.display_msg(msg)
        self.master.after(100, self.display_new_msg)

    def display_msg(self, msg):
        self.msg_window.config(state=tk.NORMAL)
        self.msg_window.insert(tk.END, "%s\n" % msg)
        self.msg_window.yview(tk.END)
        self.msg_window.config(state=tk.DISABLED)
        
    def send_msg(self, event=None):
        if self.chat is not None:
            #
            msg = self.msg_entry.get()#
            self.msg_entry.delete(0, tk.END)
            self.chat.send_msg(msg)
###
    def send_msg1(self,msg):
        if self.chat is not None:
            self.msg_entry.delete(0, tk.END)
            self.chat.send_msg(msg)
            
    def validate_entry_len(self, P, W):
        entry = self.master.nametowidget(W)
        if len(P) <= entry['width']:
            return True

        self.bell()
        return False
    
    def show_sys_msg(self, msg):
        if not msg:
            return

        msg = "SYSTEM: " + msg + "."
        self.display_msg(msg)

    def close_app(self):
        if self.chat is not None:
            self.chat.destroy()
        root.destroy()
    """    
    def setpaper(self):
        
        top=tk.Toplevel(root)
        top.minsize(500,500)
        #overall frame
        f1=tk.Frame(top)
        f1.pack()
        label=tk.Label(f1)
        label.pack()
        if(self.var.get()!=0):
            selection = "You selected the option " + str(self.var.get())
            self.setsel(f1,self.var.get())    
        else:
            selection = "You have not selected anything"
            top.withdraw()
            tk.messagebox.showwarning("Warning","Set Not Selected")
        label.config(text = selection)
        """
    

    #---------setsel()----function--------------------
    def setsel(self,f1,n):    
        self.c=0
        self.flag=0
        #--------set_1-----------------
        def set_1():
            self.score=0
            def q1(): 
                q['text']="Question1 : \n#include<iostream.h>\n#include<ctype.h>\ntypedef char Str80[80];\nvoid main()\n{\n  char *notes;\n  Str80 Str = 'vR2GooD';\n   int L=6;\n  Notes = Str;\n  while(L>=3)\n{\nStr[L] = isupper(Str[L]) ? tolower(Str[L]): toupper(Str[L]) ;\n cout<< Notes;\n  L--;\n  Notes++;\n }\n} "
                a1['text']='a'
                a1.pack()
                a2['text']='b'
                a2.pack()
                a3['text']='c'
                a3.pack()
                a4['text']='d'
                a4.pack()
                a()
            
                    
            def q2(): 
                q['text']="Question 2 : \n#include<iostream.h>\n#include<stdlib.h>\nvoid main()\n{\nrandomize();\nint Game[]={10,16},P;\nint Turn=random(2)+5;\nfor(int i=0;i<2;i++){\n p=random(2);\n cout<<Game[P]+Turn<<'#';}\n}"

                a5['text']='15#22#'
                a5.pack()
                a6['text']='22#16#'
                a6.pack()
                a7['text']='16#21#'
                a7.pack()
                a8['text']='21#22#'
                a8.pack()
                
                a()
            def q3():
                q['text']="Question 3 : \n#include<iostream.h>\n#include<stdlib.h>\nvoid main()\n{\nlong Number=7583241;\nint first=0,second=0;\ndo\n{\nit r=Number%10;\nif(r%2==0){\n  first+=r;\n}\nelse\n    second+=r;\nNumber/=10;\n}while(Number>0);\n\ncout<<first-second;\n}"
                a9['text']='-1'
                a9.pack()
                a10['text']='2'
                a10.pack()
                a11['text']='-2'
                a11.pack()
                a12['text']='1'
                a12.pack()
                a()
               
            def a():
                if self.c==0 :
                    self.flag=0
                    prev1['state']=DISABLED
                    next1['state']=NORMAL
                    next1['command']=q2
                    self.c+=1
                    
                elif(self.c==1 and self.flag==0):
                    next1['state']=NORMAL
                    prev1['state']=NORMAL
                    next1['command']=q3
                    self.c+=1
                    self.flag=1
                elif (self.c==2) :
                    self.flag=1
                    next1['state']=NORMAL
                    prev1['state']=NORMAL
                    prev1['command']=q2
                    next1['state']=DISABLED
                    self.c-=1
                elif(self.c==1 and self.flag==1):
                    prev1['state']=NORMAL
                    next1['state']=NORMAL
                    prev1['command']=q1
                    self.c-=1
                    self.flag=0
            self.score=0
            l=[]
            l2=[]
            qf=tk.LabelFrame(f2)
            qf.pack()
            q=tk.Label(f2,text="Question1 : <html>\n</html> ",bd=2,justify=LEFT)
            q.pack()
            self.flag2=0
            def sel():
                selection = self.var1.get()
                if (selection==2 and self.flag2==0):
                    self.score+=15
                    self.flag2=1
                elif(selection is not 2 and self.flag2==1):
                    self.score-=15
                    self.flag2=0
                elif (selection==2 and self.flag2==1):
                    self.score+=0
                    self.flag2=1
                else:
                    self.score+=0
                l.append(self.score)
            def sel1():
                selection = self.var2.get()
                if (selection==2 and self.flag2==0):
                    self.score+=15
                    self.flag2=1
                elif(selection is not 2 and self.flag2==1):
                    self.score-=15
                    self.flag2=0
                elif (selection==2 and self.flag2==1):
                    self.score+=0
                    self.flag2=1
                else:
                    self.score+=0
                l.append(self.score)
            def sel2():
                selection = self.var3.get()
                if (selection==2 and self.flag2==0):
                    self.score+=15
                    self.flag2=1
                elif(selection is not 2 and self.flag2==1):
                    self.score-=15
                    self.flag2=0
                elif (selection==2 and self.flag2==1):
                    self.score+=0
                    self.flag2=1
                else:
                    self.score+=0
                l.append(self.score)
            def scr():
                self.display_msg(l[len(l)-1])
                if(len(l)>=1):
                    l2.append(l[len(l)-1])
                    self.display_msg(l2)
                else:
                    pass
                
            self.var1= IntVar()
            self.var2= IntVar()
            self.var3= IntVar()
            
            a1=tk.Radiobutton(f2,value=1,variable=self.var1,text="",command=sel)
            a2=tk.Radiobutton(f2,value=2,variable=self.var1,text="",command=sel)
            a3=tk.Radiobutton(f2,value=3,variable=self.var1,text="",command=sel)
            a4=tk.Radiobutton(f2,value=4,variable=self.var1,text="",command=sel)
            a5=tk.Radiobutton(f2,value=1,variable=self.var2,text="",command=sel1)
            a6=tk.Radiobutton(f2,value=2,variable=self.var2,text="",command=sel1)
            a7=tk.Radiobutton(f2,value=3,variable=self.var2,text="",command=sel1)
            a8=tk.Radiobutton(f2,value=4,variable=self.var2,text="",command=sel1)
            a9=tk.Radiobutton(f2,value=1,variable=self.var3,text="",command=sel2)
            a10=tk.Radiobutton(f2,value=2,variable=self.var3,text="",command=sel2)
            a11=tk.Radiobutton(f2,value=3,variable=self.var3,text="",command=sel2)
            a12=tk.Radiobutton(f2,value=4,variable=self.var3,text="",command=sel2)
            sub1=tk.Button(f2,text="SUBMIT",command=scr)  
            sub1.pack(side=BOTTOM)
            
            next1=tk.Button(f2,text="NEXT")  
            next1.pack(side=BOTTOM)
            prev1=tk.Button(f2,text="PREVIOUS")
            prev1.pack(side=LEFT)
            
            q1()
        #--------set_2-----------------
        def set_2():
            
            def q2(): 
                q['text']="Question2 : \n#include<iostream.h>\n#include<ctype.h>\ntypedef char Str80[80];\nvoid main()\n{\n  char *notes;\n  Str80 Str = 'vR2GooD';\n   int L=6;\n  Notes = Str;\n  while(L>=3)\n{\nStr[L] = isupper(Str[L]) ? tolower(Str[L]): toupper(Str[L]) ;\n cout<< Notes;\n  L--;\n  Notes++;\n }\n} "
                a1['text']='a'
                a2['text']='b'
                a3['text']='c'
                a4['text']='d'
                a()
                
                
            def q3(): 
                q['text']="Question 3 : \n#include<iostream.h>\n#include<stdlib.h>\nvoid main()\n{\nrandomize();\nint Game[]={10,16},P;\nint Turn=random(2)+5;\nfor(int i=0;i<2;i++){\n p=random(2);\n cout<<Game[P]+Turn<<'#';}\n}"
                a1['text']='15#22#'
                a2['text']='22#16#'
                a3['text']='16#21#'
                a4['text']='21#22#'
                a()
                
            def q1():
                q['text']="Question 1 : \n#include<iostream.h>\n#include<stdlib.h>\nvoid main()\n{\nlong Number=7583241;\nint first=0,second=0;\ndo\n{\nit r=Number%10;\nif(r%2==0){\n  first+=r;\n}\nelse\n    second+=r;\nNumber/=10;\n}while(Number>0);\n\ncout<<first-second;\n}"
                a1['text']='-1'
                a2['text']='2'
                a3['text']='-2'
                a4['text']='1'
                a()
               
            def a():
                if self.c==0 :
                    self.flag=0
                    prev1['state']=DISABLED
                    next1['state']=NORMAL
                    next1['command']=q2
                    self.c+=1
                    
                elif(self.c==1 and self.flag==0):
                    next1['state']=NORMAL
                    prev1['state']=NORMAL
                    next1['command']=q3
                    self.c+=1
                    self.flag=1
                elif (self.c==2) :
                    self.flag=1
                    next1['state']=NORMAL
                    prev1['state']=NORMAL
                    prev1['command']=q2
                    next1['state']=DISABLED
                    self.c-=1
                elif(self.c==1 and self.flag==1):
                    prev1['state']=NORMAL
                    next1['state']=NORMAL
                    prev1['command']=q1
                    self.c-=1
                    self.flag=0
               
            qf=tk.Frame(f2)
            qf.pack()
            q=tk.Label(f2,text="Question1 : <html>\n</html> ",bd=2,justify=LEFT)
            q.pack()
            self.var1= IntVar()
            a1=tk.Radiobutton(f2,value=1,variable=self.var1,text="a")
            a1.pack()
            a2=tk.Radiobutton(f2,value=2,variable=self.var1,text="b")
            a2.pack()
            a3=tk.Radiobutton(f2,value=3,variable=self.var1,text="c")
            a3.pack()
            a4=tk.Radiobutton(f2,value=4,variable=self.var1,text="d")
            a4.pack()
            
            next1=tk.Button(f2,text="NEXT")  
            next1.pack(side=BOTTOM)
            prev1=tk.Button(f2,text="PREVIOUS")
            prev1.pack(side=LEFT)
            
            q1()
        #--------set_3-----------------
        def set_3():
            
            def q3(): 
                q['text']="Question3 : \n#include<iostream.h>\n#include<ctype.h>\ntypedef char Str80[80];\nvoid main()\n{\n  char *notes;\n  Str80 Str = 'vR2GooD';\n   int L=6;\n  Notes = Str;\n  while(L>=3)\n{\nStr[L] = isupper(Str[L]) ? tolower(Str[L]): toupper(Str[L]) ;\n cout<< Notes;\n  L--;\n  Notes++;\n }\n} "
                
                a()
            def q1(): 
                q['text']="Question 1 : \n#include<iostream.h>\n#include<stdlib.h>\nvoid main()\n{\nrandomize();\nint Game[]={10,16},P;\nint Turn=random(2)+5;\nfor(int i=0;i<2;i++){\n p=random(2);\n cout<<Game[P]+Turn<<'#';}\n}"
                a1['text']='15#22#'
                a2['text']='22#16#'
                a3['text']='16#21#'
                a4['text']='21#22#'
                
                a()
            def q2():
                q['text']="Question 2 : \n#include<iostream.h>\n#include<stdlib.h>\nvoid main()\n{\nlong Number=7583241;\nint first=0,second=0;\ndo\n{\nit r=Number%10;\nif(r%2==0){\n  first+=r;\n}\nelse\n    second+=r;\nNumber/=10;\n}while(Number>0);\n\ncout<<first-second;\n}"
                a1['text']='-1'
                a2['text']='2'
                a3['text']='-2'
                a4['text']='1'
                a()
               
            def a():
                if self.c==0 :
                    self.flag=0
                    prev1['state']=DISABLED
                    next1['state']=NORMAL
                    next1['command']=q2
                    self.c+=1
                    
                elif(self.c==1 and self.flag==0):
                    next1['state']=NORMAL
                    prev1['state']=NORMAL
                    next1['command']=q3
                    self.c+=1
                    self.flag=1
                elif (self.c==2) :
                    self.flag=1
                    next1['state']=NORMAL
                    prev1['state']=NORMAL
                    prev1['command']=q2
                    next1['state']=DISABLED
                    self.c-=1
                elif(self.c==1 and self.flag==1):
                    prev1['state']=NORMAL
                    next1['state']=NORMAL
                    prev1['command']=q1
                    self.c-=1
                    self.flag=0
               
            qf=tk.Frame(f2)
            qf.pack()
            q=tk.Label(f2,text="Question1 : <html>\n</html> ",bd=2,justify=LEFT)
            q.pack()
            self.var1= IntVar()
            a1=tk.Radiobutton(f2,value=1,variable=self.var1,text="a")
            a1.pack()
            a2=tk.Radiobutton(f2,value=2,variable=self.var1,text="b")
            a2.pack()
            a3=tk.Radiobutton(f2,value=3,variable=self.var1,text="c")
            a3.pack()
            a4=tk.Radiobutton(f2,value=4,variable=self.var1,text="d")
            a4.pack()
            
            next1=tk.Button(f2,text="NEXT")  
            next1.pack(side=BOTTOM)
            prev1=tk.Button(f2,text="PREVIOUS")
            prev1.pack(side=LEFT)
            
            q1()
            
        #-------------selection of a set-------------------
        if(n==1):
            f2=tk.Frame(f1)
            f2.pack()
            st=tk.Label(f2,text="SET1")
            st.pack()
            set_1()
        elif(n==2):
            f2=tk.Frame(f1)
            f2.pack()
            st=tk.Label(f2,text="SET2")
            st.pack()
            set_2()
        elif(n==3):
            f2=tk.Frame(f1)
            f2.pack()
            st=tk.Label(f2,text="SET3")
            st.pack()
            set_3()

            
            
        
        
        
        
        
root = tk.Tk()
p2p_chat = P2pChat(master=root)
p2p_chat.mainloop()

