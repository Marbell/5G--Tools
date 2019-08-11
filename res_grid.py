# -*- coding: UTF-8 -*-

import sys,os
import math

import win32api

import wx
import wx.grid


class res_window(wx.Frame):

    def __init__(self,parent,input_para):

        rect_parent = parent.GetRect()
        print rect_parent
        pos_target = rect_parent.GetTopRight()
        wx.Frame.__init__(self,parent,-1,"Resource Grid",pos=pos_target,size=(1000, 700))
        panel = wx.Panel(self,-1)

        sizer_grid = wx.GridBagSizer(0,0)
        usr_style = wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL
        grid = wx.grid.Grid(self,-1)
        grid.CreateGrid(12*2,14)
        cell_width =20

        grid.DisableDragColSize()
        grid.DisableDragGridSize()
        grid.DisableDragRowSize()
        grid.SetRowLabelAlignment(wx.CENTER,wx.CENTER)

        clo_num = grid.GetNumberCols()
        row_num = grid.GetNumberRows()

        for i in range(0,row_num):
            grid.SetRowLabelValue(i,str(row_num-i-1))
            grid.AutoSizeRowLabelSize(i)
        grid.SetRowLabelSize(cell_width)
        grid.SetDefaultRowSize(cell_width)
        for j in range(0,clo_num):
            grid.SetColLabelValue(j,str(j))
            grid.AutoSizeColLabelSize(j)
        grid.SetRowLabelSize(cell_width)
        grid.SetDefaultColSize(cell_width)
        grid.SetDefaultCellBackgroundColour(wx.Colour(192,192,192))

        #pdcch
        for i in range(0,row_num):
            for j in range(0,clo_num):
                grid.SetReadOnly(i,j)
                if(j<input_para['pdcch_symbol']):
                    grid.SetCellBackgroundColour(i,j,wx.GREEN)
                    if((int(grid.GetRowLabelValue(i)) - 1 )%4 == 0):
                        grid.SetCellBackgroundColour(i,j,wx.Colour(66,66,111))
        #pdsch
        for i in range(0,row_num):
            for j in range(input_para['start_symbol'],clo_num):
                if(j-input_para['start_symbol'] < input_para['symbol_length']):
                    grid.SetCellBackgroundColour(i,j,wx.Colour(255,255,255))
        #pdsch dmrs
        for j in range(0,len(input_para['dmrs_pos_list'])):
            for i in range(0,row_num):
                if input_para['dmrs_length'] == 0 and j == 0:
                    grid.SetCellBackgroundColour(i,input_para['dmrs_pos_list'][j],wx.Colour(153,204,50))
                    continue
                if input_para['dmrs_length'] == 1 and (j == 1 or j== 0):
                    grid.SetCellBackgroundColour(i,input_para['dmrs_pos_list'][j],wx.Colour(153,204,50))
                    continue
                else:
                    grid.SetCellBackgroundColour(i,input_para['dmrs_pos_list'][j],wx.Colour(234,234,173))


        sizer_grid.Add(grid,pos=(0,0),span=(5,5),flag=wx.EXPAND|usr_style)

        lbl_pdcch = wx.StaticText(self,-1,u'  PDCCH  ',style = usr_style)
        lbl_pdcch.SetBackgroundColour(wx.GREEN)
        sizer_grid.Add(lbl_pdcch,pos=(7,0),span=(1,1),flag=wx.EXPAND|usr_style)

        lbl_pdcch_dmrs = wx.StaticText(self,-1,u'  PDCCH DMRS  ',style = usr_style,)
        lbl_pdcch_dmrs.SetBackgroundColour(wx.Colour(66,66,111))
        lbl_pdcch_dmrs.SetForegroundColour(wx.Colour(255,255,255))
        sizer_grid.Add(lbl_pdcch_dmrs,pos=(7,1),span=(1,1),flag=wx.EXPAND|usr_style,)

        lbl_pdsch = wx.StaticText(self,-1,u'  PDXCH  ',style = usr_style)
        lbl_pdsch.SetBackgroundColour(wx.Colour(255,255,255))
        lbl_pdsch.SetForegroundColour(wx.Colour(0,0,0))
        sizer_grid.Add(lbl_pdsch,pos=(7,2),span=(1,1),flag=wx.EXPAND|usr_style)

        lbl_fl_dmrs = wx.StaticText(self,-1,u'Front Loaded DMRS',style = usr_style)
        lbl_fl_dmrs.SetBackgroundColour(wx.Colour(153,204,50))
        lbl_fl_dmrs.SetForegroundColour(wx.Colour(255,255,255))
        sizer_grid.Add(lbl_fl_dmrs,pos=(8,0),span=(1,1),flag=wx.EXPAND|usr_style)

        lbl_add_dmrs = wx.StaticText(self,-1,u'Add DMRS',style = usr_style)
        lbl_add_dmrs.SetBackgroundColour(wx.Colour(234,234,173))
        lbl_add_dmrs.SetForegroundColour(wx.Colour(0,0,0))
        sizer_grid.Add(lbl_add_dmrs,pos=(8,1),span=(1,1),flag=wx.EXPAND|usr_style)

        b_close = wx.Button(self,-1,"Close")
        self.Bind(wx.EVT_BUTTON,self.close_window,b_close)
        sizer_grid.Add(b_close,pos=(10,0),span=(2,5),flag=wx.EXPAND|usr_style)
        self.equal = b_close

        self.SetSizer(sizer_grid)
        sizer_grid.Fit(self)

        self.Show()

    def close_window(self,event):
        self.Close(True)


