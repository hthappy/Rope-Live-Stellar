# #!/usr/bin/env python3

import time
import torch
import os
import logging
import sys

import rope.GUI as GUI
import rope.VideoManager as VM
import rope.Models as Models
from rope.Dicts import DEFAULT_DATA

resize_delay = 1
mem_delay = 1

def quit_app():
    vm.terminate_audio_process_tree()
    gui.destroy()

# @profile
def coordinator():
    global gui, vm, action, frame, r_frame, load_notice, resize_delay, mem_delay

    if gui.get_action_length() > 0:
        action.append(gui.get_action())

    if vm.get_action_length() > 0:
        action.append(vm.get_action())

    if vm.get_frame_length() > 0:
        frame.append(vm.get_frame())

    if len(frame) > 0:
        gui.set_image(frame[0], False)
        frame.pop(0)

    if vm.get_requested_frame_length() > 0:
        r_frame.append(vm.get_requested_frame())

    if len(r_frame) > 0:
        gui.set_image(r_frame[0], True)
        r_frame=[]

    if len(action) > 0:
        # print('Action:', action[0][0])
        # print('Value:', action[0][1])
        if action[0][0] == "load_target_video":
            vm.load_target_video(action[0][1])
            action.pop(0)

        elif action[0][0] == "load_target_image":
            vm.load_target_image(action[0][1])
            action.pop(0)

        elif action[0][0] == "play_video":
            vm.play_video(action[0][1])
            action.pop(0)

        elif action[0][0] == "get_requested_video_frame":
            vm.get_requested_video_frame(action[0][1], marker=True)
            action.pop(0)

        elif action[0][0] == "get_requested_video_frame_without_markers":
            vm.get_requested_video_frame(action[0][1], marker=False)
            action.pop(0)

        elif action[0][0] == "enable_virtualcam":
            vm.enable_virtualcam()
            action.pop(0)

        elif action[0][0] == "disable_virtualcam":
            vm.disable_virtualcam()
            action.pop(0)

        elif action[0][0] == "change_webcam_resolution_and_fps":
            vm.change_webcam_resolution_and_fps()
            action.pop(0)

        elif action[0][0] == "target_faces":
            vm.assign_found_faces(action[0][1])
            action.pop(0)

        elif action [0][0] == "saved_video_path":
            vm.saved_video_path = action[0][1]
            action.pop(0)

        elif action [0][0] == "vid_qual":
            vm.vid_qual = int(action[0][1])
            action.pop(0)

        elif action [0][0] == "set_stop":
            vm.stop_marker = action[0][1]
            action.pop(0)

        elif action [0][0] == "perf_test":
            vm.perf_test = action[0][1]
            action.pop(0)

        elif action [0][0] == 'ui_vars':
            vm.ui_data = action[0][1]
            action.pop(0)

        elif action [0][0] == 'control':
            vm.control = action[0][1]
            action.pop(0)

        elif action [0][0] == "parameters":
            vm.parameters = action[0][1]
            action.pop(0)

        # Face Editor
        elif action [0][0] == "parameters_face_editor":
            vm.parameters_face_editor = action[0][1]
            action.pop(0)

        elif action [0][0] == "markers":
            vm.markers = action[0][1]
            action.pop(0)

        elif action[0][0] == "function":
            eval(action[0][1])
            action.pop(0)

        elif action [0][0] == "clear_mem":
            vm.clear_mem()
            action.pop(0)

        # From VM
        elif action[0][0] == "stop_play":
            gui.set_player_buttons_to_inactive()
            action.pop(0)

        elif action[0][0] == "set_virtual_cam_toggle_disable":
            gui.set_virtual_cam_toggle_disable()
            action.pop(0)

        elif action[0][0] == "disable_record_button":
            gui.disable_record_button()
            action.pop(0)

        elif action[0][0] == "clear_faces_stop_swap":
            gui.clear_faces()
            gui.toggle_swapper(0)
            action.pop(0)

        elif action[0][0] == "clear_stop_enhance":
            gui.toggle_enhancer(0)
            action.pop(0)

        elif action[0][0] == "clear_stop_faces_editor":
            gui.toggle_faces_editor(0)
            action.pop(0)

        elif action[0][0] == "set_slider_length":
            gui.set_video_slider_length(action[0][1])
            action.pop(0)

        elif action[0][0] == "set_slider_fps":
            gui.set_video_slider_fps(action[0][1])
            action.pop(0)

        elif action[0][0] == "update_markers_canvas":
            gui.update_markers_canvas()
            action.pop(0)

        # Face Landmarks
        elif action[0][0] == "face_landmarks":
            vm.face_landmarks = action[0][1]
            action.pop(0)

        # Face Editor
        elif action[0][0] == "face_editor":
            vm.face_editor = action[0][1]
            action.pop(0)

        else:
            print("Action not found: "+action[0][0]+" "+str(action[0][1]))
            action.pop(0)

    if resize_delay > 100:
        gui.check_for_video_resize()
        resize_delay = 0
    else:
        resize_delay +=1

    if mem_delay > 1000:
        gui.update_vram_indicator()
        mem_delay = 0
    else:
        mem_delay +=1

    vm.process()
    gui.after(1, coordinator)
    # print(time.time() - start)

def run():
    global gui, vm, action, frame, r_frame, resize_delay, mem_delay

    try:
        # 设置设备
        device = "cuda" if torch.cuda.is_available() else "cpu"
        if device == "cuda":
            DEFAULT_DATA['ProvidersPriorityTextSelMode'] = 'CUDA'
            DEFAULT_DATA['ProvidersPriorityTextSelModes'] = ['CUDA', 'TensorRT', 'TensorRT-Engine', 'CPU']
        else:
            DEFAULT_DATA['ProvidersPriorityTextSelMode'] = 'CPU'
            DEFAULT_DATA['ProvidersPriorityTextSelModes'] = ['CPU']

        # 获取媒体路径
        media_path = os.path.join(os.path.dirname(__file__), 'media')
        logging.debug(f"Media path: {media_path}")
        
        if not os.path.exists(media_path):
            raise FileNotFoundError(f"Media directory not found: {media_path}")

        # 初始化模型
        logging.debug("Initializing Models...")
        models = Models.Models(device=device)

        # 初始化 GUI，传入媒体路径
        logging.debug("Initializing GUI...")
        gui = GUI.GUI(models, media_path)  # 传入媒体路径
        vm = VM.VideoManager(models)

        # 初始化其他变量
        action = []
        frame = []
        r_frame = []

        # 初始化 GUI
        logging.debug("Initializing GUI interface...")
        gui.initialize_gui()

        # 设置关闭窗口的处理
        gui.protocol("WM_DELETE_WINDOW", lambda: quit_app())

        # 启动协调器
        logging.debug("Starting coordinator...")
        coordinator()

        # 启动主循环
        logging.debug("Entering mainloop...")
        gui.mainloop()

    except FileNotFoundError as e:
        logging.error(f"Resource error: {e}")
        print(f"错误：{str(e)}")
        print("\n请确保以下目录存在：")
        print(f"- {media_path}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Error in run: {e}")
        raise
