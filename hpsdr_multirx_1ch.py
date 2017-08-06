#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: HPSDR MultiRX -- 1 active channel
# Author: John Ackermann N8UR
# Description: Records multiple spectrum chunks to disk
# Generated: Sun Aug  6 16:23:46 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from datetime import datetime
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import logpwrfft
from gnuradio.filter import firdes
from optparse import OptionParser
import hpsdr
import sip
import sys
import threading
import time


class hpsdr_multirx_1ch(gr.top_block, Qt.QWidget):

    def __init__(self, rx_0=10100000):
        gr.top_block.__init__(self, "HPSDR MultiRX -- 1 active channel")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("HPSDR MultiRX -- 1 active channel")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "hpsdr_multirx_1ch")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.rx_0 = rx_0

        ##################################################
        # Variables
        ##################################################
        self.probe1 = probe1 = 0
        self.working_dir = working_dir = "hf_data/"
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = probe1
        self.timestamp_iso = timestamp_iso = datetime.utcnow().isoformat()+"Z"
        self.rx_samp_rate = rx_samp_rate = 384000
        self.metadata = metadata = {"call=<call>","rx=<receiver>","ant=<antenna>"}
        self.file_stamp = file_stamp = datetime.now().strftime("%Y.%m.%d.%H.%M.%S") 
        self.fft_size = fft_size = 1024

        ##################################################
        # Blocks
        ##################################################
        self.probe0 = blocks.probe_signal_f()
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: x
        
        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel("probe0"+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_layout.addWidget(self._variable_qtgui_label_0_tool_bar)
          
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	fft_size, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	000000, #fc
        	rx_samp_rate, #bw
        	"QT GUI Plot", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 0)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["RX0", "RX1", "RX2", "Rx3", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        def _probe1_probe():
            while True:
                val = self.probe0.level()
                try:
                    self.set_probe1(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (1))
        _probe1_thread = threading.Thread(target=_probe1_probe)
        _probe1_thread.daemon = True
        _probe1_thread.start()
        self.max_value = blocks.max_ff(fft_size,1)
        self.logpwrfft_x_0 = logpwrfft.logpwrfft_c(
        	sample_rate=rx_samp_rate,
        	fft_size=fft_size,
        	ref_scale=2,
        	frame_rate=10,
        	avg_alpha=0.001,
        	average=False,
        )
        self.hpsdr_hermesNB_0 = hpsdr.hermesNB(rx_0, rx_0, rx_0, rx_0, rx_0, rx_0, rx_0, rx_0, 71000000, 0, 0, 1, 1, 0, 384000, "eno1", "0xF0", 0, 0, 0x20, 0x10, 0, 1, "*")
        self.analog_sig_source_x_1 = analog.sig_source_c(48000, analog.GR_COS_WAVE, -1000, 0.95, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_1, 0), (self.hpsdr_hermesNB_0, 0))    
        self.connect((self.hpsdr_hermesNB_0, 0), (self.logpwrfft_x_0, 0))    
        self.connect((self.hpsdr_hermesNB_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.logpwrfft_x_0, 0), (self.max_value, 0))    
        self.connect((self.max_value, 0), (self.probe0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "hpsdr_multirx_1ch")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_rx_0(self):
        return self.rx_0

    def set_rx_0(self, rx_0):
        self.rx_0 = rx_0
        self.hpsdr_hermesNB_0.set_Receive0Frequency(self.rx_0)
        self.hpsdr_hermesNB_0.set_Receive1Frequency(self.rx_0)
        self.hpsdr_hermesNB_0.set_Receive2Frequency(self.rx_0)
        self.hpsdr_hermesNB_0.set_Receive3Frequency(self.rx_0)
        self.hpsdr_hermesNB_0.set_Receive4Frequency(self.rx_0)
        self.hpsdr_hermesNB_0.set_Receive5Frequency(self.rx_0)
        self.hpsdr_hermesNB_0.set_Receive6Frequency(self.rx_0)
        self.hpsdr_hermesNB_0.set_Receive7Frequency(self.rx_0)

    def get_probe1(self):
        return self.probe1

    def set_probe1(self, probe1):
        self.probe1 = probe1
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(self.probe1))

    def get_working_dir(self):
        return self.working_dir

    def set_working_dir(self, working_dir):
        self.working_dir = working_dir

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.variable_qtgui_label_0)))

    def get_timestamp_iso(self):
        return self.timestamp_iso

    def set_timestamp_iso(self, timestamp_iso):
        self.timestamp_iso = timestamp_iso

    def get_rx_samp_rate(self):
        return self.rx_samp_rate

    def set_rx_samp_rate(self, rx_samp_rate):
        self.rx_samp_rate = rx_samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(000000, self.rx_samp_rate)
        self.logpwrfft_x_0.set_sample_rate(self.rx_samp_rate)

    def get_metadata(self):
        return self.metadata

    def set_metadata(self, metadata):
        self.metadata = metadata

    def get_file_stamp(self):
        return self.file_stamp

    def set_file_stamp(self, file_stamp):
        self.file_stamp = file_stamp

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size


def argument_parser():
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option(
        "-a", "--rx-0", dest="rx_0", type="intx", default=10100000,
        help="Set rx0 [default=%default]")
    return parser


def main(top_block_cls=hpsdr_multirx_1ch, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(rx_0=options.rx_0)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
