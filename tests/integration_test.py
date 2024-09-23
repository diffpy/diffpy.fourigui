import h5py
import numpy as np
import pytest

from diffpy.fourigui.fourigui import Gui


@pytest.fixture
def gui():
    # set up gui
    return Gui()


@pytest.fixture
def test_data():
    # set up test data
    return {
        "test_sofq": h5py.File("tests/testdata/sofq.h5")["data"],
        "test_sofq_cut_10to40px": h5py.File("tests/testdata/sofq_cut_10to40px.h5")["data"],
        "test_sofq_cut_15to35px": h5py.File("tests/testdata/sofq_cut_15to35px.h5")["data"],
        "test_gofr": h5py.File("tests/testdata/gofr.h5")["data"],
        "test_gofr_cut_10to40px": h5py.File("tests/testdata/gofr_from_sofq_cut_10to40px.h5")["data"],
        "test_gofr_cut_15to35px": h5py.File("tests/testdata/gofr_from_sofq_cut_15to35px.h5")["data"],
    }


def test_load_cube_testdataset1(gui, test_data):
    # given
    gui.filename_entry.delete(0, "end")
    gui.filename_entry.insert(0, "tests/testdata/sofq.h5")

    # when
    gui.load_cube()
    result = gui.cube

    # then
    assert np.allclose(result, test_data["test_sofq"])


def test_load_cube_testdataset2(gui, test_data):
    # given
    gui.filename_entry.delete(0, "end")
    gui.filename_entry.insert(0, "tests/testdata/sofq_cut_10to40px.h5")

    # when
    gui.load_cube()
    result = gui.cube

    # then
    assert np.allclose(np.nan_to_num(result), np.nan_to_num(test_data["test_sofq_cut_10to40px"]))


def test_load_cube_testdataset3(gui, test_data):
    # given
    gui.filename_entry.delete(0, "end")
    gui.filename_entry.insert(0, "tests/testdata/sofq_cut_15to35px.h5")

    # when
    gui.load_cube()
    result = gui.cube

    # then
    assert np.allclose(np.nan_to_num(result), np.nan_to_num(test_data["test_sofq_cut_15to35px"]))


def test_fft_testdataset1(gui, test_data):
    # given
    gui.plot_plane = lambda *a, **b: ()  # overwrite plot_plane which requires not initialized attribute im
    gui.cube = test_data["test_sofq"]

    # when
    gui.fft()
    result = gui.cube

    # then
    assert np.allclose(result, test_data["test_gofr"])


def test_fft_testdataset2(gui, test_data):
    # given
    gui.plot_plane = lambda *a, **b: ()  # overwrite plot_plane which requires not initialized attribute im
    gui.cube = test_data["test_sofq_cut_10to40px"]

    # when
    gui.fft()
    result = gui.cube

    # then
    assert np.allclose(result, test_data["test_gofr_cut_10to40px"])


def test_fft_testdataset3(gui, test_data):
    # given
    gui.plot_plane = lambda *a, **b: ()  # overwrite plot_plane which requires not initialized attribute im
    gui.cube = test_data["test_sofq_cut_15to35px"]

    # when
    gui.fft()
    result = gui.cube

    # then
    assert np.allclose(result, test_data["test_gofr_cut_15to35px"])


def test_applycutoff_range1(gui, test_data):
    # given
    gui.plot_plane = lambda *a, **b: ()
    gui.cube = test_data["test_sofq"]
    gui.qminentry.insert(0, "10")
    gui.qmaxentry.insert(0, "40")

    # when
    gui.applycutoff()
    result = gui.cube

    # then
    assert np.allclose(np.nan_to_num(result), np.nan_to_num(test_data["test_sofq_cut_10to40px"]))


def test_applycutoff_range2(gui, test_data):
    # given
    gui.plot_plane = lambda *a, **b: ()
    gui.cube = test_data["test_sofq"]
    gui.qminentry.insert(0, "15")
    gui.qmaxentry.insert(0, "35")

    # when
    gui.applycutoff()
    result = gui.cube

    # then
    assert np.allclose(np.nan_to_num(result), np.nan_to_num(test_data["test_sofq_cut_15to35px"]))
