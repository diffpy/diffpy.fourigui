import h5py
import pytest

from diffpy.fourigui.fourigui import Gui


@pytest.fixture
def gui():
    # set up gui
    return Gui()


@pytest.fixture
def dummydata():
    # set up dummy data
    return h5py.File("tests/testdata/dummydata.h5")["data"]


def test_init(gui):
    assert not gui.loaded
    assert not gui.transformed
    assert not gui.cutted
    assert not gui.transcutted
    assert not gui.cutoff.get()
    assert not gui.space.get()


def test_load_cube_nothing_loaded(gui):
    # given
    gui.filename_entry.delete(0, "end")
    gui.filename_entry.insert(0, "tests/testdata/dummydata.h5")

    # when
    gui.load_cube()

    # then
    assert gui.loaded


def test_load_cube_something_loaded(gui):
    # given
    gui.loaded
    gui.filename_entry.delete(0, "end")
    gui.filename_entry.insert(0, "tests/testdata/dummydata.h5")

    # when
    gui.load_cube()

    # then
    assert gui.loaded


def test_fft_000(gui):
    # given
    gui.cube = dummydata
    gui.plot_plane = lambda *a, **b: ()  # overwrite plot_plane which requires not initialized attribute im
    gui.transformed = False
    gui.transcutted = False
    gui.cutoff.set(0)

    # when
    gui.fft()

    # then
    assert gui.transformed and not gui.transcutted


def test_fft_010(gui):
    # given
    gui.cube = dummydata
    gui.plot_plane = lambda *a, **b: ()  # overwrite plot_plane which requires not initialized attribute im
    gui.transformed = False
    gui.transcutted = False
    gui.cutoff.set(1)

    # when
    gui.fft()

    # then
    assert not gui.transformed and gui.transcutted
    # assert gui.cutted)


def test_fft_001(gui):
    # given
    gui.cube = dummydata
    gui.cube_reci = dummydata
    gui.plot_plane = lambda *a, **b: ()  # overwrite plot_plane which requires not initialized attribute im
    gui.transformed = False
    gui.transcutted = True
    gui.cutoff.set(0)

    # when
    gui.fft()

    # then
    assert gui.transformed and gui.transcutted


def test_fft_011(gui):
    # given
    gui.cube = dummydata
    gui.cube_realcut = dummydata
    gui.plot_plane = lambda *a, **b: ()  # overwrite plot_plane which requires not initialized attribute im
    gui.transformed = False
    gui.transcutted = True
    gui.cutoff.set(1)

    # when
    gui.fft()

    # then
    assert not gui.transformed and gui.transcutted


def test_fft_101(gui):
    # given
    gui.cube = dummydata
    gui.cube_real = dummydata
    gui.plot_plane = lambda *a, **b: ()  # overwrite plot_plane which requires not initialized attribute im
    gui.transformed = True
    gui.transcutted = True
    gui.cutoff.set(0)

    # when
    gui.fft()

    # then
    assert gui.transformed and gui.transcutted


def test_fft_111(gui):
    # given
    gui.cube = dummydata
    gui.cube_realcut = dummydata
    gui.plot_plane = lambda *a, **b: ()  # overwrite plot_plane which requires not initialized attribute im
    gui.transformed = True
    gui.transcutted = True
    gui.cutoff.set(1)

    # when
    gui.fft()

    # then
    assert gui.transformed and gui.transcutted
