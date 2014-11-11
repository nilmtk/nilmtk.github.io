def code():


    # CONVERT THE REDD DATASET TO NILMTK'S HDF5 FORMAT
    from nilmtk.dataset_converters import convert_redd
    convert_redd('/data/REDD/low_freq', '/data/REDD/redd.h5')

    # IMPORT HDF5 FORMAT INTO NILMTK
    from nilmtk import DataSet
    redd = DataSet('/data/REDD/redd.h5')




