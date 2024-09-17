from tinydb import TinyDB, Query
import customtkinter as ctki
from PIL import Image


db = TinyDB('contas.json')
dba = TinyDB('animais.json')
dbq = Query()
e = ''
boxchecka = 0
boxcheckp = 0
boxchecki = 0
global p1, p2, p3, p4, lv
p1 = 'Espécie'
p2 = 'Porte'
p3 = 'Idade'
p4 = 'Cor'
lv = [p1, p2, p3, p4]

#Main 
ctki.set_appearance_mode('light')
ctki.set_default_color_theme('green')
janlog = ctki.CTk()
janlog.title('Login')
janlog.geometry('1000x600')

        
#erro no email (Login)
def emlgerro():
    lgerro = ctki.CTkToplevel(janlog)
    lgerro.title('Erro no Email')
    janlog.withdraw()
        
    lgerro.title = ('Erro no login')
    lgerro.geometry('500x300')
        
    def closeerro():
        lgerro.destroy()
        lgerro.update()
        janlog.deiconify()


    emlgerr = ctki.CTkLabel(lgerro, text='email inválido', font=ctki.CTkFont(size=20))
    emlgerr.pack(pady = 20)
    errok = ctki.CTkButton(lgerro, text='OK', command=closeerro)
    errok.pack(pady = 30)


#erro na senha (Login)
def snlgerro():
    lgerro = ctki.CTkToplevel(janlog)
    lgerro.title('Erro na Senha')
    lgerro.geometry('500x300')
    janlog.withdraw()
        
    snlgerr = ctki.CTkLabel(lgerro, text='senha incorreta', font=ctki.CTkFont(size=20))
    snlgerr.pack(pady = 20)
        
    def closeerro():
        lgerro.destroy()
        lgerro.update()
        janlog.deiconify()


    errok = ctki.CTkButton(lgerro, text='OK', command=closeerro)
    errok.pack(pady = 30)


#Pagina de cadastro
def new():
    jancad = ctki.CTkToplevel(janlog)
    jancad.title('Cadastro')
    jancad.geometry('1000x600')
    janlog.withdraw()

    def cademerro():
        caderro = ctki.CTkToplevel(janlog)
        caderro.geometry('500x300')
        caderro.title('Erro no Cadastro')
        jancad.withdraw()

        def closecaderro():
            caderro.destroy()
            caderro.update()
            jancad.deiconify()
              
        cademerr = ctki.CTkLabel(caderro, text=e, font=ctki.CTkFont(size=20))
        cademerr.pack(pady = 20)
        caderrok = ctki.CTkButton(caderro, text='OK', command=closecaderro)
        caderrok.pack(pady = 30)

#Criação de conta
    def create():
        em = cademail.get()
        nom = cadnom.get()
        sen = cadsenha.get()
        per = segpe.get()
        rep = segre.get()
        global e
        if per == '':
            per = 'Sem Pergunta'
        if em == '' or em.count('@') != 1:
            e = 'E-mail Inválido'
            cademerro()
        elif db.search(dbq.Email == em) != []:
            e = 'E-mail Já Existente'
            cademerro()
        elif nom == '':
            e = 'O Nome Precisa Ser Preenchido'
            cademerro()
        elif len(sen) < 6:
            e = 'A Senha Precisa De Pelo Menos 6 Algarismos'
            cademerro()
        else:
            db.insert({'Email': em, 'Nome': nom, 'Senha': sen, 'Pergunta':per, 'Resposta':rep})
            jancad.destroy()
            jancad.update()
            sucesso = ctki.CTkToplevel(janlog)
            sucesso.title('cadastro bem sucedido')
            sucesso.geometry('500x300')
            sucess = ctki.CTkLabel(sucesso, text='Seu cadastro foi bem sucedido', font= ctki.CTkFont(size=30))

            def closesuc():
                sucesso.destroy()
                sucesso.update()
                janlog.deiconify()

            sucbutton = ctki.CTkButton(sucesso, text='OK', command=closesuc)
            sucess.pack(pady = 20)
            sucbutton.pack(pady=20)
    
    def close():
        jancad.destroy()
        jancad.update()
        janlog.deiconify()


#Cadastro
    maincad = ctki.CTkLabel(jancad, text='Cadastre-se', font= ctki.CTkFont(family='Open_Sans', size=40))
    emai = ctki.CTkLabel(jancad, text='E-mail *', font=ctki.CTkFont(size=18))
    cademail = ctki.CTkEntry(jancad,width=250)
    nomi = ctki.CTkLabel(jancad, text='Nome *', font=ctki.CTkFont(size=18))
    cadnom = ctki.CTkEntry(jancad,width=250)
    seni = ctki.CTkLabel(jancad, text='Senha *', font=ctki.CTkFont(size=18))
    cadsenha = ctki.CTkEntry(jancad,width=250, placeholder_text='Pelo menos 6 dígitos')
    segper = ctki.CTkLabel(jancad, text='Pergunta de segurança', font=ctki.CTkFont(size=18))
    segpe = ctki.CTkEntry(jancad, width=250, placeholder_text='Opicional')
    segrel = ctki.CTkLabel(jancad, text='Resposta da pergunta', font=ctki.CTkFont(size=18))
    segre = ctki.CTkEntry(jancad, width=250, placeholder_text='Opicional')
    maincadbutton = ctki.CTkButton(jancad, text='Cadastrar-se', command=create)
    logbutton = ctki.CTkButton(jancad, text='Logar', text_color='blue', fg_color='transparent',hover=False, command=close)


    maincad.pack(pady = 50)
    emai.pack(pady = 0)
    cademail.pack(pady = 10)
    nomi.pack(pady = 0)
    cadnom.pack(pady = 10)
    seni.pack(pady = 0)
    cadsenha.pack(pady = 10)
    segper.pack(pady = 0)
    segpe.pack(pady = 10)
    segrel.pack(pady = 0)
    segre.pack(pady = 10)
    maincadbutton.pack(pady = 5)
    logbutton.pack(pady = 0)


def check():
        global em
        em = logemail.get()
        sen = logsenha.get()
        if db.search(dbq.Email == em) == []:
            et = 1
            emlgerro()
        elif db.search(dbq.Email == em)[0]['Senha'] != sen:
            et = 2
            snlgerro()
            
        else:
            abrigo = 0
            mainpage()


def chiki():
    logsenha.configure(show = cheki.get())

#Recuperação de Senha

def esq():
    tm = logemail.get()
    janlog.withdraw()
    if db.search(dbq.Email == tm) == []:
        erq = ctki.CTkToplevel(janlog)
        erq.geometry('500x300')
        erq.title('ERRO')
        erql = ctki.CTkLabel(erq, text='Preencha um Email válido para recuperar a senha', font=ctki.CTkFont(size=20))
        def volq():
            erq.destroy()
            erq.update()
            janlog.deiconify()
        erqvol = ctki.CTkButton(erq, text='OK', command=volq)
        erql.pack(pady = 40)
        erqvol.pack(pady = 20)
    else:
        if db.search(dbq.Email == tm)[0]['Pergunta'] == 'Sem Pergunta':
            janlog.withdraw()
            erq2 = ctki.CTkToplevel(janlog)
            erq2.geometry('500x300')
            erq2.title('ERRO')
            erql2 = ctki.CTkLabel(erq2, text='Essa conta não possui pergunta de segurança', font=ctki.CTkFont(size=20))
            erql22 = ctki.CTkLabel(erq2, text='para recuperar a conta entre em contato com o suporte:', font=ctki.CTkFont(size=20))
            erql222 = ctki.CTkLabel(erq2, text= '(81) 982726973', font=ctki.CTkFont(size=20))
            def erq2vol():
                erq2.destroy()
                erq2.update()
                janlog.deiconify()
            erqb2 = ctki.CTkButton(erq2, text='OK', command=erq2vol)
            erql2.pack(pady = 10)
            erql22.pack(pady = 0)
            erql222.pack(pady = 10)
            erqb2.pack(pady = 40)
        else:
            janlog.withdraw()
            recsen = ctki.CTkToplevel(janlog)
            recsen.geometry('500x300')
            recsen.title('Recuperar Senha')
            recsnl = ctki.CTkLabel(recsen, text='Responda a pergunta de segurança', font=ctki.CTkFont(size=20))
            recper = ctki.CTkLabel(recsen, text=db.search(dbq.Email == tm)[0]['Pergunta'], font=ctki.CTkFont(size=20))
            recre = ctki.CTkEntry(recsen, width=250)
            def recp():
                if recre.get() == db.search(dbq.Email == tm)[0]['Resposta']:
                    recsen.destroy()
                    recsen.update()
                    senrec = ctki.CTkToplevel(janlog)
                    senrec.geometry('500x300')
                    senrec.title('Senha Recuperada')
                    senr = ctki.CTkLabel(senrec, text='Sua senha é: ' + db.search(dbq.Email == tm)[0]['Senha'], font=ctki.CTkFont(size=20))
                    def volsen():
                        senrec.destroy()
                        senrec.update()
                        janlog.deiconify()
                    senrvol = ctki.CTkButton(senrec, text='OK', command=volsen)
                    senr.pack(pady = 30)
                    senrvol.pack(pady = 20)  
                else:
                    recsen.destroy()
                    recsen.update()
                    reer = ctki.CTkToplevel(janlog)
                    reer.geometry('500x300')
                    reer.title('ERRO')
                    reel = ctki.CTkLabel(reer, text='Resposta incorreta', font=ctki.CTkFont(size=20))
                    def reerv():
                        reer.destroy()
                        reer.update()
                        janlog.deiconify()
                    reevol = ctki.CTkButton(reer, text='OK', command=reerv)
                    reel.pack(pady = 20)
                    reevol.pack(pady = 10)
            recon = ctki.CTkButton(recsen, text='OK', command=recp)
            def recvol():
                recsen.destroy()
                recsen.update()
                janlog.deiconify()
            revol = ctki.CTkButton(recsen, text='voltar', text_color='blue', hover=False, fg_color='transparent', command=recvol)
            recsnl.pack(pady = 20)
            recper.pack(pady = 20)
            recre.pack(pady = 0)
            recon.pack(pady = 20)
            revol.pack(pady = 0)

#Login

titulo = ctki.CTkLabel(janlog, text = 'MatchPet', font= ctki.CTkFont(family='Open_Sans', size=70), text_color='#069E6E')
logla = ctki.CTkLabel(janlog, text='Login', font= ctki.CTkFont(size = 40))
logemi = ctki.CTkLabel(janlog, text='E-mail', font=ctki.CTkFont(size=18))
logemail = ctki.CTkEntry(janlog,width=250, font=ctki.CTkFont(size=20))
logseni = ctki.CTkLabel(janlog, text='Senha', font=ctki.CTkFont(size=18))
cheki = ctki.CTkCheckBox(janlog, text='mostrar senha', onvalue='', offvalue='*', command=chiki)
logsenha = ctki.CTkEntry(janlog,width=250, show= cheki.get(), font=ctki.CTkFont(size=20))
essen = ctki.CTkButton(janlog, text='esqueceu sua senha', text_color='blue', hover=False, fg_color='transparent', command=esq)
mainlogbutton = ctki.CTkButton(janlog, text='Login', command=check)
cadbutton = ctki.CTkButton(janlog, text='cadastro', command=new)

titulo.pack(pady = 20)
logla.pack(pady = 30)
logemi.pack(pady = 0)
logemail.pack(pady = 10)
logseni.pack(pady = 0)
logsenha.pack(pady = 10)
cheki.pack(pady = 0)
essen.pack(pady = 10)
mainlogbutton.pack(pady = 20)
cadbutton.pack(pady = 0)


#Pagina principal
def mainpage():
    
    mp = ctki.CTkToplevel(janlog)
    mp.title('Página Principal')
    mp.geometry('1000x600')
    janlog.withdraw()
    

    def voltar():
        janlog.deiconify()
        mp.destroy()
        mp.update()
        logemail.delete(0, len(logemail.get()))
        logsenha.delete(0, len(logsenha.get()))

#Filtro de adoção  
    def adotar():
        ad = ctki.CTkToplevel(janlog)
        ad.title('Adotar')
        ad.geometry('1000x600')
        ad.columnconfigure(0, weight=2)
        ad.columnconfigure(1, weight=1)
        ad.columnconfigure(2, weight=1)
        ad.columnconfigure(3, weight=1)
        ad.columnconfigure(4, weight=1)
        ad.rowconfigure(0, weight=1)
        ad.rowconfigure(1, weight=1)
        ad.rowconfigure(2, weight=1)
        ad.rowconfigure(3, weight=1)
        ad.rowconfigure(4, weight=1)
        ad.rowconfigure(5, weight=1)
        ad.rowconfigure(6, weight=1)
        ad.rowconfigure(7, weight=1)
        mp.destroy()
        mp.update()
        def pch():
            ad.withdraw()
            prch = ctki.CTkToplevel(janlog)
            prch.geometry('1000x600')
            prch.title('Alterar Prioridades')
            prchl = ctki.CTkLabel(prch, text='Prioridade atual:', font=ctki.CTkFont(size=20))
            p1l = ctki.CTkLabel(prch, text= '1-' + p1, font=ctki.CTkFont(size=20))
            p2l = ctki.CTkLabel(prch, text= '2-' + p2, font=ctki.CTkFont(size=20))
            p3l = ctki.CTkLabel(prch, text= '3-' + p3, font=ctki.CTkFont(size=20))
            p4l = ctki.CTkLabel(prch, text= '4-' + p4, font=ctki.CTkFont(size=20))
            def ap():
                prch.destroy()
                apc = ctki.CTkToplevel(janlog)
                apc.geometry('1000x600')
                apc.title('Alterar Prioridades')
                apc.columnconfigure(0, weight=1)
                apc.columnconfigure(1, weight=1)
                apc.rowconfigure(0, weight=1)
                apc.rowconfigure(1, weight=1)
                apc.rowconfigure(2, weight=1)
                apc.rowconfigure(3, weight=1)
                apc.rowconfigure(4, weight=1)
                apc.rowconfigure(5, weight=1)
                apct = ctki.CTkLabel(apc, text='Defina as Prioridades', font=ctki.CTkFont(size=40))
                t1 = ctki.CTkLabel(apc, text='Prioridade 1-', font=ctki.CTkFont(size = 20))
                apc1 = ctki.CTkComboBox(apc, values=lv, button_color='#069E6E', font=ctki.CTkFont(size = 20))
                t2 = ctki.CTkLabel(apc, text='Prioridade 2-', font=ctki.CTkFont(size = 20))
                apc2 = ctki.CTkComboBox(apc, values=lv, button_color='#069E6E', font=ctki.CTkFont(size = 20))
                apc2.set(lv[1])
                t3 = ctki.CTkLabel(apc, text='Prioridade 3-', font=ctki.CTkFont(size = 20))
                apc3 = ctki.CTkComboBox(apc, values=lv, button_color='#069E6E', font=ctki.CTkFont(size = 20))
                apc3.set(lv[2])
                t4 = ctki.CTkLabel(apc, text='Prioridade 4-', font=ctki.CTkFont(size = 20))
                apc4 = ctki.CTkComboBox(apc, values=lv, button_color='#069E6E', font=ctki.CTkFont(size = 20))
                apc4.set(lv[3])
                def av():
                    apc.destroy()
                    ad.deiconify()
                apcv = ctki.CTkButton(apc, text='cancelar', command=av)
                def pc():
                    global p1, p2, p3, p4, lv
                    p1t = apc1.get()
                    p2t = apc2.get()
                    p3t = apc3.get()
                    p4t = apc4.get()
                    if p1t == p2t or p1t == p3t or p1t == p4t or p2t == p3t or p2t == p4t or p3t == p4t:
                        apc.withdraw()
                        aper = ctki.CTkToplevel(janlog)
                        aper.geometry('500x300')
                        aper.title('ERRO')
                        apel = ctki.CTkLabel(aper, text='Escolha opções diferentes para cada prioridade', font=ctki.CTkFont(size = 20))
                        def aperok():
                            aper.destroy()
                            apc.deiconify()
                        apeok = ctki.CTkButton(aper, text='OK', command=aperok)
                        apel.pack(pady = 50)
                        apeok.pack(pady = 10)
                    else:
                        p1 = p1t
                        p2 = p2t                          p3 = p3t
                        p4 = p4t
                        lv = [p1, p2, p3, p4]
                        apc.destroy()
                        ad.deiconify()
                apok = ctki.CTkButton(apc, text='confirmar', command=pc)
                apct.grid(row = 0, column = 0, columnspan = 2)
                t1.grid(row = 1, column = 0, sticky = 'e', padx = 10)
                apc1.grid(row = 1, column = 1, sticky = 'w')
                t2.grid(column = 0, row = 2, sticky = 'e', padx = 10)
                apc2.grid(column = 1, row = 2, sticky = 'w')
                t3.grid(column = 0, row = 3, sticky = 'e', padx = 10)
                apc3.grid(column = 1, row = 3, sticky = 'w')
                t4.grid(column = 0, row = 4, sticky = 'e', padx = 10)
                apc4.grid(column = 1, row = 4, sticky = 'w')
                apcv.grid(column = 0, row = 5, sticky = 'e', padx = 10)
                apok.grid(column = 1, row = 5, sticky = 'w', padx = 10)

            alp = ctki.CTkButton(prch, text='Alterar Prioridades', command=ap)
            def adv():
                prch.destroy()
                ad.deiconify()
            pv = ctki.CTkButton(prch, text='voltar', text_color='blue', hover=False, fg_color='transparent', command=adv)
            prchl.pack(pady = 40)
            p1l.pack(pady = 20)
            p2l.pack(pady = 10)
            p3l.pack(pady = 20)
            p4l.pack(pady = 10)
            alp.pack(pady = 30)
            pv.pack(pady = 0)
        adlab = ctki.CTkLabel(ad, text='Selecione características desejadas', font=ctki.CTkFont(size = 30))
        adpch = ctki.CTkButton(ad, text='Definir Prioridades', command=pch)
        catcheck = ctki.CTkCheckBox(ad, text='Gato', onvalue='cat', offvalue='')
        dogcheck = ctki.CTkCheckBox(ad, text='Cachorro', onvalue='dog', offvalue='')
        
        c1check = ctki.CTkCheckBox(ad, text='Branco', onvalue='1', offvalue='')
        c2check = ctki.CTkCheckBox(ad, text='Caramelo', onvalue='2', offvalue='')
        c3check = ctki.CTkCheckBox(ad, text='Laranja', onvalue='3', offvalue='')
        c4check = ctki.CTkCheckBox(ad, text='Marrom', onvalue='4', offvalue='')
        c5check = ctki.CTkCheckBox(ad, text='Cinza', onvalue='5', offvalue='')
        c6check = ctki.CTkCheckBox(ad, text='Preto', onvalue='6', offvalue='')
        
        cp1check = ctki.CTkCheckBox(ad, text='Pequeno Porte', onvalue='peq', offvalue='')
        cp2check = ctki.CTkCheckBox(ad, text='Médio Porte', onvalue='med', offvalue='')
        cp3check = ctki.CTkCheckBox(ad, text='Grande Porte', onvalue='big', offvalue='')
        ci1check = ctki.CTkCheckBox(ad, text='Filhote', onvalue='nov', offvalue='')
        ci2check = ctki.CTkCheckBox(ad, text='Adulto', onvalue='adt', offvalue='')
        ci3check = ctki.CTkCheckBox(ad, text='Idoso', onvalue='old', offvalue='')

#Cálculo de valor adoção
        def prox():
            global lv
            cat = catcheck.get()
            dog = dogcheck.get()
            c1 = c1check.get()
            c2 = c2check.get()
            c3 = c3check.get()
            c4 = c4check.get()
            c5 = c5check.get()
            c6 = c6check.get()
            cp1 = cp1check.get()
            cp2 = cp2check.get()
            cp3 = cp3check.get()
            ci1 = ci1check.get()
            ci2 = ci2check.get()
            ci3 = ci3check.get()
            l = []
            lf = []
            vt = 0
            vp = 0
            vi = 0
            vc = 0
            x = 100000
            for i in lv:
                x /= 10
                if i == 'Cor':
                    vc = x
                elif i == 'Porte':
                    vp = x
                elif i == 'Idade':
                    vi = x
                else:
                    vt = x
            for i in dba:
                v = 0
                if i['Tipo'] == cat or i['Tipo'] == dog:
                    v += vt
                if i['Porte'] == cp1 or i['Porte'] == cp2 or i['Porte'] == cp3:
                    v += vp
                if i['Idade'] == ci1 or i['Idade'] == ci2 or i['Idade'] == ci3:
                    v += vi
                if i['Cor'].count(c1) == 1 or i['Cor'].count(c2) == 1 or i['Cor'].count(c3) == 1 or i['Cor'].count(c4) == 1 or i['Cor'].count(c5) == 1 or i['Cor'].count(c6) == 1:
                    v += vc                
                l.append(v)
                l2 = sorted(l, reverse=True)              
                lf.insert(l2.index(v), i['Foto'])
                
#Escolha de pet adoção
            fado = ctki.CTkToplevel(janlog)
            ad.destroy()
            ad.update()
            fado.geometry('1000x600')
            fado.title('Escolha seu pet')
            tefado = ctki.CTkLabel(fado, text='Escolha um Pet', font= ctki.CTkFont(size=35))
            tfado = ctki.CTkScrollableFrame(fado, width=900, height=400)
            tefado.pack(pady = 20)
            tfado.pack(pady = 0)
            
            def voltfado():
                fado.destroy()
                fado.update()
                adotar()
#Perfil do pet
            def perf():
                fado.destroy()
                fado.update()
                perch = ctki.CTkToplevel(janlog)
                perch.geometry('500x300')
                perch.title('Escolha um Pet')
                perchtxt = ctki.CTkLabel(perch, text='Número do pet de interesse', font=ctki.CTkFont(size=20))
                perchent = ctki.CTkEntry(perch)
                def okperch():
                    pet = int(perchent.get()) - 1
                    try:
                        lf[pet]
                    except:
                        perch.destroy()
                        perch.update()
                        pererro = ctki.CTkToplevel(janlog)
                        pererro.geometry('500x300')
                        pererro.title('Erro')
                        ptxt = ctki.CTkLabel(pererro, text='número inválido', font=ctki.CTkFont(size=20))
                        def ptko():
                            pererro.destroy()
                            pererro.update()
                            perf()
                        ptok = ctki.CTkButton(pererro, text='OK',command=ptko)
                        ptxt.pack(pady = 20)
                        ptok.pack(pady = 20)
                    else:
                        perch.destroy()
                        perch.update()
                        anperf = ctki.CTkToplevel(janlog)
                        anperf.geometry('1000x600')
                        anperf.title('Perfil do Pet')
                        ftperfil = ctki.CTkImage(light_image=Image.open('Pets/' + lf[pet]), dark_image=Image.open('Pets/' + lf[pet]), size=[300, 300])
                        ft = ctki.CTkLabel(anperf, image=ftperfil, text='')
                        nomperf = ctki.CTkLabel(anperf, text='Dono: ' + dba.search(dbq.Foto == lf[pet])[0]['Dono'], font=ctki.CTkFont(size=20))
                        locperf = ctki.CTkLabel(anperf, text='Localização: ' + dba.search(dbq.Foto == lf[pet])[0]['Endereço'], font=ctki.CTkFont(size=20))
                        def fina():
                            anperf.destroy()
                            anperf.update()
                            fim = ctki.CTkToplevel(janlog)
                            fim.geometry('500x300')
                            fim.title('Obrigado pela adoção')
                            fimem = ctki.CTkLabel(fim, text='E-mail para contato: ' + dba.search(dbq.Foto == lf[pet])[0]['Conta'], font=ctki.CTkFont(size=20))
                            fimnum = ctki.CTkLabel(fim, text='Telefone para contato: ' + dba.search(dbq.Foto == lf[pet])[0]['Celular'], font=ctki.CTkFont(size=20))
                            fimm = ctki.CTkLabel(fim, text='Obrigado pela preferência', font=ctki.CTkFont(size=20))
                            def fimfi():
                                fim.destroy()
                                fim.update()
                                mainpage()
                            fimfim = ctki.CTkButton(fim, text='OK', command=fimfi)
                            fimem.pack(pady = 10)
                            fimnum.pack(pady = 10)
                            fimm.pack(pady = 10)
                            fimfim.pack(pady  = 30)
                        adtper = ctki.CTkButton(anperf, text='Adotar', command=fina)
                        def volperf():
                            anperf.destroy()
                            anperf.update()
                            perf()
                        volpef = ctki.CTkButton(anperf, text='voltar', text_color='blue', hover=False, fg_color='transparent', command=volperf)
                        ft.pack(pady = 20)
                        nomperf.pack(pady = 10)
                        locperf.pack(pady = 10)
                        adtper.pack(pady = 10)
                        volpef.pack(pady = 0)

                perchok = ctki.CTkButton(perch, text='Ver informações', command=okperch)
                def volperc():
                    perch.destroy()
                    perch.update()
                    prox()
                perchvol = ctki.CTkButton(perch, text='voltar', text_color='blue', hover=False, fg_color='transparent', command=volperc)
                perchtxt.pack(pady = 10)
                perchent.pack(pady = 10)
                perchok.pack(pady = 20)
                perchvol.pack(pady = 0)
                
            
            z = 0
            for j in lf:
                z += 1
                img = 'Pets/' + j
                numim = ctki.CTkLabel(tfado, text=z, font=ctki.CTkFont(size=20))
                numim.pack(pady = 5)
                imfado = ctki.CTkImage(light_image=Image.open(img), dark_image=Image.open(img), size=[150, 150])
                imgfado = ctki.CTkLabel(tfado, image=imfado, text='')                
                imgfado.pack(pady = 10)
                    
            adtfado = ctki.CTkButton(fado, text='Escolher um pet', command=perf)
            adtfado.pack(pady = 5)
            volfado = ctki.CTkButton(fado, text='voltar', text_color='blue', hover=False, fg_color='transparent', command=voltfado)
            volfado.pack(pady = 5)
        
        nextbutton = ctki.CTkButton(ad, text='Proxima Etapa', command=prox)
        def volbul():
            ad.destroy()
            ad.update()
            mainpage()
        volbu = ctki.CTkButton(ad, text='voltar', text_color='blue', hover=False, fg_color='transparent', command=volbul)

        adlab.grid(row = 0, column = 2, ipady = 10, sticky = 'w')
        adpch.grid(row = 5, column = 2, sticky = 's')
        catcheck.grid(row = 1, column = 1, ipadx = 10, ipady = 10, sticky = 'we')
        dogcheck.grid(row = 1, column = 3, ipadx = 10, ipady = 10, sticky = 'we')
        
        c1check.grid(row = 2, column = 1, ipadx = 10, ipady = 10, sticky = 'we')
        c2check.grid(row = 3, column = 1, ipadx = 10, ipady = 10, sticky = 'we')
        c3check.grid(row = 4, column = 1, ipadx = 10, ipady = 10, sticky = 'we')
        c4check.grid(row = 5, column = 1, ipadx = 10, ipady = 10, sticky = 'we')
        c5check.grid(row = 6, column = 1, ipadx = 10, ipady = 10, sticky = 'we')
        c6check.grid(row = 7, column = 1, ipadx = 10, ipady = 10, sticky = 'we')

        cp1check.grid(row = 2, column = 3, ipadx = 10, ipady = 10, sticky = 'we')
        cp2check.grid(row = 3, column = 3, ipadx = 10, ipady = 10, sticky = 'we')
        cp3check.grid(row = 4, column = 3, ipadx = 10, ipady = 10, sticky = 'we')
        ci1check.grid(row = 5, column = 3, ipadx = 10, ipady = 10, sticky = 'we')
        ci2check.grid(row = 6, column = 3, ipadx = 10, ipady = 10, sticky = 'we')
        ci3check.grid(row = 7, column = 3, ipadx = 10, ipady = 10, sticky = 'we')

        nextbutton.grid(row = 6, column = 2)
        volbu.grid(row = 7, column = 2)
#Filtro Doação    
    def doar():
        do = ctki.CTkToplevel(janlog)
        do.title('Registro de Doações')
        do.geometry('1000x600')
        do.columnconfigure(0, weight=2)
        do.columnconfigure(1, weight=1)
        do.columnconfigure(2, weight=1)
        do.columnconfigure(3, weight=1)
        do.columnconfigure(4, weight=1)
        do.rowconfigure(0, weight=1)
        do.rowconfigure(1, weight=1)
        do.rowconfigure(2, weight=1)
        do.rowconfigure(3, weight=1)
        do.rowconfigure(4, weight=1)
        do.rowconfigure(5, weight=1)
        do.rowconfigure(6, weight=1)
        mp.destroy()
        mp.update()
        
        def catcom():
            global boxchecka
            dogcheck.deselect()
            boxchecka = catcheck.get()
        def dogcom():
            global boxchecka
            catcheck.deselect()
            boxchecka = dogcheck.get()
        
        def cp1com():
            global boxcheckp
            cp2check.deselect()
            cp3check.deselect()
            boxcheckp = cp1check.get()
        def cp2com():
            global boxcheckp
            cp1check.deselect()
            cp3check.deselect()
            boxcheckp = cp2check.get()
        def cp3com():
            global boxcheckp
            cp1check.deselect()
            cp2check.deselect()
            boxcheckp = cp3check.get()
        
        def ci1com():
            global boxchecki
            ci2check.deselect()
            ci3check.deselect()
            boxchecki = ci1check.get()
        def ci2com():
            global boxchecki
            ci1check.deselect()
            ci3check.deselect()
            boxchecki = ci2check.get()
        def ci3com():
            global boxchecki
            ci1check.deselect()
            ci2check.deselect()
            boxchecki = ci3check.get()
        
        doartitle = ctki.CTkLabel(do, text='Registro de Características', font = ctki.CTkFont(size=30))
        catcheck = ctki.CTkCheckBox(do, text='Gato', command=catcom)
        dogcheck = ctki.CTkCheckBox(do, text='Cachorro', command=dogcom)
        
        c1check = ctki.CTkCheckBox(do, text='Branco')
        c2check = ctki.CTkCheckBox(do, text='Caramelo')
        c3check = ctki.CTkCheckBox(do, text='Laranja')
        c4check = ctki.CTkCheckBox(do, text='Marrom')
        c5check = ctki.CTkCheckBox(do, text='Cinza')
        c6check = ctki.CTkCheckBox(do, text='Preto')
        
        cp1check = ctki.CTkCheckBox(do, text='Pequeno Porte', command=cp1com)
        cp2check = ctki.CTkCheckBox(do, text='Médio Porte', command=cp2com)
        cp3check = ctki.CTkCheckBox(do, text='Grande Porte', command=cp3com)
        ci1check = ctki.CTkCheckBox(do, text='Filhote', command=ci1com)
        ci2check = ctki.CTkCheckBox(do, text='Adulto', command=ci2com)
        ci3check = ctki.CTkCheckBox(do, text='Idoso', command=ci3com)
#Doação Registro
        def regs():
            regp = ctki.CTkToplevel(janlog)
            regp.title('Registro de Pet')
            regp.geometry('1000x600')

            cor = ''
            global em

            if catcheck.get() == 0:
                an = 'dog'
            else:
                an = 'cat'
            
            if c1check.get() == 1:
                cor += '1'
            if c2check.get() == 1:
                cor += '2'
            if c3check.get() == 1:
                cor += '3'
            if c4check.get() == 1:
                cor += '4'
            if c5check.get() == 1:
                cor += '5'
            if c6check.get() == 1:
                cor += '6'
            
            if cp1check.get() == 1:
                por = 'peq'
            elif cp2check.get() == 1:
                por = 'med'
            else:
                por = 'big'
            
            if ci1check.get() == 1:
                age = 'nov'
            elif ci2check.get() == 1:
                age = 'adt'
            else:
                age = 'old'
            
#Final Doação
            def inse():
                txt = ''
                if len(nentry.get()) < 12 :
                    txt = 'Número inválido'
                elif addentry.get() == '':
                    txt = 'Bairro inválido'
                try: 
                    Image.open('Pets/' + fotentry.get() + '.jpg')
                except:
                    txt = 'Imagem não encontrada'
                try:
                    dba.search(dbq.Foto == fotentry.get() + '.jpg')[0]
                except:
                    ''
                else:
                    txt = 'Animal já registrado'

                if txt == '':

                    def dvol():
                        doasuc.destroy()
                        doasuc.update()
                        mainpage()
                    
                    ft = fotentry.get() + '.jpg'
                    cl = nentry.get()
                    ed = addentry.get()
                    dba.insert({'Tipo': an,'Cor': cor, 'Porte': por,'Idade': age, 
                            'Dono': db.search(dbq.Email == em)[0]['Nome'], 'Conta': em, 'Foto': ft, 
                            'Celular': cl, 'Endereço': ed})
                    regp.destroy()
                    regp.update()
                    
                    
                    doasuc = ctki.CTkToplevel(janlog)
                    doasuc.title('Doação Registrada')
                    doasuc.geometry('500x300')
                    suctxt = ctki.CTkLabel(doasuc, text='Obrigado pela doação', font=ctki.CTkFont(size=20))
                    suctxt2 = ctki.CTkLabel(doasuc, text='Interessados no seu pet entrarão em contato', font=ctki.CTkFont(size=20))
                    doavolt = ctki.CTkButton(doasuc, text='voltar', command=dvol)
                    suctxt.pack(pady = 10)
                    suctxt2.pack(pady = 10)
                    doavolt.pack(pady = 50)
                

                else:
                
                    ner = ctki.CTkToplevel(janlog)
                    ner.geometry('500x300')
                    regp.withdraw()

                    def nerdest():
                        ner.destroy()
                        ner.update()
                        regp.deiconify()

                    ner.title('Erro')
                    typner = ctki.CTkLabel(ner, text=txt, font=ctki.CTkFont(size=20))
                    nerok = ctki.CTkButton(ner, text='OK', command=nerdest)

                    typner.pack(pady = 20)
                    nerok.pack(pady = 20)   

                

            def finvolti():
                regp.destroy()
                regp.update()
                doar()

            def nftc():
                regp.withdraw()
                inst = ctki.CTkToplevel(janlog)
                inst.geometry('700x300')
                inst.title('Como colocar foto')
                inst1 = ctki.CTkLabel(inst, text='Primeiramente salve um arquivo .jpg na pasta Pets localizada na pasta do programa')
                inst2 = ctki.CTkLabel(inst, text='Quando o programa pedir a foto informe o nome do arquivo SEM A TERMINAÇÃO .jpg')
                def inok():
                    inst.destroy()
                    regp.deiconify()
                instok = ctki.CTkButton(inst, text='OK', command=inok)
                inst1.pack(pady = 0)
                inst2.pack(pady = 0)
                instok.pack(pady = 30)
            regptitulo = ctki.CTkLabel(regp, text='Últimas Informações', font = ctki.CTkFont(size=30))
            
            finaln = ctki.CTkLabel(regp, text='Número para contato', font=ctki.CTkFont(size=18))
            nentry = ctki.CTkEntry(regp, placeholder_text='DDD 000000000', width=250)
            
            finaladd = ctki.CTkLabel(regp, text='Bairro', font=ctki.CTkFont(size=18))
            addentry = ctki.CTkEntry(regp, width=250)
            
            finalie = ctki.CTkLabel(regp, text='Foto do animal', font=ctki.CTkFont(size=18))
            fotentry = ctki.CTkEntry(regp, placeholder_text='Nome do arquivo jpg', width=250)
            
            finalizb = ctki.CTkButton(regp, text='Finalizar registro', command=inse)
            nft = ctki.CTkButton(regp, text='Ainda Sem Foto', command=nftc)
            finvolt = ctki.CTkButton(regp, text='voltar', command=finvolti, fg_color='transparent', hover=False, text_color='blue')

            regptitulo.pack(pady = 50)
            finaln.pack(pady = 0)
            nentry.pack(pady = 20)
            finaladd.pack(pady = 0)
            addentry.pack(pady = 20)
            finalie.pack(pady = 0)
            fotentry.pack(pady = 20)
            finalizb.pack(pady = 0)
            nft.pack(pady = 20)
            finvolt.pack(pady = 0)



        def regerr():
            reger = ctki.CTkToplevel(janlog)
            reger.title('Erro no registro')
            reger.geometry('500x300')
            do.withdraw()
            global boxerr
            if boxerr == 1:
                boxerr = 'Tipo do Animal Precisa ser Preenchido'
            elif boxerr == 2:
                boxerr = 'Faixa Etária do Animal Precisa ser Preenchida'
            else:
                boxerr = 'Porte do Animal Precisa ser Preenchido'
            regertyp = ctki.CTkLabel(reger, text=boxerr, font=ctki.CTkFont(size=20))
            regertyp.pack(pady = 40)
            def regeroki():
                reger.destroy()
                reger.update()
                do.deiconify()
            regerok = ctki.CTkButton(reger, text='OK', command=regeroki)
            regerok.pack(pady = 10)
        
        def regcheck():
            global boxerr
            if boxchecka == 0:
                boxerr = 1
                regerr()
            elif boxchecki == 0:
                boxerr = 2
                regerr()
            elif boxcheckp == 0:
                regerr()
            else:
                regs()
                do.withdraw()

        
        def dovolti():
            do.destroy()
            do.update()
            mainpage()
        regsbutton = ctki.CTkButton(do, text='Póxima Etapa', command=regcheck)
        dovolt = ctki.CTkButton(do, text='voltar', command=dovolti, fg_color='transparent', hover=False, text_color='blue')

        doartitle.grid(row = 0, column = 2, sticky = 'w')
        
        catcheck.grid(row = 0, column = 1, ipadx = 10, ipady = 10, sticky = 'we')
        dogcheck.grid(row = 0, column = 3, ipadx = 10, ipady = 10, sticky = 'we')
        
        c1check.grid(row = 1, column = 1, ipadx = 10, ipady = 10, sticky = 'we')
        c2check.grid(row = 2, column = 1, ipadx = 10, ipady = 10, sticky = 'we')
        c3check.grid(row = 3, column = 1, ipadx = 10, ipady = 10, sticky = 'we')
        c4check.grid(row = 4, column = 1, ipadx = 10, ipady = 10, sticky = 'we')
        c5check.grid(row = 5, column = 1, ipadx = 10, ipady = 10, sticky = 'we')
        c6check.grid(row = 6, column = 1, ipadx = 10, ipady = 10, sticky = 'we')

        cp1check.grid(row = 1, column = 3, ipadx = 10, ipady = 10, sticky = 'we')
        cp2check.grid(row = 2, column = 3, ipadx = 10, ipady = 10, sticky = 'we')
        cp3check.grid(row = 3, column = 3, ipadx = 10, ipady = 10, sticky = 'we')
        ci1check.grid(row = 4, column = 3, ipadx = 10, ipady = 10, sticky = 'we')
        ci2check.grid(row = 5, column = 3, ipadx = 10, ipady = 10, sticky = 'we')
        ci3check.grid(row = 6, column = 3, ipadx = 10, ipady = 10, sticky = 'we')

        regsbutton.grid(row = 5, column = 2)
        dovolt.grid(row = 6, column = 2, sticky = 'N')

    
#Seu Perfil
    def perfi():
        global em
        perfil = ctki.CTkToplevel(janlog)
        perfil.geometry('1000x600')
        perfil.title('Perfil')
        mp.destroy()
        mp.update()
        pertit = ctki.CTkLabel(perfil, text='Meu Perfil', font= ctki.CTkFont(family='Open_Sans', size=40 ))
        infem = ctki.CTkLabel(perfil, text='E-mail: ' + em, font= ctki.CTkFont(family='Open_Sans', size=20 ))
        infnom=ctki.CTkLabel(perfil,text='Nome: '+db.search(dbq.Email==em)[0]['Nome'],font= ctki.CTkFont(family='Open_Sans', size=20 ))
        def inf():
            perfil.destroy()
            perfil.update()
            infc = ctki.CTkToplevel(janlog)
            infc.geometry('1000x500')
            infc.title('Trocar Informações')
            inflb = ctki.CTkLabel(infc, text='Alterar Informações', font= ctki.CTkFont(family='Open_Sans', size=30))
            infq = ctki.CTkLabel(infc, text='Qual informação deve ser alterada?', font= ctki.CTkFont(family='Open_Sans', size=20))
#Alterar Email
            def altem():
                infc.destroy()
                infc.update()
                emar = ctki.CTkToplevel(janlog)
                emar.geometry('500x300')
                emar.title('Alterar Email')
                emarla = ctki.CTkLabel(emar, text='Alterar Email', font= ctki.CTkFont(family='Open_Sans', size=25))
                eman = ctki.CTkLabel(emar, text='E-mail antigo: ' + em, font= ctki.CTkFont(size=20))
                emnvl = ctki.CTkLabel(emar, text='Informe o novo Email', font= ctki.CTkFont(size=20 ))
                emnv = ctki.CTkEntry(emar)
                def emcheck():
                    global em
                    er = ''
                    im = emnv.get()
                    emar.destroy()
                    emar.update()
                    if im == '' or im.count('@') != 1:
                        er = 'Email inválido'
                    elif im == em:
                        er = 'Novo Email deve ser diferente do anterior'
                    elif db.search(dbq.Email == im) != []:
                        er = 'Email já existente'
                    else:
                        er = 'ok'
                    if er == 'ok':
                        emck = ctki.CTkToplevel(janlog)
                        emck.geometry('500x300')
                        emck.title('Confirmar Email')
                        nvem = ctki.CTkLabel(emck, text='Novo Email: ' + im, font=ctki.CTkFont(size = 20))
                        def nem():
                            global em
                            emck.destroy()
                            emck.update()
                            dba.update({'Conta':im}, dbq.Conta == em)
                            db.update({'Email':im}, dbq.Email == em)
                            em = im
                            perfi()
                        nvemcon = ctki.CTkButton(emck, text='Confirmar', command=nem)
                        
                        def cnc():
                            emck.destroy()
                            emck.update()
                            altem()
                        nvemvol = ctki.CTkButton(emck, text='cancelar', text_color='blue', hover=False, fg_color='transparent', command=cnc)
                        nvem.pack(pady = 20)
                        nvemcon.pack(pady = 10)
                        nvemvol.pack(pady = 10)
                    else:
                        nvemer = ctki.CTkToplevel(janlog)
                        nvemer.geometry('500x300')
                        nvemer.title('Erro')
                        erla = ctki.CTkLabel(nvemer, text=er,  font=ctki.CTkFont(size=20))
                        def emro():
                            nvemer.destroy()
                            nvemer.update()
                            altem()
                        emrok = ctki.CTkButton(nvemer, text='OK', command=emro)
                        erla.pack(pady = 20)
                        emrok.pack(pady = 20)
                emnvok = ctki.CTkButton(emar, text='OK', command=emcheck)
                def emvol():
                    emar.destroy()
                    emar.update()
                    perfi()
                emnvol = ctki.CTkButton(emar, text='voltar', text_color='blue', hover=False, fg_color='transparent', command=emvol)
                emarla.pack(pady = 20)
                eman.pack(pady = 10)
                emnvl.pack(pady = 10)
                emnv.pack(pady = 0)
                emnvok.pack(pady = 20)
                emnvol.pack(pady = 0)
            chem = ctki.CTkButton(infc, text='Email', command=altem)
#Alterar Nome
            def altnom():
                infc.destroy()
                infc.update()
                nmar = ctki.CTkToplevel(janlog)
                nmar.geometry('500x300')
                nmar.title('Alterar Nome')
                nmarla = ctki.CTkLabel(nmar, text='Alterar Nome', font= ctki.CTkFont(family='Open_Sans', size=25))
                nman = ctki.CTkLabel(nmar, text='Nome antigo: ' + db.search(dbq.Email == em)[0]['Nome'], font= ctki.CTkFont(size=20))
                nmnvl = ctki.CTkLabel(nmar, text='Informe o novo Nome', font= ctki.CTkFont(size=20 ))
                nmnv = ctki.CTkEntry(nmar)
                def nmcheck():
                    global em
                    er = ''
                    im = nmnv.get()
                    nmar.destroy()
                    nmar.update()
                    if im == '':
                        er = 'Nome inválido'
                    elif im == db.search(dbq.Email == em)[0]['Nome']:
                        er = 'Novo Nome deve ser diferente do anterior'
                    else:
                        er = 'ok'
                    if er == 'ok':
                        nmck = ctki.CTkToplevel(janlog)
                        nmck.geometry('500x300')
                        nmck.title('Confirmar Email')
                        nvnm = ctki.CTkLabel(nmck, text='Novo Nome: ' + im, font=ctki.CTkFont(size = 20))
                        def nnm():
                            global em
                            nmck.destroy()
                            nmck.update()
                            dba.update({'Dono':im}, dbq.Conta == em)
                            db.update({'Nome':im}, dbq.Email == em)
                            perfi()
                        nvnmcon = ctki.CTkButton(nmck, text='Confirmar', command=nnm)
                        
                        def cncnm():
                            nmck.destroy()
                            nmck.update()
                            altnom()
                        nvnmvol = ctki.CTkButton(nmck, text='cancelar', text_color='blue', hover=False, fg_color='transparent', command=cncnm)
                        nvnm.pack(pady = 20)
                        nvnmcon.pack(pady = 10)
                        nvnmvol.pack(pady = 10)
                    else:
                        nvnmer = ctki.CTkToplevel(janlog)
                        nvnmer.geometry('500x300')
                        nvnmer.title('Erro')
                        erlanm = ctki.CTkLabel(nvnmer, text=er, font=ctki.CTkFont(size=20))
                        def nmro():
                            nvnmer.destroy()
                            nvnmer.update()
                            altnom()
                        nmrok = ctki.CTkButton(nvnmer, text='OK', command=nmro)
                        erlanm.pack(pady = 20)
                        nmrok.pack(pady = 20)
                nmnvok = ctki.CTkButton(nmar, text='OK', command=nmcheck)
                def nmvol():
                    nmar.destroy()
                    nmar.update()
                    perfi()
                nmnvol = ctki.CTkButton(nmar, text='voltar', text_color='blue', hover=False, fg_color='transparent', command=nmvol)
                nmarla.pack(pady = 20)
                nman.pack(pady = 10)
                nmnvl.pack(pady = 10)
                nmnv.pack(pady = 0)
                nmnvok.pack(pady = 20)
                nmnvol.pack(pady = 0)
            chnom = ctki.CTkButton(infc, text='Nome', command=altnom)
#Alterar Senha
            def altsn():
                infc.destroy()
                infc.update()
                snar = ctki.CTkToplevel(janlog)
                snar.geometry('500x300')
                snar.title('Alterar Senha')
                snarla = ctki.CTkLabel(snar, text='Alterar Senha', font= ctki.CTkFont(family='Open_Sans', size=25))
                snan = ctki.CTkLabel(snar, text='Senha antiga: ' + db.search(dbq.Email == em)[0]['Senha'], font= ctki.CTkFont(size=20))
                snnvl = ctki.CTkLabel(snar, text='Informe a nova Senha', font= ctki.CTkFont(size=20 ))
                snnv = ctki.CTkEntry(snar)
                def sncheck():
                    global em
                    er = ''
                    im = snnv.get()
                    snar.destroy()
                    snar.update()
                    if im == '' or len(im) < 6:
                        er = 'Senha inválida'
                    elif im == db.search(dbq.Email == em)[0]['Senha']:
                        er = 'Nova Senha deve ser diferente da anterior'
                    else:
                        er = 'ok'
                    if er == 'ok':
                        snck = ctki.CTkToplevel(janlog)
                        snck.geometry('500x300')
                        snck.title('Confirmar Senha')
                        nvsn = ctki.CTkLabel(snck, text='Nova Senha: ' + im, font=ctki.CTkFont(size=20))
                        def nemsn():
                            global em
                            snck.destroy()
                            snck.update()
                            db.update({'Senha':im}, dbq.Email == em)
                            perfi()
                        nvsncon = ctki.CTkButton(snck, text='Confirmar', command=nemsn)
                        
                        def cncsn():
                            snck.destroy()
                            snck.update()
                            altsn()
                        nvsnvol = ctki.CTkButton(snck, text='cancelar', text_color='blue', hover=False, fg_color='transparent', command=cncsn)
                        nvsn.pack(pady = 20)
                        nvsncon.pack(pady = 10)
                        nvsnvol.pack(pady = 10)
                    else:
                        nvsner = ctki.CTkToplevel(janlog)
                        nvsner.geometry('500x300')
                        nvsner.title('Erro')
                        erlasn = ctki.CTkLabel(nvsner, text=er, font=ctki.CTkFont(size=20))
                        def snro():
                            nvsner.destroy()
                            nvsner.update()
                            altsn()
                        snrok = ctki.CTkButton(nvsner, text='OK', command=snro)
                        erlasn.pack(pady = 20)
                        snrok.pack(pady = 20)
                snnvok = ctki.CTkButton(snar, text='OK', command=sncheck)
                def snvol():
                    snar.destroy()
                    snar.update()
                    perfi()
                snnvol = ctki.CTkButton(snar, text='voltar', text_color='blue', hover=False, fg_color='transparent', command=snvol)
                snarla.pack(pady = 20)
                snan.pack(pady = 10)
                snnvl.pack(pady = 10)
                snnv.pack(pady = 0)
                snnvok.pack(pady = 20)
                snnvol.pack(pady = 0)
            chsn = ctki.CTkButton(infc, text='Senha', command=altsn)
#Alterar Pergunta de Segurança
            def altper():
                infc.destroy()
                infc.update()
                perar = ctki.CTkToplevel(janlog)
                perar.geometry('750x450')
                perar.title('Alterar Pergunta de Segurança')
                perarla = ctki.CTkLabel(perar, text='Alterar Pergunta de Segurança', font= ctki.CTkFont(family='Open_Sans', size=25))
                peran = ctki.CTkLabel(perar, text='Pergunta antiga: ' + db.search(dbq.Email == em)[0]['Pergunta'], font=ctki.CTkFont(size=20))
                pernvl = ctki.CTkLabel(perar, text='Informe a nova Pergunta', font=ctki.CTkFont(size=20))
                pernv = ctki.CTkEntry(perar, width=250)
                renvl = ctki.CTkLabel(perar, text='Informe a Resposta da Pergunta', font=ctki.CTkFont(size=20))
                renv = ctki.CTkEntry(perar, width=250)
                def percheck():
                    global em
                    er = ''
                    im = pernv.get()
                    im2 = renv.get()
                    perar.destroy()
                    perar.update()
                    if im == '':
                        er = 'Pergunta inválida'
                    elif im == db.search(dbq.Email == em)[0]['Pergunta']:
                        er = 'Nova Pergunta deve ser diferente da anterior'
                    elif im2 == '':
                        er = 'Resposta inválida'
                    elif im2 == db.search(dbq.Email == em)[0]['Resposta']:
                        er = 'Nova Resposta deve ser diferente da anterior'
                    else:
                        er = 'ok'
                    if er == 'ok':
                        perck = ctki.CTkToplevel(janlog)
                        perck.geometry('500x300')
                        perck.title('Confirmar Pergunta')
                        nvper = ctki.CTkLabel(perck, text='Nova Pergunta: ' + im, font=ctki.CTkFont(size=20))
                        nvrer = ctki.CTkLabel(perck, text='Nova Resposta: ' + im2, font=ctki.CTkFont(size=20))
                        def nemsn():
                            global em
                            perck.destroy()
                            perck.update()
                            db.update({'Pergunta':im}, dbq.Email == em)
                            db.update({'Resposta':im2}, dbq.Email == em)
                            perfi()
                        nvpercon = ctki.CTkButton(perck, text='Confirmar', command=nemsn)
                        
                        def cncper():
                            perck.destroy()
                            perck.update()
                            altper()
                        nvpervol = ctki.CTkButton(perck, text='cancelar', text_color='blue', hover=False, fg_color='transparent', command=cncper)
                        nvper.pack(pady = 10)
                        nvrer.pack(pady = 20)
                        nvpercon.pack(pady = 10)
                        nvpervol.pack(pady = 10)
                    else:
                        nvperer = ctki.CTkToplevel(janlog)
                        nvperer.geometry('500x300')
                        nvperer.title('Erro')
                        erlaper = ctki.CTkLabel(nvperer, text=er, font=ctki.CTkFont(size=20))
                        def perro():
                            nvperer.destroy()
                            nvperer.update()
                            altper()
                        perrok = ctki.CTkButton(nvperer, text='OK', command=perro)
                        erlaper.pack(pady = 20)
                        perrok.pack(pady = 20)
                pernvok = ctki.CTkButton(perar, text='OK', command=percheck)
                def pervol():
                    perar.destroy()
                    perar.update()
                    perfi()
                pernvol = ctki.CTkButton(perar, text='voltar', text_color='blue', hover=False, fg_color='transparent', command=pervol)
                perarla.pack(pady = 30)
                peran.pack(pady = 20)
                pernvl.pack(pady = 10)
                pernv.pack(pady = 0)
                renvl.pack(pady = 10)
                renv.pack(pady = 0)
                pernvok.pack(pady = 10)
                pernvol.pack(pady = 0)
            chpr = ctki.CTkButton(infc, text='Pergunta de Segurança', command=altper)

            def volin():
                infc.destroy()
                infc.update()
                perfi()
            invol = ctki.CTkButton(infc, text='voltar', text_color='blue', hover=False, fg_color='transparent', command=volin)
            inflb.pack(pady = 30)
            infq.pack(pady = 20)
            chem.pack(pady = 10)
            chnom.pack(pady = 10)
            chsn.pack(pady = 10)
            chpr.pack(pady = 10)
            invol.pack(pady = 30)
        infch = ctki.CTkButton(perfil, text='Mudar Informações', command=inf)
        def delt():
            perfil.destroy()
            perfil.update()
            delfir = ctki.CTkToplevel(janlog)
            delfir.geometry('500x300')
            della = ctki.CTkLabel(delfir, text='Deseja mesmo Apagar sua conta?', font=ctki.CTkFont(size=20))
            def apg():
                delfir.destroy()
                delfir.update()
                dba.remove(cond= dbq.Conta == em)
                db.remove(cond= dbq.Email == em)
                apgsuc = ctki.CTkToplevel(janlog)
                apgsuc.geometry('500x300')
                apgsuc.title('Conta Apagada')
                apgla = ctki.CTkLabel(apgsuc, text='Conta deletada com sucesso', font=ctki.CTkFont(size=20))
                def apok():
                    apgsuc.destroy()
                    apgsuc.update()
                    janlog.deiconify()
                    logemail.delete(0, )
                    logsenha.delete(0)
                apgok = ctki.CTkButton(apgsuc, text='OK', command=apok)
                apgla.pack(pady = 50)
                apgok.pack(pady = 10)
            delok = ctki.CTkButton(delfir, text='SIM', hover_color='red', command=apg)
            def volde():
                delfir.destroy()
                delfir.update()
                perfi()
            delvol = ctki.CTkButton(delfir, text='NÃO', command=volde)
            della.pack(pady = 50)
            delok.pack(pady = 10)
            delvol.pack(pady = 10)
        condel = ctki.CTkButton(perfil, text='Apagar Conta', command=delt)
#Minhas doações
        def minhas():
            global em
            perfil.destroy()
            perfil.update()
            if not dba.search(dbq.Conta == em):
                minde = ctki.CTkToplevel(janlog)
                minde.title('Sem Doações')
                minde.geometry('500x300')
                nod = ctki.CTkLabel(minde, text='Nenhuma Doação Registrada', font=ctki.CTkFont(size=20))

                def mindemp():
                    perfi()
                    minde.destroy()
                    minde.update()

                nodok = ctki.CTkButton(minde, text='OK', command=mindemp)
                nod.pack(pady = 20)
                nodok.pack(pady = 60)
            else:
                mind = ctki.CTkToplevel(janlog)
                mind.title('Minhas Doações')
                mind.geometry('1000x600')
                mindtit = ctki.CTkLabel(mind, text='Lista de Doações', font=ctki.CTkFont(size = 25))
                mindlst = ctki.CTkScrollableFrame(mind, height=400, width=800)
                mindtit.pack(pady = 20)
                mindlst.pack(pady = 20)
                for i in dba.search(dbq.Conta == em):
                    img = 'Pets/' + i['Foto']
                    mindim = ctki.CTkImage(light_image=Image.open(img), dark_image=Image.open(img), size=[150, 150])
                    mindimg = ctki.CTkLabel(mindlst, image=mindim, text='')
                    fi = i['Foto'].split('.jpg')[0]
                    mindtxt = ctki.CTkLabel(mindlst, text= fi)
                    mindimg.pack(pady = 0)
                    mindtxt.pack(pady = 5)

#Remover uma doação  
                def rem():
                    remv = ctki.CTkToplevel()
                    remv.geometry('500x300')
                    remv.title('remover uma doação')
                    mind.destroy()
                    mind.update()
                    remtxt = ctki.CTkLabel(remv, text='nome do pet que quer remover', font=ctki.CTkFont(size=20))
                    rement = ctki.CTkEntry(remv, placeholder_text='nome da foto')
                    def remcheck():
                        r = rement.get()
                        remv.destroy()
                        remv.update()
                    

                        try:
                            dba.search(dbq.Foto == r + '.jpg')[0]['Conta']

                        except:
                            remer = ctki.CTkToplevel(janlog)
                            remer.geometry('500x300')
                            remer.title('imagem não encontrada')
                            reme = ctki.CTkLabel(remer, text='imagem não encontrada', font=ctki.CTkFont(size=20))
                            def reok():
                                remer.destroy()
                                remer.update()
                                rem()
                            remerok = ctki.CTkButton(remer, text='OK', command=reok)
                            reme.pack(pady = 10)
                            remerok.pack(pady = 10)
                        else:
                            if dba.search(dbq.Foto == r + '.jpg')[0]['Conta'] == em:
                        
                                rmv = ctki.CTkToplevel(janlog)
                                rmv.geometry('500x300')
                                rmv.title('confirmar remoção')
                                rmvtxt = ctki.CTkLabel(rmv, text='corfirmar remoção de: '+ r, font=ctki.CTkFont(size=20))
                                def rok():
                                    dba.remove(cond= dbq.Foto == r + '.jpg')
                                    remf = ctki.CTkToplevel(janlog)
                                    remf.geometry('500x300')
                                    remf.title('remoção concluída')
                            
                                    def remfoki():
                                        remf.destroy()
                                        remf.update()
                                        rem()

                                    remtt = ctki.CTkLabel(remf, text='Remoção concluída', font=ctki.CTkFont(size=20))
                                    remfok = ctki.CTkButton(remf, text='OK', command=remfoki)
                                    remtt.pack(pady = 10)
                                    remfok.pack(pady = 40)
                                    rmv.destroy()
                                    rmv.update()
                                def cnc():
                                    rmv.destroy()
                                    rmv.update()
                                    rem()

                                rmvok = ctki.CTkButton(rmv, text='remover',hover_color='red', command=rok)
                                rmvnot = ctki.CTkButton(rmv, text='cancelar', command=cnc)
                        
                                rmvtxt.pack(pady = 10)
                                rmvok.pack(pady = 10)
                                rmvnot.pack(pady = 10)
                            else:
                                remer = ctki.CTkToplevel(janlog)
                                remer.geometry('500x300')
                                remer.title('esse pet não pertence a essa conta')
                                reme = ctki.CTkLabel(remer, text='imagem não encontrada', font=ctki.CTkFont(size=20))
                                def reok():
                                    remer.destroy()
                                    remer.update()
                                    rem()
                                remerok = ctki.CTkButton(remer, text='OK', command=reok)
                                reme.pack(pady = 10)
                                remerok.pack(pady = 10)



                    remok = ctki.CTkButton(remv, text='remover', command=remcheck)
                    def remvoli():
                        remv.destroy()
                        remv.update()
                        minhas()

                    remvol = ctki.CTkButton(remv, text='voltar', text_color='blue', hover=False, fg_color='transparent', command=remvoli)
                
                    remtxt.pack(pady = 10)
                    rement.pack(pady = 10)
                    remok.pack(pady = 10)
                    remvol.pack(pady = 0)

                    
                mindbut = ctki.CTkButton(mind, text='remover um pet', command=rem)
                mindbut.pack(pady = 10)
            
                def mindmp():
                    perfi()
                    mind.destroy()
                    mind.update()

                mindvolt = ctki.CTkButton(mind, text='voltar', command=mindmp, fg_color='transparent', hover=False, text_color='blue')
                mindvolt.pack(pady = 0)
        doacoes = ctki.CTkButton(perfil, text='Minhas Doações', command=minhas)
        def pevol():
            perfil.destroy()
            perfil.update()
            mainpage()
        pervol = ctki.CTkButton(perfil, text='voltar', text_color='blue', fg_color='transparent', hover=False, command=pevol)
        pertit.pack(pady = 50)
        infem.pack(pady = 10)
        infnom.pack(pady = 20)
        infch.pack(pady = 20)
        condel.pack(pady = 10)
        doacoes.pack(pady = 20)
        pervol.pack(pady = 20)        
    mptitulo = ctki.CTkLabel(mp, text = 'Adote um Pet',font= ctki.CTkFont(family='Open_Sans', size=60))
    mpadotar = ctki.CTkButton(mp, text='Adotar', command=adotar)
    mpdoar = ctki.CTkButton(mp, text='Doar', command=doar)
    mpdoacoes = ctki.CTkButton(mp, text='Meu Perfil',command=perfi)
    mpvoltar = ctki.CTkButton(mp, text='voltar',text_color='blue', fg_color='transparent', hover=False, command=voltar)
    

    mptitulo.pack(pady = 100)
    mpadotar.pack(pady = 10)
    mpdoar.pack(pady = 10)
    mpdoacoes.pack(pady = 10)
    mpvoltar.pack(pady = 20)


janlog.mainloop()

