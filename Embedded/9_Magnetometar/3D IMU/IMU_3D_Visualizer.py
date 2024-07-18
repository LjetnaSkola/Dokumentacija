import os
import sys
import vtk
import serial
import serial.tools.list_ports
from time import sleep
import socket

# Communication mode
USB = 1
COMMUNICATION = USB

# Global variables
serial_connection = None
vtk_render_window = None
vtk_actors = None
last_quat = None
board_id = 1

def get_orientation_data():
    if COMMUNICATION == USB:
        data = serial_connection.readline().decode().strip().split()
    print("Received data:", data)  # Debugging line
    return data

def information_callback(self, obj):
    rotate_data = get_orientation_data()
    # print("Rotate data:", rotate_data)  # Debugging line

    if len(rotate_data) == 4:
        global last_quat
        last_quat = vtk.vtkQuaternionf(float(rotate_data[0]), float(rotate_data[1]), float(rotate_data[2]), float(rotate_data[3]))
        # print("Quaternion:", last_quat)  # Debugging line

        t = [[0]*3 for _ in range(3)]
        last_quat.ToMatrix3x3(t)
        # print("Matrix:", t)  # Debugging line

        temp_matrix = vtk.vtkMatrix4x4()
        for i in range(3):
            for j in range(3):
                temp_matrix.SetElement(i, j, t[i][j])
        for i in range(3):
            temp_matrix.SetElement(i, 3, 0)
        temp_matrix.SetElement(3, 0, 0)
        temp_matrix.SetElement(3, 1, 0)
        temp_matrix.SetElement(3, 2, 0)
        temp_matrix.SetElement(3, 3, 1)

        vtk_actors.InitTraversal()
        vtk_next_actor = vtk_actors.GetNextActor()
        while vtk_next_actor is not None:
            vtk_next_actor.SetUserMatrix(temp_matrix)
            vtk_next_actor.SetScale(0.6, 0.6, 0.6)
            vtk_next_actor.GetProperty().LightingOff()
            vtk_next_actor = vtk_actors.GetNextActor()
        vtk_render_window.Render()
    else:
        print("Invalid data length:", len(rotate_data))  # Debugging line

def connect_usb():
    print("\n*Searching for plugged in USB ports...")
    ports = list(serial.tools.list_ports.comports())
    port_number = 0

    print("*Found COM ports:")
    for i, port in enumerate(ports):
        print(i, "\t", port)

    if not ports:
        print("*No boards were found to be plugged in - stopping debugger")
        sys.exit()
    elif len(ports) > 1:
        port_number = int(input("*Enter number from above: "))

    print("*Using board port", ports[port_number].device)
    try:
        global serial_connection
        serial_connection = serial.Serial(ports[port_number].device, 115200)
        print("*Successfully opened device port\n")
        return 1
    except Exception as e:
        print("*Could not open port:", str(e))
        sys.exit()

def init_3D_scene(board_file_name):
    data_root = os.path.dirname(__file__)
    importer = vtk.vtkGLTFImporter()
    importer.SetFileName(os.path.join(data_root, board_file_name))
    importer.Read()

    global vtk_render_window
    vtk_renderer = importer.GetRenderer()
    vtk_render_window = importer.GetRenderWindow()
    vtk_render_window_interactor = vtk.vtkRenderWindowInteractor()
    vtk_render_window_interactor.SetRenderWindow(vtk_render_window)

    vtk_renderer.GradientBackgroundOn()
    vtk_renderer.SetBackground(0.2, 0.2, 0.2)
    vtk_renderer.SetBackground2(0.3, 0.3, 0.3)
    vtk_render_window.SetSize(600, 600)
    vtk_render_window.SetWindowName('IMU 3D Visualizer')

    vtk_render_window_interactor.Initialize()
    vtk_renderer.GetActiveCamera().Zoom(1.0)
    vtk_renderer.GetActiveCamera().SetRoll(90)
    vtk_renderer.GetActiveCamera().SetClippingRange(0.01, 100)
    vtk_renderer.GetActiveCamera().SetViewAngle(40)
    vtk_renderer.SetClippingRangeExpansion(0.1)
    vtk_renderer.TwoSidedLightingOn()
    vtk_renderer.SetAmbient([1, 1, 1])
    vtk_renderer.ResetCamera()
    vtk_render_window.Render()

    vtk_render_window_interactor.CreateRepeatingTimer(1)
    vtk_render_window_interactor.AddObserver("TimerEvent", information_callback)

    global vtk_actors
    vtk_actors = vtk_renderer.GetActors()
    vtk_render_window_interactor.Start()

def main():
    if COMMUNICATION == USB:
        connect_usb()

    sleep(0.1)
    global board_id
    if board_id == "1":
        init_3D_scene("data/TinyZero.glb")
    elif board_id == "2":
        init_3D_scene("data/RobotZero.glb")
    elif board_id == "3":
        init_3D_scene("data/Wireling9Axis.glb")
    elif board_id == "4":
        init_3D_scene("data/Wireling3Axis.glb")

if __name__ == '__main__':
    main()
