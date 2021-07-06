import PySimpleGUI as sg
sg.theme('Dark blue')
layout =[              
        [sg.Text("Quantos resistores?: ")],
        [sg.Button("paralelo 2", key=(1.2), size=(8,3)),
        sg.Button("serie 2",     key=(2.2), size=(8,3))],
        [sg.Button("paralelo 3", key=(1.3), size=(8,3)),
        sg.Button("serie 3",     key=(2.3), size=(8,3))],
        [sg.Button("paralelo 4", key=(1.4), size=(8,3)),
        sg.Button("Série 4",     key=(2.4), size=(8,3))],
        [sg.Button("paralelo 5", key=(1.5), size=(8,3)),
        sg.Button("Série 5",     key=(2.5), size=(8,3))]]
window = sg.Window('calculos de resistores',size=(400,700)).layout(layout)
while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:  
                break
        if event == (1.2):                
                window.hide()
                layout2 = [
                        [sg.Text("Qual é a Voltagem?:                " ),sg.Input(              key=1.1                   )],
                        [sg.Text("Qual é o primeiro resistor?:       " ),sg.Input(              key=1.2                   )],
                        [sg.Text("Qual é o segundo resistor?:       "  ),sg.Input(              key=1.3                   )],
                        [sg.Text('A resistencia equivalente é:  '      ),sg.Text(size=(5,1),    key='1.1.1'), sg.Text('Ω')],
                        [sg.Text('Tensão total:                      ' ),sg.Text(size=(5,1),    key='1.1.2'), sg.Text('A')],
                        [sg.Text('corrente inteira:                  ' ),sg.Text(size=(5,1),    key='1.1.3'), sg.Text('W')],
                        [sg.Text('corrente do resistor 1:         '    ),sg.Text(size=(5,1 ),   key='1.2.1'), sg.Text('A')],
                        [sg.Text('corrente do resistor 2:         '    ),sg.Text(size=(5,1 ),   key='1.2.2'), sg.Text('A')],
                        [sg.Text('Potencia 1:                         '),sg.Text(size=(5,1),    key='1.3.1'), sg.Text('W')],
                        [sg.Text('Potencia 2:                         '),sg.Text(size=(5,1),    key='1.3.2'), sg.Text('W')],                        
                        [sg.Button('calcular'                          ),sg.Button('Exit'                                )]]
                window2 = sg.Window("2 resistores em paralelo", layout2,size=(400,700))        
                while True:
                        event2, values2 = window2.read()
                        if event2 == 'calcular':                                
                                v = int(values2[1.1])
                                a = int(values2[1.2])
                                b = int(values2[1.3])
                                req = ((a*b)/(a+b))
                                Vreq = v / req
                                ReqT = v * Vreq
                                Ir1 = v / a
                                Ir2 = v / b
                                Wr1 = Ir1 * v
                                Wr2 = Ir2 * v                                
                                window2['1.1.1'].update(req)
                                window2['1.1.2'].update(Vreq)
                                window2['1.1.3'].update(ReqT)
                                window2['1.2.1'].update(Ir1)
                                window2['1.2.2'].update(Ir2)
                                window2['1.3.1'].update(Wr1)
                                window2['1.3.2'].update(Wr2)                                
                        if event2 == 'Exit' or event2 == sg.WIN_CLOSED:
                                window2.close()                                                           
                                window.UnHide()                                
                                break                                     
        if event == (1.3):                
                window.hide()
                layout3 = [
                        [sg.Text("Qual é a Voltagem?:          "       ),sg.Input               (key=1.1                  )],
                        [sg.Text("Qual é o primeiro resistor?: "       ),sg.Input               (key=1.2                  )],
                        [sg.Text("Qual é o segundo resistor?:"         ),sg.Input               (key=1.3                  )],
                        [sg.Text("Qual é o terceiro resistor?: "       ),sg.Input               (key=1.4                  )],
                        [sg.Text('a resistencia equivalente é:'        ),sg.Text(size=(5,1),     key='1.1.1'), sg.Text('Ω')],
                        [sg.Text('Tensão total:                    '   ),sg.Text(size=(5,1),     key='1.1.2'), sg.Text('A')],
                        [sg.Text('corrente inteira:                '   ),sg.Text(size=(5,1),     key='1.1.3'), sg.Text('W')],
                        [sg.Text('corrente do resistor 1:       '      ),sg.Text(size=(5,1),     key='1.2.1'), sg.Text('A')],
                        [sg.Text('corrente do resistor 2:       '      ),sg.Text(size=(5,1),     key='1.2.2'), sg.Text('A')],
                        [sg.Text('corrente do resistor 3:       '      ),sg.Text(size=(5,1),     key='1.2.3'), sg.Text('A')],
                        [sg.Text('Potencia 1:                       '  ),sg.Text(size=(5,1),     key='1.3.1'), sg.Text('W')],
                        [sg.Text('Potencia 2:                       '  ),sg.Text(size=(5,1),     key='1.3.2'), sg.Text('W')],
                        [sg.Text('Potencia 3:                       '  ),sg.Text(size=(5,1),     key='1.3.3'), sg.Text('W')],                        
                        [sg.Button('calcular'                          ),sg.Button('Exit'                                 )]]
                window3 = sg.Window("3 resistores em paralelo", layout3,size=(400,700))        
                while True:
                        event3, values3 = window3.read()
                        if event3 == 'calcular':                               
                                v = int(values3[1.1])
                                a = int(values3[1.2])                                
                                b = int(values3[1.3])
                                c = int(values3[1.4])
                                req = 1/((1/c)+(1/b)+(1/a))
                                Vreq = v / req
                                ReqT = v * Vreq
                                Ir1 = v / a
                                Ir2 = v / b
                                Ir3 = v / c
                                Wr1 = Ir1 * v
                                Wr2 = Ir2 * v
                                Wr3 = Ir3 * v                                
                                window3['1.1.1'].update(req)
                                window3['1.1.2'].update(Vreq)
                                window3['1.1.3'].update(ReqT)
                                window3['1.2.1'].update(Ir1)
                                window3['1.2.2'].update(Ir2)
                                window3['1.2.3'].update(Ir3)
                                window3['1.3.1'].update(Wr1)
                                window3['1.3.2'].update(Wr2)
                                window3['1.3.3'].update(Wr3)                                
                        if event3 == 'Exit' or event3 == sg.WIN_CLOSED:
                                window3.close()                                                           
                                window.UnHide()                                
                                break                                          
        if event == (1.4):                
                window.hide()
                layout4 = [
                        [sg.Text("Qual é a Voltagem?:          "       ),sg.Input               (key=1.1                  )],
                        [sg.Text("Qual é o primeiro resistor?: "       ),sg.Input               (key=1.2                  )],
                        [sg.Text("Qual é o segundo resistor?:"         ),sg.Input               (key=1.3                  )],
                        [sg.Text("Qual é o terceiro resistor?: "       ),sg.Input               (key=1.4                  )],
                        [sg.Text("Qual é o quatro resistor?:   "       ),sg.Input               (key=1.5                  )],
                        [sg.Text('a resistencia equivalente é:'        ),sg.Text(size=(5,1),     key='1.1.1'), sg.Text('Ω')],
                        [sg.Text('Tensão total:                    '   ),sg.Text(size=(5,1),     key='1.1.2'), sg.Text('A')],
                        [sg.Text('corrente inteira:                '   ),sg.Text(size=(5,1),     key='1.1.3'), sg.Text('W')],
                        [sg.Text('corrente do resistor 1:       '      ),sg.Text(size=(5,1),     key='1.2.1'), sg.Text('A')],
                        [sg.Text('corrente do resistor 2:       '      ),sg.Text(size=(5,1),     key='1.2.2'), sg.Text('A')],
                        [sg.Text('corrente do resistor 3:       '      ),sg.Text(size=(5,1),     key='1.2.3'), sg.Text('A')],
                        [sg.Text('corrente do resistor 4:       '      ),sg.Text(size=(5,1),     key='1.2.4'), sg.Text('A')],
                        [sg.Text('Potencia 1:                       '  ),sg.Text(size=(5,1),     key='1.3.1'), sg.Text('W')],
                        [sg.Text('Potencia 2:                       '  ),sg.Text(size=(5,1),     key='1.3.2'), sg.Text('W')],
                        [sg.Text('Potencia 3:                       '  ),sg.Text(size=(5,1),     key='1.3.3'), sg.Text('W')],
                        [sg.Text('Potencia 4:                       '  ),sg.Text(size=(5,1),     key='1.3.4'), sg.Text('W')],                     
                        [sg.Button('calcular'                          ),sg.Button('Exit'                                 )]]
                window4 = sg.Window("4 resistores em paralelo", layout4,size=(700,700))        
                while True:
                        event4, values4 = window4.read()
                        if event4 == 'calcular':                                
                                v = int(values4[1.1])
                                a = int(values4[1.2])                                
                                b = int(values4[1.3])
                                c = int(values4[1.4])
                                d = int(values4[1.5])
                                req = 1/((1/c)+(1/b)+(1/a)+(1/d))
                                Vreq = v / req
                                ReqT = v * Vreq
                                Ir1 = v / a
                                Ir2 = v / b
                                Ir3 = v / c
                                Ir4 = v / d                                
                                Wr1 = Ir1 * v
                                Wr2 = Ir2 * v
                                Wr3 = Ir3 * v 
                                Wr4 = Ir4 * v                                
                                window4['1.1.1'].update(req)
                                window4['1.1.2'].update(Vreq)
                                window4['1.1.3'].update(ReqT)
                                window4['1.2.1'].update(Ir1)
                                window4['1.2.2'].update(Ir2)
                                window4['1.2.3'].update(Ir3)
                                window4['1.2.4'].update(Ir4)
                                window4['1.3.1'].update(Wr1)
                                window4['1.3.2'].update(Wr2)
                                window4['1.3.3'].update(Wr3)
                                window4['1.3.4'].update(Wr4)                                
                        if event4 == 'Exit' or event4 == sg.WIN_CLOSED:
                                window4.close()                                                           
                                window.UnHide()                                
                                break                                
        if event == (1.5):                
                window.hide()
                layout5 = [
                        [sg.Text("Qual é a Voltagem?:          "        ),sg.Input              (key=1.1                  )],
                        [sg.Text("Qual é o primeiro resistor?: "        ),sg.Input              (key=1.2                  )],
                        [sg.Text("Qual é o segundo resistor?:"          ),sg.Input              (key=1.3                  )],
                        [sg.Text("Qual é o terceiro resistor?: "        ),sg.Input              (key=1.4                  )],
                        [sg.Text("Qual é o quatro resistor?:   "        ),sg.Input              (key=1.5                  )],
                        [sg.Text("Qual é o quinto resistor?:   "        ),sg.Input              (key=1.6                  )],
                        [sg.Text('a resistencia equivalente é:'         ),sg.Text(size=(5,1),    key='1.1.1'), sg.Text('Ω')],
                        [sg.Text('Tensão total:                    '    ),sg.Text(size=(5,1),    key='1.1.2'), sg.Text('A')],
                        [sg.Text('corrente inteira:                '    ),sg.Text(size=(5,1),    key='1.1.3'), sg.Text('W')],
                        [sg.Text('corrente do resistor 1:       '       ),sg.Text(size=(5,1),    key='1.2.1'), sg.Text('A')],
                        [sg.Text('corrente do resistor 2:       '       ),sg.Text(size=(5,1),    key='1.2.2'), sg.Text('A')],
                        [sg.Text('corrente do resistor 3:       '       ),sg.Text(size=(5,1),    key='1.2.3'), sg.Text('A')],
                        [sg.Text('corrente do resistor 4:       '       ),sg.Text(size=(5,1),    key='1.2.4'), sg.Text('A')],
                        [sg.Text('corrente do resistor 5:       '       ),sg.Text(size=(5,1),    key='1.2.5'), sg.Text('A')],
                        [sg.Text('Potencia 1:                       '   ),sg.Text(size=(5,1),    key='1.3.1'), sg.Text('W')],
                        [sg.Text('Potencia 2:                       '   ),sg.Text(size=(5,1),    key='1.3.2'), sg.Text('W')],
                        [sg.Text('Potencia 3:                       '   ),sg.Text(size=(5,1),    key='1.3.3'), sg.Text('W')],
                        [sg.Text('Potencia 4:                       '   ),sg.Text(size=(5,1),    key='1.3.4'), sg.Text('W')],
                        [sg.Text('Potencia 5:                       '   ),sg.Text(size=(5,1),    key='1.3.5'), sg.Text('W')],                     
                        [sg.Button('calcular'                           ),sg.Button('Exit'                                )]]
                window5 = sg.Window("5 resistores em paralelo", layout5,size=(700,700))        
                while True:
                        event5, values5 = window5.read()
                        if event5 == 'calcular':                                
                                v = int(values5[1.1])
                                a = int(values5[1.2])                                
                                b = int(values5[1.3])
                                c = int(values5[1.4])
                                d = int(values5[1.5])
                                e = int(values5[1.6])
                                req = (1/((1/c)+(1/b)+(1/a)+(1/d)+(1/e)))
                                Vreq = v / req
                                ReqT = v * Vreq
                                Ir1 = v / a
                                Ir2 = v / b
                                Ir3 = v / c
                                Ir4 = v / d
                                Ir5 = v / e                               
                                Wr1 = Ir1 * v
                                Wr2 = Ir2 * v
                                Wr3 = Ir3 * v 
                                Wr4 = Ir4 * v
                                Wr5 = Ir5 * v                                
                                window5['1.1.1'].update(req)
                                window5['1.1.2'].update(Vreq)
                                window5['1.1.3'].update(ReqT)
                                window5['1.2.1'].update(Ir1)
                                window5['1.2.2'].update(Ir2)
                                window5['1.2.3'].update(Ir3)
                                window5['1.2.4'].update(Ir4)
                                window5['1.2.5'].update(Ir5)
                                window5['1.3.1'].update(Wr1)
                                window5['1.3.2'].update(Wr2)
                                window5['1.3.3'].update(Wr3)
                                window5['1.3.4'].update(Wr4)
                                window5['1.3.5'].update(Wr5)                                
                        if event5 == 'Exit' or event5 == sg.WIN_CLOSED:
                                window5.close()                                                           
                                window.UnHide()                                
                                break
        if event == (2.2):                
                window.hide()
                layout22 = [
                        [sg.Text("Qual é a Voltagem?:                " ),sg.Input(              key=1.1                  )],
                        [sg.Text("Qual é o primeiro resistor?:       " ),sg.Input(              key=1.2                  )],
                        [sg.Text("Qual é o segundo resistor?:       "  ),sg.Input(              key=1.3                  )],
                        [sg.Text('A resistencia equivalente é:  '      ),sg.Text(size=(5,1),    key='2.1.1'), sg.Text('Ω')],
                        [sg.Text('Tensão total:                      ' ),sg.Text(size=(5,1),    key='2.1.2'), sg.Text('A')],
                        [sg.Text('corrente inteira:                  ' ),sg.Text(size=(5,1),    key='2.1.3'), sg.Text('W')],
                        [sg.Text('Tensão do resistor 1:           '    ),sg.Text(size=(5,1 ),   key='2.2.1'), sg.Text('V')],
                        [sg.Text('Tensão do resistor 2:           '    ),sg.Text(size=(5,1 ),   key='2.2.2'), sg.Text('V')],
                        [sg.Text('Potencia 1:                         '),sg.Text(size=(5,1),    key='2.3.1'), sg.Text('W')],
                        [sg.Text('Potencia 2:                         '),sg.Text(size=(5,1),    key='2.3.2'), sg.Text('W')],                        
                        [sg.Button('calcular'                          ),sg.Button('Exit'                                )]]
                window22 = sg.Window("2 resistores em serie", layout22,size=(700,700))        
                while True:
                        event22, values22 = window22.read()
                        if event22 == 'calcular':                                
                                v = int(values22[1.1])
                                a = int(values22[1.2])                                
                                b = int(values22[1.3])                                
                                req = b + a
                                Vreq = v / req
                                ReqT = v *Vreq
                                Ir1 = a*Vreq
                                Ir2 = b*Vreq
                                Wr1 = Ir1*Vreq
                                Wr2 = Ir2*Vreq                                                             
                                window22['2.1.1'].update(req)
                                window22['2.1.2'].update(Vreq)
                                window22['2.1.3'].update(ReqT)
                                window22['2.2.1'].update(Ir1)
                                window22['2.2.2'].update(Ir2)
                                window22['2.3.1'].update(Wr1)
                                window22['2.3.2'].update(Wr2)                                
                        if event22 == 'Exit' or event22 == sg.WIN_CLOSED:
                                window22.close()                                                           
                                window.UnHide()                                
                                break                                  
        if event == (2.3):                
                window.hide()
                layout23 = [
                        [sg.Text("Qual é a Voltagem?:          "       ),sg.Input               (key=1.1                  )],
                        [sg.Text("Qual é o primeiro resistor?: "       ),sg.Input               (key=1.2                  )],
                        [sg.Text("Qual é o segundo resistor?:"         ),sg.Input               (key=1.3                  )],
                        [sg.Text("Qual é o terceiro resistor?: "       ),sg.Input               (key=1.4                  )],
                        [sg.Text('a resistencia equivalente é:'        ),sg.Text(size=(5,1),     key='2.1.1'), sg.Text('Ω')],
                        [sg.Text('Tensão total:                    '   ),sg.Text(size=(5,1),     key='2.1.2'), sg.Text('A')],
                        [sg.Text('corrente inteira:                '   ),sg.Text(size=(5,1),     key='2.1.3'), sg.Text('W')],
                        [sg.Text('Tensão do resistor 1:         '      ),sg.Text(size=(5,1),     key='2.2.1'), sg.Text('V')],
                        [sg.Text('Tensão do resistor 2:         '      ),sg.Text(size=(5,1),     key='2.2.2'), sg.Text('V')],
                        [sg.Text('Tensão do resistor 3:         '      ),sg.Text(size=(5,1),     key='2.2.3'), sg.Text('V')],
                        [sg.Text('Potencia 1:                       '  ),sg.Text(size=(5,1),     key='2.3.1'), sg.Text('W')],
                        [sg.Text('Potencia 2:                       '  ),sg.Text(size=(5,1),     key='2.3.2'), sg.Text('W')],
                        [sg.Text('Potencia 3:                       '  ),sg.Text(size=(5,1),     key='2.3.3'), sg.Text('W')],                        
                        [sg.Button('calcular'                          ),sg.Button('Exit'                                 )]]
                window23 = sg.Window("3 resistores em serie", layout23,size=(700,700))        
                while True:
                        event23, values23 = window23.read()
                        if event23 == 'calcular':                               
                                v = int(values23[1.1])
                                a = int(values23[1.2])                                
                                b = int(values23[1.3])
                                c = int(values23[1.4])
                                req = a + b + c
                                Vreq = v / req
                                ReqT = v * Vreq
                                Ir1 = a * Vreq
                                Ir2 = b * Vreq
                                Ir3 = c * Vreq
                                Wr1 = Ir1 * Vreq
                                Wr2 = Ir2 * Vreq
                                Wr3 = Ir3 * Vreq                                
                                window23['2.1.1'].update(req)
                                window23['2.1.2'].update(Vreq)
                                window23['2.1.3'].update(ReqT)
                                window23['2.2.1'].update(Ir1)
                                window23['2.2.2'].update(Ir2)
                                window23['2.2.3'].update(Ir3)
                                window23['2.3.1'].update(Wr1)
                                window23['2.3.2'].update(Wr2)
                                window23['2.3.3'].update(Wr3)                                
                        if event23 == 'Exit' or event23 == sg.WIN_CLOSED:
                                window23.close()                                                           
                                window.UnHide()                                
                                break                                          
        if event == (2.4):                
                window.hide()
                layout24 = [
                        [sg.Text("Qual é a Voltagem?:          "       ),sg.Input               (key=1.1                  )],
                        [sg.Text("Qual é o primeiro resistor?: "       ),sg.Input               (key=1.2                  )],
                        [sg.Text("Qual é o segundo resistor?:"         ),sg.Input               (key=1.3                  )],
                        [sg.Text("Qual é o terceiro resistor?: "       ),sg.Input               (key=1.4                  )],
                        [sg.Text("Qual é o quatro resistor?:   "       ),sg.Input               (key=1.5                  )],
                        [sg.Text('a resistencia equivalente é:'        ),sg.Text(size=(5,1),     key='2.1.1'), sg.Text('Ω')],
                        [sg.Text('Tensão total:                    '   ),sg.Text(size=(5,1),     key='2.1.2'), sg.Text('A')],
                        [sg.Text('corrente inteira:                '   ),sg.Text(size=(5,1),     key='2.1.3'), sg.Text('W')],
                        [sg.Text('Tensão do resistor 1:         '      ),sg.Text(size=(5,1),     key='2.2.1'), sg.Text('V')],
                        [sg.Text('Tensão do resistor 2:         '      ),sg.Text(size=(5,1),     key='2.2.2'), sg.Text('V')],
                        [sg.Text('Tensão do resistor 3:         '      ),sg.Text(size=(5,1),     key='2.2.3'), sg.Text('V')],
                        [sg.Text('Tensão do resistor 4:         '      ),sg.Text(size=(5,1),     key='2.2.4'), sg.Text('V')],
                        [sg.Text('Potencia 1:                       '  ),sg.Text(size=(5,1),     key='2.3.1'), sg.Text('W')],
                        [sg.Text('Potencia 2:                       '  ),sg.Text(size=(5,1),     key='2.3.2'), sg.Text('W')],
                        [sg.Text('Potencia 3:                       '  ),sg.Text(size=(5,1),     key='2.3.3'), sg.Text('W')],
                        [sg.Text('Potencia 4:                       '  ),sg.Text(size=(5,1),     key='2.3.4'), sg.Text('W')],                     
                        [sg.Button('calcular'                          ),sg.Button('Exit'                                 )]]
                window24 = sg.Window("4 resistores em serie", layout24,size=(700,700))        
                while True:
                        event24, values24 = window24.read()
                        if event24 == 'calcular':                                
                                v = int(values24[1.1])
                                a = int(values24[1.2])                                
                                b = int(values24[1.3])
                                c = int(values24[1.4])
                                d = int(values24[1.5])
                                req = a + b + c + d
                                Vreq = v / req
                                ReqT = v * Vreq 
                                Ir1 = a * Vreq
                                Ir2 = b * Vreq
                                Ir3 = c * Vreq
                                Ir4 = d * Vreq
                                Wr1 = Ir1 * Vreq
                                Wr2 = Ir2 * Vreq
                                Wr3 = Ir3 * Vreq
                                Wr4 = Ir4 * Vreq                                                              
                                window24['2.1.1'].update(req)
                                window24['2.1.2'].update(Vreq)
                                window24['2.1.3'].update(ReqT)
                                window24['2.2.1'].update(Ir1)
                                window24['2.2.2'].update(Ir2)
                                window24['2.2.3'].update(Ir3)
                                window24['2.2.4'].update(Ir4)
                                window24['2.3.1'].update(Wr1)
                                window24['2.3.2'].update(Wr2)
                                window24['2.3.3'].update(Wr3)
                                window24['2.3.4'].update(Wr4)                                
                        if event24 == 'Exit' or event24 == sg.WIN_CLOSED:
                                window24.close()                                                           
                                window.UnHide()                                
                                break                                
        if event == (2.5):                
                window.hide()
                layout25 = [
                        [sg.Text("Qual é a Voltagem?:          "        ),sg.Input              (key=1.1                  )],
                        [sg.Text("Qual é o primeiro resistor?: "        ),sg.Input              (key=1.2                  )],
                        [sg.Text("Qual é o segundo resistor?:"          ),sg.Input              (key=1.3                  )],
                        [sg.Text("Qual é o terceiro resistor?: "        ),sg.Input              (key=1.4                  )],
                        [sg.Text("Qual é o quatro resistor?:   "        ),sg.Input              (key=1.5                  )],
                        [sg.Text("Qual é o quinto resistor?:   "        ),sg.Input              (key=1.6                  )],
                        [sg.Text('a resistencia equivalente é:'         ),sg.Text(size=(5,1),    key='2.1.1'), sg.Text('Ω')],
                        [sg.Text('Tensão total:                    '    ),sg.Text(size=(5,1),    key='2.1.2'), sg.Text('A')],
                        [sg.Text('corrente inteira:                '    ),sg.Text(size=(5,1),    key='2.1.3'), sg.Text('W')],
                        [sg.Text('Tensão do resistor 1:         '       ),sg.Text(size=(5,1),    key='2.2.1'), sg.Text('V')],
                        [sg.Text('Tensão do resistor 2:         '       ),sg.Text(size=(5,1),    key='2.2.2'), sg.Text('V')],
                        [sg.Text('Tensão do resistor 3:         '       ),sg.Text(size=(5,1),    key='2.2.3'), sg.Text('V')],
                        [sg.Text('Tensão do resistor 4:         '       ),sg.Text(size=(5,1),    key='2.2.4'), sg.Text('V')],
                        [sg.Text('Tensão do resistor 5:         '       ),sg.Text(size=(5,1),    key='2.2.5'), sg.Text('V')],
                        [sg.Text('Potencia 1:                       '   ),sg.Text(size=(5,1),    key='2.3.1'), sg.Text('W')],
                        [sg.Text('Potencia 2:                       '   ),sg.Text(size=(5,1),    key='2.3.2'), sg.Text('W')],
                        [sg.Text('Potencia 3:                       '   ),sg.Text(size=(5,1),    key='2.3.3'), sg.Text('W')],
                        [sg.Text('Potencia 4:                       '   ),sg.Text(size=(5,1),    key='2.3.4'), sg.Text('W')],
                        [sg.Text('Potencia 5:                       '   ),sg.Text(size=(5,1),    key='2.3.5'), sg.Text('W')],                     
                        [sg.Button('calcular'                           ),sg.Button('Exit'                                )]]
                window25 = sg.Window("5 resistores em serie", layout25,size=(700,700))        
                while True:
                        event25, values25 = window25.read()
                        if event25 == 'calcular':
                                v = int(values25[1.1])
                                a = int(values25[1.2])      
                                b = int(values25[1.3])
                                c = int(values25[1.4])
                                d = int(values25[1.5])
                                e = int(values25[1.6])
                                req = a + b + c + d + e
                                Vreq = v / req
                                ReqT = v * Vreq
                                Ir1 = a * Vreq
                                Ir2 = b * Vreq
                                Ir3 = c * Vreq
                                Ir4 = d * Vreq
                                Ir5 = e * Vreq
                                Wr1 = Ir1 * Vreq
                                Wr2 = Ir2 * Vreq
                                Wr3 = Ir3 * Vreq
                                Wr4 = Ir4 * Vreq
                                Wr5 = Ir5 * Vreq                                                               
                                window25['2.1.1'].update(req)
                                window25['2.1.2'].update(Vreq)
                                window25['2.1.3'].update(ReqT)
                                window25['2.2.1'].update(Ir1)
                                window25['2.2.2'].update(Ir2)
                                window25['2.2.3'].update(Ir3)
                                window25['2.2.4'].update(Ir4)
                                window25['2.2.5'].update(Ir5)
                                window25['2.3.1'].update(Wr1)
                                window25['2.3.2'].update(Wr2)
                                window25['2.3.3'].update(Wr3)
                                window25['2.3.4'].update(Wr4)
                                window25['2.3.5'].update(Wr5)                                
                        if event25 == 'Exit' or event25 == sg.WIN_CLOSED:
                                window25.close()                                                           
                                window.UnHide()                                
                                break