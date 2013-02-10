#!/usr/bin/env python

import gtk, webkit

win = gtk.Window()
win.connect('destroy', lambda w: gtk.main_quit())

win.fullscreen()

scroller = gtk.scrolledWindow()
web = webkit.WebView()

web.open("http://www.ikalin.com")

win.add(scroller)
scroller.add(web)

win.show.all()
gtk.main()
