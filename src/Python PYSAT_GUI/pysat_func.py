from pysat.spectral.spectral_data import spectral_data
from pysat.regression.sm import sm
import pandas as pd

# This class should be worked on and saved for the future.
# Currently we are only going to work on setting up the program
# such that the user can only do each function once, but the
# inner process is done twice.

# The below class will one day be an attempt at moving away from
# this restriction

class pysat_func(object):

    # Below are all your file setters. ======================================================

    def set_file_outpath(self, outpath):
        self.outpath = outpath

    def set_file_known_data(self, db):
        self.known_data = db

    def set_file_unknown_data(self, unknowndatacsv):
        self.unknown_data = unknowndatacsv

    def set_file_maskfile(self, maskfile):
        self.maskfile = maskfile

    # Below are all your file getters. ======================================================

    def get_file_outpath(self):
        return self.outpath

    def get_file_known_data(self):
        return self.known_data

    def get_file_unknown_data(self):
        return self.unknown_data

    def get_file_maskfile(self):
        return self.maskfile


    # These are the functions that do the necessary work ====================================
    # Note: functions double up because of known and unknown data, it is done this way because
    # I realized we want to keep things as private as possible between the two classes:
    # PYSAT_UI and PYSAT_FUNC
    # After working through everything, I realized doubling up on functions, is not the best
    # way forward. Instead we'll have to allow UI to have a little access to pysat_func.data
    # and pysat_func.unknowndata

    def set_spectral(self, data_base):
        """
        Usage:
        k_data = set_spectral(pysat_func.get_file_known_data())
        u_data = set_spectral(pysat_func.get_file_unknown_data())

        The user will choose from either database of unknowndata or knowndata
        this means usage will be either:

        :param data_base:
        :return spectra:
        """
        data = pd.read_csv(data_base, header=[0, 1])
        return spectral_data(data)

    def set_interp(self, data_1, data_2):
        """
        Usage:
        set_interp(u_data, k_data)

        Technically speaking, the values can be set up any way you want.
        The only concern in the typing. Make sure both values are of type spectral_data
        :param data_1
        :param data_1
        :return:
        """
        data_1.interp(data_2.df['wv1'].columns)

    def set_mask(self, data, maskfile):
        """
        Usage:
        set_mask(pysat_func.get_known_data(), pysat_func.get_maskfile())
        set_mask(pysat_func.get_unknown_data(), pysat_func.get_maskfile())

        :param data:
        :param maskfile:
        :return:
        """
        pass

    def get_range(self, data, ranges):
        """
        Usage:
        pysat_func.get_ranges(k_data, [(0, 1000)])
        pysat_func.get_ranges(u_data, [(0, 1000)])

        :param data:
        :param ranges:
        :return:
        """
        data.norm(ranges)

    def set_element_name(self, el):
        """

        :param el:
        :return:
        """
        pass