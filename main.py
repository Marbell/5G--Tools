# -*- coding: UTF-8 -*-

import sys,os
import math

import win32api

import wx
import wx.grid

import protocol
import res_grid

APP_TITLE = u'5G Tools'
APP_ICON = 'res/5g.ico'

#wx.SetDefaultPyEncoding('utf8')


class MainFrame(wx.Frame):
    def __init__(self):

        wx.Frame.__init__(self,None,-1,APP_TITLE,style=wx.DEFAULT_FRAME_STYLE^wx.RESIZE_BORDER)
        self.SetBackgroundColour(wx.Colour(244,244,244))
        self.SetSize((800,1000))
        self.Center()

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "windows_exe":
            exe_name = win32api.GetModuleFileName(win32api.GetModuleHandle(None))
            icon = wx.Icon(exe_name,wx.BITMAP_TYPE_ICO)
        else:
            icon = wx.Icon(APP_ICON,wx.BITMAP_TYPE_ICO)

        self.SetIcon(icon)

        sizer_main = wx.GridBagSizer(0,0)
        usr_style = wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL

        text_location_and_bandwith = wx.StaticText(self,-1,u'LocationAndBandwith:',style=usr_style)
        sizer_main.Add(text_location_and_bandwith, pos=(0,0), span=(1,1), flag=usr_style)

        self.display_lab = wx.ComboBox(self,-1)
        sizer_main.Add(self.display_lab, pos=(0,1), span=(1,1), flag=usr_style)

        text_start_prb_index = wx.StaticText(self,-1,u'Start PRB Index:',style=usr_style)
        sizer_main.Add(text_start_prb_index, pos=(1,0), span=(1,1), flag=usr_style)

        self.start_prb_value = wx.TextCtrl(self,-1,u'',style=wx.TE_READONLY)
        sizer_main.Add(self.start_prb_value, pos=(1, 1), span=(1, 1), flag=usr_style)

        text_prb_length = wx.StaticText(self,-1,u'BandWith Length:',style=usr_style)
        sizer_main.Add(text_prb_length, pos=(2,0), span=(1,1), flag=usr_style)

        self.prb_length_value = wx.TextCtrl(self,-1,u'',style=wx.TE_READONLY)
        sizer_main.Add(self.prb_length_value, pos=(2, 1), span=(1, 1), flag=usr_style)

        b_cal_lab = wx.Button(self,-1,"Calculate BWP")
        self.Bind(wx.EVT_BUTTON,self.onbutton,b_cal_lab)
        sizer_main.Add(b_cal_lab, pos=(3, 0), span=(1, 1), flag=usr_style)
        self.equal = b_cal_lab

        b_del_lab = wx.Button(self,-1,"Clear BWP")
        self.Bind(wx.EVT_BUTTON,self.onbutton,b_del_lab)
        sizer_main.Add(b_del_lab, pos=(3, 1), span=(1, 1), flag=usr_style)
        self.equal = b_del_lab

        static_alloc_type_text = wx.StaticText(self,label='Alloc Type A or Type B')
        list_alloc_type = ['Type A','Type B']
        self.choice_alloc_type = wx.Choice(self,-1,choices = list_alloc_type)
        self.choice_alloc_type.SetSelection(0)
        sizer_main.Add(static_alloc_type_text, pos=(4, 0), span=(1, 1), flag=usr_style)
        sizer_main.Add(self.choice_alloc_type, pos=(4, 1), span=(1, 1), flag=usr_style)

        text_sliv = wx.StaticText(self,-1,u'SLIV:',style=usr_style)
        sizer_main.Add(text_sliv, pos=(5,0), span=(1,1), flag=usr_style)

        self.display_sliv = wx.ComboBox(self,-1)
        sizer_main.Add(self.display_sliv, pos=(5,1), span=(1,1), flag=usr_style)

        text_start_symbol_index = wx.StaticText(self,-1,u'Start Symbol Index:',style=usr_style)
        sizer_main.Add(text_start_symbol_index, pos=(6,0), span=(1,1), flag=usr_style)

        self.start_symbol_value = wx.TextCtrl(self,-1,u'',style=wx.TE_READONLY)
        sizer_main.Add(self.start_symbol_value, pos=(6, 1), span=(1, 1), flag=usr_style)

        text_symbol_length = wx.StaticText(self,-1,u'Symbol Length:',style=usr_style)
        sizer_main.Add(text_symbol_length, pos=(7,0), span=(1,1), flag=usr_style)

        self.symbol_length_value = wx.TextCtrl(self,-1,u'',style=wx.TE_READONLY)
        sizer_main.Add(self.symbol_length_value, pos=(7, 1), span=(1, 1), flag=usr_style)

        b_cal_sliv = wx.Button(self,-1,"Calculate SLIV")
        self.Bind(wx.EVT_BUTTON,self.onbutton,b_cal_sliv)
        sizer_main.Add(b_cal_sliv, pos=(8, 0), span=(1, 1), flag=usr_style)
        self.equal = b_cal_sliv

        b_del_siiv = wx.Button(self,-1,"Clear SLIV")
        self.Bind(wx.EVT_BUTTON,self.onbutton,b_del_siiv)
        sizer_main.Add(b_del_siiv, pos=(8, 1), span=(1, 1), flag=usr_style)
        self.equal = b_del_siiv

        static_pxsch_text = wx.StaticText(self,label='PDSCH or PUSCH')
        list_pxsch = ['PDSCH','PUSCH']
        self.choice_pxsch = wx.Choice(self,-1,choices = list_pxsch)
        self.choice_pxsch.SetSelection(0)
        sizer_main.Add(static_pxsch_text, pos=(9, 0), span=(1, 1), flag=usr_style)
        sizer_main.Add(self.choice_pxsch, pos=(9, 1), span=(1, 1), flag=usr_style)

        static_dmrs_typeA_pos_text = wx.StaticText(self,label='DMRS TypeA Pos')
        list_dmrs_typeA_pos = ['','pos2','pos3']
        self.choice_dmrs_typeA_pos = wx.Choice(self,-1,choices = list_dmrs_typeA_pos)
        self.choice_dmrs_typeA_pos.SetSelection(0)
        sizer_main.Add(static_dmrs_typeA_pos_text, pos=(10, 0), span=(1, 1), flag=usr_style)
        sizer_main.Add(self.choice_dmrs_typeA_pos, pos=(10, 1), span=(1, 1), flag=usr_style)

        static_dmrs_type_text = wx.StaticText(self,label='DMRS Type 1 or Type 2')
        list_dmrs_type = ['Type 1','Type 2']
        self.choice_dmrs_type = wx.Choice(self,-1,choices = list_dmrs_type)
        self.choice_dmrs_type.SetSelection(0)
        sizer_main.Add(static_dmrs_type_text, pos=(11, 0), span=(1, 1), flag=usr_style)
        sizer_main.Add(self.choice_dmrs_type, pos=(11, 1), span=(1, 1), flag=usr_style)

        static_dmrs_length_text = wx.StaticText(self,label='DMRS Length 1 or Length 2')
        list_dmrs_length = ['Length 1','Length 2']
        self.choice_dmrs_length = wx.Choice(self,-1,choices = list_dmrs_length)
        self.choice_dmrs_length.SetSelection(0)
        sizer_main.Add(static_dmrs_length_text, pos=(12, 0), span=(1, 1), flag=usr_style)
        sizer_main.Add(self.choice_dmrs_length, pos=(12, 1), span=(1, 1), flag=usr_style)

        static_add_dmrs_pos_text = wx.StaticText(self,label='Add DMRS pos')
        list_add_dmrs_pos = ['','pos1','pos2','pos3']
        self.choice_add_dmrs_pos = wx.Choice(self,-1,choices = list_add_dmrs_pos)
        self.choice_add_dmrs_pos.SetSelection(0)
        sizer_main.Add(static_add_dmrs_pos_text, pos=(13, 0), span=(1, 1), flag=usr_style)
        sizer_main.Add(self.choice_add_dmrs_pos, pos=(13, 1), span=(1, 1), flag=usr_style)

        static_pdcch_sym_text = wx.StaticText(self,label='PDCCH Symbol Number')
        list_pdcch_sym = ['','1 Symbol','2 Symbol']
        self.choice_pdcch_sym = wx.Choice(self,-1,choices = list_pdcch_sym)
        self.choice_pdcch_sym.SetSelection(0)
        sizer_main.Add(static_pdcch_sym_text, pos=(19, 0), span=(1, 1), flag=usr_style)
        sizer_main.Add(self.choice_pdcch_sym, pos=(19, 1), span=(1, 1), flag=usr_style)

        b_get_res_grid = wx.Button(self,-1,"Get Resource Grid")
        self.Bind(wx.EVT_BUTTON,self.onbutton,b_get_res_grid)
        sizer_main.Add(b_get_res_grid, pos=(20, 0), span=(1, 1), flag=usr_style)
        self.equal = b_get_res_grid

        self.SetSizer(sizer_main)
        sizer_main.Fit(self)
        self.CenterOnScreen()

    def onbutton(self,evt):
        label = evt.GetEventObject().GetLabel()
        if label == "Calculate BWP":
            try:
                lab_value = self.display_lab.GetValue()
                if not lab_value.strip():
                    return

                lab_num = int(filter(str.isdigit,lab_value.encode("utf-8")))

                list_out = ["Invalid Input","Invalid Input"]

                protocol.cal_location_and_bandwith(lab_num,list_out)

                self.display_lab.Insert(lab_value,0)

                self.start_prb_value.SetValue(str(list_out[0]))
                self.prb_length_value.SetValue(str(list_out[1]))

            except Exception,e:
                wx.LogError(str(e))
                return
        if label == "Clear BWP":
                self.display_lab.SetValue("")
                self.start_prb_value.SetValue("")
                self.prb_length_value.SetValue("")


        if label == "Calculate SLIV":
            try:
                sliv_value = self.display_sliv.GetValue()
                if not sliv_value.strip():
                    return

                sliv_num = int(filter(str.isdigit,sliv_value.encode("utf-8")))

                list_out = ["Invalid Input","Invalid Input",0]
                list_out[2] = self.choice_alloc_type.GetCurrentSelection()

                protocol.cal_sliv(sliv_num,list_out)

                if list_out[0] == "Invalid Input" or list_out[1] == "Invalid Input":
                    wx.MessageBox(u"SLIV is wrong Number or not match allocation type!", u"Info", wx.OK | wx.ICON_INFORMATION)

                self.display_sliv.Insert(sliv_value,0)

                self.start_symbol_value.SetValue(str(list_out[0]))
                self.symbol_length_value.SetValue(str(list_out[1]))

            except Exception,e:
                wx.LogError(str(e))
                return
        if label == "Clear SLIV":
                self.display_sliv.SetValue("")
                self.start_symbol_value.SetValue("")
                self.symbol_length_value.SetValue("")

        if label == "Get Resource Grid":
            input_para = {
                'pxsch':0,
                'alloc_type':0,
                'start_symbol':0,
                'symbol_length':14,
                'dmrs_type':0,
                'dmrs_typeA_pos':0,
                'dmrs_length':0,
                'add_dmrs_pos':0,
                'pdcch_symbol':1,
                'dmrs_pos_list':[],
            }
            input_para['pxsch'] = self.choice_pxsch.GetCurrentSelection()
            input_para['alloc_type'] = self.choice_alloc_type.GetCurrentSelection()
            input_para['dmrs_type'] = self.choice_dmrs_type.GetCurrentSelection()
            input_para['dmrs_length'] = self.choice_dmrs_length.GetCurrentSelection()
            input_para['add_dmrs_pos'] = self.choice_add_dmrs_pos.GetCurrentSelection()
            input_para['pdcch_symbol'] = self.choice_pdcch_sym.GetCurrentSelection()

            try:
                sliv_value = self.display_sliv.GetValue()
                if not sliv_value.strip():
                    return

                sliv_num = int(filter(str.isdigit,sliv_value.encode("utf-8")))

                list_out = ["Invalid Input","Invalid Input",0]
                list_out[2] = self.choice_alloc_type.GetCurrentSelection()

                protocol.cal_sliv(sliv_num,list_out)

                input_para['start_symbol'] = list_out[0]
                input_para['symbol_length'] = list_out[1]

                warning_index = protocol.cal_input_grid_valid(input_para)
                if(warning_index!=0):
                    wx.MessageBox(protocol.out_warning_str_list[warning_index], u"Info", wx.OK | wx.ICON_INFORMATION)
                    return

                protocol.cal_dmrs_pos(input_para)

                self.display_sliv.Insert(sliv_value,0)

                self.display_sliv.SetValue(str(sliv_num))
                self.start_symbol_value.SetValue(str(list_out[0]))
                self.symbol_length_value.SetValue(str(list_out[1]))

            except Exception,e:
                wx.LogError(str(e))
                return


            res_window1 = res_grid.res_window(self,input_para)
        else:
            self.equal.SetFocus()

        pass


class MainApp(wx.App):
    def OnInit(self):
        self.SetAppName(APP_TITLE)
        self.Frame = MainFrame()
        self.Frame.Show()
        return True


if __name__ == "__main__":
    app = MainApp(redirect=True, filename="debug.txt")
    app.MainLoop()


