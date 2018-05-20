from tkinter import filedialog
from tkinter.messagebox import showerror

hexfile = None

def button1Click(this):
	global hexfile
	hexfile = askopenfilename(filetypes=(("Hex Dosyası", "*.hex"),("All files", "*.*") ))
	
	if hexfile:
		print(hexfile)
	
def button2Click(this):
	if hexfile:
		import platform,subprocess
		platform = platform.system()
		#print(platform)
		deleteTextBoxText("textBox1")
		if platform == "Windows":
			try:
				com = 'assets\\mikroe-uhb.exe -v "{}"'.format(hexfile)
				import subprocess
				p = subprocess.Popen(com,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,stdin=subprocess.PIPE,shell=True)
				for line in iter(p.stdout.readline, b''):
					appendTextBoxText("textBox1",'\n{}\n'.format(line.rstrip()))
			except:
				showerror("Unexpected error", sys.exc_info())
				raise
		elif platform == "Linux":
			print("asd")
		elif platform == "Mac":
			print("asd")
		else:
			showerror("HATA","Bilinmeyen Platform")
	else:
		showerror("HATA","Lütfen önce bir Hex dosyası seçiniz")
	
def button3Click(this):
	import webbrowser
	webbrowser.open('http://www.pickat.org/', new=2)
