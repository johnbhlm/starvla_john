"""
mixtures.py

Defines a registry of dataset mixtures and weights for the Open-X Embodiment Datasets. Each dataset is associated with
a float "sampling weight"
"""

from typing import Dict, List, Tuple

DATASET_NAMED_MIXTURES = {

    "custom_dataset": [
        ("custom_dataset_name", 1.0, "custom_robot_config"),
    ],
    "custom_dataset_2": [
        ("custom_dataset_name_1", 1.0, "custom_robot_config"),
        ("custom_dataset_name_2", 1.0, "custom_robot_config"),
    ],

    "libero_all": [
        ("libero_object_no_noops_1.0.0_lerobot", 1.0, "libero_franka"),
        ("libero_goal_no_noops_1.0.0_lerobot", 1.0, "libero_franka"),
        ("libero_spatial_no_noops_1.0.0_lerobot", 1.0, "libero_franka"),
        ("libero_90_no_noops_lerobot", 1.0, "libero_franka"),
        ("libero_10_no_noops_1.0.0_lerobot", 1.0, "libero_franka"),
    ],
    "libero_goal": [
        ("libero_goal_no_noops_1.0.0_lerobot", 1.0, "libero_franka"),
    ],
    "libero_object": [
        ("libero_object_no_noops_1.0.0_lerobot", 1.0, "libero_franka"),
    ],
    "libero_spatial": [
        ("libero_spatial_no_noops_1.0.0_lerobot", 1.0, "libero_franka"),
    ],
    "libero_10": [
        ("libero_10_no_noops_1.0.0_lerobot", 1.0, "libero_franka"),
    ],
    "libero_90": [
        ("libero_90_no_noops_lerobot", 1.0, "libero_franka"),
        ("libero_90_no_noops_lerobot", 1.0, "libero_ur5"),
    ],

    "bridge": [
        ("bridge_orig_1.0.0_lerobot", 1.0, "oxe_bridge"),
    ],
    "bridge_rt_1": [
        ("bridge_orig_1.0.0_lerobot", 1.0, "oxe_bridge"),
        ("fractal20220817_data_0.1.0_lerobot", 1.0, "oxe_rt1"),
    ],

    "demo_sim_pick_place": [
        ("sim_pick_place", 1.0, "demo_sim_franka_delta_eef"),
    ],

    "custom_dataset": [
        ("4", 1.0, "custom_robot_config"),
    ],
    "h10w_dataset": [
        ("demo_randomized_lerobot", 1.0, "h10w_robot_config"),
    ],
    "h10w_real_dataset_wr": [
        ("Whitetable_Righthand", 1.0, "h10w_robot_config"),
    ],
    "h10w_real_dataset_wl": [
        ("Whitetable_Lefthand", 1.0, "h10w_robot_config"),
    ],
    "h10w_real_dataset_br": [
        ("BlackTable_Righthand", 1.0, "h10w_robot_config"),
    ],
    "h10w_real_dataset_bl": [
        ("BlackTable_Lefthand", 1.0, "h10w_robot_config"),
    ],
    "h10w_real_dataset_boxr": [
        ("BlackTable_Frombox", 1.0, "h10w_robot_config"),
    ],
    "h10w_real_dataset_sr": [
        ("Sofa_Righthand", 1.0, "h10w_robot_config"),
    ],
    "h10w_real_dataset_sl": [
        ("Sofa_Lefthand", 1.0, "h10w_robot_config"),
    ],
    # "h10w_real_dataset_all": [
    #     ("Merged_Robot_Dataset", 1.0, "h10w_robot_config"),
    # ],
    "h10w_real_dataset_all": [
        ("Whitetable_Righthand", 1.0, "h10w_robot_config"),
        ("Sofa_Lefthand", 1.0, "h10w_robot_config"),
        ("BlackTable_Righthand", 1.0, "h10w_robot_config"),
        ("Whitetable_Lefthand", 1.0, "h10w_robot_config"),
        ("BlackTable_Frombox", 1.0, "h10w_robot_config"),
        ("Sofa_Righthand", 1.0, "h10w_robot_config"),
        ("BlackTable_Lefthand", 1.0, "h10w_robot_config"),
        ("BlackTable_Left", 1.0, "h10w_robot_config"),
        ("BlackTable_Right", 1.0, "h10w_robot_config"),
    ],
    "h10w_real_dataset_all_left": [
        ("Whitetable_Righthand", 1.0, "h10w_robot_config"),
        ("Sofa_Lefthand", 1.0, "h10w_robot_config"),
        ("BlackTable_Righthand", 1.0, "h10w_robot_config"),
        ("Whitetable_Lefthand", 1.0, "h10w_robot_config"),
        ("BlackTable_Frombox", 1.0, "h10w_robot_config"),
        ("Sofa_Righthand", 1.0, "h10w_robot_config"),
        ("BlackTable_Lefthand", 1.0, "h10w_robot_config"),
        ("BlackTable_Left", 1.0, "h10w_robot_config"),
        ("BlackTable_Right", 1.0, "h10w_robot_config"),
    ],
    "h10w_real_dataset_vr": [
        # ("lerobot_dataset_167", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_171", 0.25, "h10w_robot_config"),
        ("lerobot_dataset_172", 0.4, "h10w_robot_config"),
        ("lerobot_dataset_174", 0.1, "h10w_robot_config"),
        ("lerobot_dataset_177", 0.25, "h10w_robot_config"),
        ("lerobot_dataset_186_r", 1.0, "h10w_robot_config"),
    ],
    "custom_dataset_2": [
        ("custom_dataset_name_1", 1.0, "custom_robot_config"),
        ("custom_dataset_name_2", 1.0, "custom_robot_config"),
    ],

    "fourier_gr1_unified_1000": [
        ("gr1_unified.PnPBottleToCabinetClose_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PnPCanToDrawerClose_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PnPCupToDrawerClose_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PnPMilkToMicrowaveClose_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PnPPotatoToMicrowaveClose_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PnPWineToCabinetClose_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PosttrainPnPNovelFromCuttingboardToBasketSplitA_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PosttrainPnPNovelFromCuttingboardToCardboardboxSplitA_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PosttrainPnPNovelFromCuttingboardToPanSplitA_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PosttrainPnPNovelFromCuttingboardToPotSplitA_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PosttrainPnPNovelFromCuttingboardToTieredbasketSplitA_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PosttrainPnPNovelFromPlacematToBasketSplitA_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PosttrainPnPNovelFromPlacematToBowlSplitA_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PosttrainPnPNovelFromPlacematToPlateSplitA_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PosttrainPnPNovelFromPlacematToTieredshelfSplitA_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PosttrainPnPNovelFromPlateToBowlSplitA_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PosttrainPnPNovelFromPlateToCardboardboxSplitA_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PosttrainPnPNovelFromPlateToPanSplitA_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PosttrainPnPNovelFromPlateToPlateSplitA_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PosttrainPnPNovelFromTrayToCardboardboxSplitA_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PosttrainPnPNovelFromTrayToPlateSplitA_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PosttrainPnPNovelFromTrayToPotSplitA_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PosttrainPnPNovelFromTrayToTieredbasketSplitA_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
        ("gr1_unified.PosttrainPnPNovelFromTrayToTieredshelfSplitA_GR1ArmsAndWaistFourierHands_1000", 1.0, "fourier_gr1_arms_waist"),
    ],


    "SO101_pick": [
        ("pick_dataset_name", 1.0, "SO101"),
    ],

    "h10w_500l_500r": [
        ("lerobot_dataset_172", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_186_r", 1.0, "h10w_robot_config"),
    ],

    "h10w_800l_800r": [
        ("lerobot_dataset_172", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_174", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_194", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_186_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_195_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_196_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_197_r", 1.0, "h10w_robot_config"),
    ],

    "h10w_1000l_1000r": [
        ("lerobot_dataset_177", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_193", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_194", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_245", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_246", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_248", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_249", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_186_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_195_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_196_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_197_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_242_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_247_r", 1.0, "h10w_robot_config"),
    ],

    "h10w_1000l_1000r_algo": [
        ("lerobot_dataset_177", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_193", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_194", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_245", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_246", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_248", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_249", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_186_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_195_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_196_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_197_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_242_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_247_r", 1.0, "h10w_robot_config"),
        ("Whitetable_Lefthand_l101", 1.0, "h10w_robot_config"),
        ("Whitetable_Righthand_r106", 1.0, "h10w_robot_config"),
        ("Sofa_Righthand_r101", 1.0, "h10w_robot_config"),
        ("Sofa_Righthand_r101", 1.0, "h10w_robot_config"),
        ("BlackTable_Lefthand_l106", 1.0, "h10w_robot_config"),
        ("BlackTable_Righthand_r101", 1.0, "h10w_robot_config"),
        ("BlackTable_Left_Clean_l382", 1.0, "h10w_robot_config"),
        ("BlackTable_Right_Clean_r366", 1.0, "h10w_robot_config"),
        ("BlackTable_Dina_Left_l41", 1.0, "h10w_robot_config"),
        ("BlackTable_Dinasour_Right_r40", 1.0, "h10w_robot_config"),
        ("BlackTable_Dog_Left_l42", 1.0, "h10w_robot_config"),
        ("BlackTable_Dog_Right_r50", 1.0, "h10w_robot_config"),
        ("BlackTable_Duck_Left_l42", 1.0, "h10w_robot_config"),
        ("BlackTable_Duck_Right_r52", 1.0, "h10w_robot_config"),
        ("BlackTable_Lion_Left_l41", 1.0, "h10w_robot_config"),
        ("BlackTable_Lion_Right_r40", 1.0, "h10w_robot_config"),
        ("BlackTable_Mixed_Left_l114", 1.0, "h10w_robot_config"),
        ("BlackTable_Mixed_Right_r64", 1.0, "h10w_robot_config"),
        ("BlackTable_Mixed2_Right_r51", 1.0, "h10w_robot_config"),
    ],

    "full_data": [
        # left arm
        ("lerobot_dataset_171", 1.0, "h10w_robot_config"), # 简单背景 338
        ("lerobot_dataset_172", 1.0, "h10w_robot_config"), # 简单背景 499
        ("lerobot_dataset_177", 1.0, "h10w_robot_config"), # 简单背景 297
        ("lerobot_dataset_194", 1.0, "h10w_robot_config"), # 复杂背景空间关系 287
        ("lerobot_dataset_245", 1.0, "h10w_robot_config"), # 复杂背景另一只手抓着东西 100
        ("lerobot_dataset_273", 1.0, "h10w_robot_config"), # 复杂背景另一只手抓着东西 98
        ("lerobot_dataset_272", 1.0, "h10w_robot_config"), # 复杂背景另一只手抓着东西 101
        ("lerobot_dataset_193", 1.0, "h10w_robot_config"), # 暗光条件，复杂背景，简单抓放 47
        ("lerobot_dataset_246", 1.0, "h10w_robot_config"), # 暗光条件，复杂背景，简单抓放 101
        ("lerobot_dataset_248", 1.0, "h10w_robot_config"), # 复杂背景简单抓放 50
        ("lerobot_dataset_249", 1.0, "h10w_robot_config"), # 复杂背景简单抓放 50
        ("lerobot_dataset_265", 1.0, "h10w_robot_config"), # 复杂背景简单抓放，桌边 97
        ("lerobot_dataset_268", 1.0, "h10w_robot_config"), # 半复杂背景简单抓放 & 放在盘子 200
        ("lerobot_dataset_263", 1.0, "h10w_robot_config"), # 复杂背景抓放到盘子 250
        ("lerobot_dataset_286", 1.0, "h10w_robot_config"), # 299
        ("lerobot_dataset_45", 1.0, "h10w_robot_config"), # 299
        ("lerobot_dataset_51", 1.0, "h10w_robot_config"), # 299
        # right arm
        ("lerobot_dataset_186_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_270_r", 1.0, "h10w_robot_config"), # 303
        ("lerobot_dataset_271_r", 1.0, "h10w_robot_config"), # 196
        ("lerobot_dataset_267_r", 1.0, "h10w_robot_config"), # 171
        ("lerobot_dataset_275_r", 1.0, "h10w_robot_config"), # 134
        ("lerobot_dataset_242_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_274_r", 1.0, "h10w_robot_config"), # 101
        ("lerobot_dataset_261_r", 1.0, "h10w_robot_config"), # 105
        ("lerobot_dataset_247_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_196_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_197_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_276_r", 1.0, "h10w_robot_config"), # 104
        ("lerobot_dataset_266_r", 1.0, "h10w_robot_config"), # 105
        ("lerobot_dataset_269_r", 1.0, "h10w_robot_config"), # 200
        ("lerobot_dataset_264_r", 1.0, "h10w_robot_config"), # 253
        ("lerobot_dataset_285_r", 1.0, "h10w_robot_config"), # 310
        ("lerobot_dataset_46_r", 1.0, "h10w_robot_config"), # 309
        ("lerobot_dataset_52_r", 1.0, "h10w_robot_config"), # 299
    ],
    
    "full_data_fixed": [
        # left arm
        # ("lerobot_dataset_171", 1.0, "h10w_robot_config"), # 简单背景 338
        ("lerobot_dataset_172", 1.0, "h10w_robot_config"), # 简单背景 499
        # ("lerobot_dataset_177", 1.0, "h10w_robot_config"), # 简单背景 297
        # ("lerobot_dataset_194", 1.0, "h10w_robot_config"), # 复杂背景空间关系 287
        ("lerobot_dataset_245", 1.0, "h10w_robot_config"), # 复杂背景另一只手抓着东西 100
        ("lerobot_dataset_273", 1.0, "h10w_robot_config"), # 复杂背景另一只手抓着东西 98
        ("lerobot_dataset_272", 1.0, "h10w_robot_config"), # 复杂背景另一只手抓着东西 101
        # ("lerobot_dataset_193", 1.0, "h10w_robot_config"), # 暗光条件，复杂背景，简单抓放 47
        # ("lerobot_dataset_246", 1.0, "h10w_robot_config"), # 暗光条件，复杂背景，简单抓放 101
        ("lerobot_dataset_288", 1.0, "h10w_robot_config"), # 复杂背景简单抓放 50
        # ("lerobot_dataset_249", 1.0, "h10w_robot_config"), # 复杂背景简单抓放 50
        ("lerobot_dataset_265", 1.0, "h10w_robot_config"), # 复杂背景简单抓放，桌边 97
        # ("lerobot_dataset_268", 1.0, "h10w_robot_config"), # 半复杂背景简单抓放 & 放在盘子 200
        # ("lerobot_dataset_263", 1.0, "h10w_robot_config"), # 复杂背景抓放到盘子 250
        ("lerobot_dataset_286", 1.0, "h10w_robot_config"), # 299
        ("lerobot_dataset_45", 1.0, "h10w_robot_config"), # 299
        ("lerobot_dataset_51", 1.0, "h10w_robot_config"), # 299
        # right arm
        ("lerobot_dataset_186_r", 1.0, "h10w_robot_config"),
        # ("lerobot_dataset_270_r", 1.0, "h10w_robot_config"), # 303
        # ("lerobot_dataset_271_r", 1.0, "h10w_robot_config"), # 196
        # ("lerobot_dataset_267_r", 1.0, "h10w_robot_config"), # 171
        # ("lerobot_dataset_275_r", 1.0, "h10w_robot_config"), # 134
        ("lerobot_dataset_242_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_274_r", 1.0, "h10w_robot_config"), # 101
        ("lerobot_dataset_261_r", 1.0, "h10w_robot_config"), # 105
        # ("lerobot_dataset_247_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_196_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_197_r", 1.0, "h10w_robot_config"),
        # ("lerobot_dataset_276_r", 1.0, "h10w_robot_config"), # 104
        ("lerobot_dataset_266_r", 1.0, "h10w_robot_config"), # 105
        # ("lerobot_dataset_269_r", 1.0, "h10w_robot_config"), # 200
        # ("lerobot_dataset_264_r", 1.0, "h10w_robot_config"), # 253
        ("lerobot_dataset_285_r", 1.0, "h10w_robot_config"), # 310
        ("lerobot_dataset_46_r", 1.0, "h10w_robot_config"), # 309
        ("lerobot_dataset_52_r", 1.0, "h10w_robot_config"), # 299
    ],
    
    "data_baseline_lr1600": [
        # left arm
        # ("lerobot_dataset_171", 1.0, "h10w_robot_config"), # 简单背景 338
        ("lerobot_dataset_172", 1.0, "h10w_robot_config"), # 简单背景 499
        # ("lerobot_dataset_177", 1.0, "h10w_robot_config"), # 简单背景 297
        # ("lerobot_dataset_194", 1.0, "h10w_robot_config"), # 复杂背景空间关系 287
        # ("lerobot_dataset_245", 1.0, "h10w_robot_config"), # 复杂背景另一只手抓着东西 100
        # ("lerobot_dataset_273_l98", 1.0, "h10w_robot_config"), # 复杂背景另一只手抓着东西 98
        # ("lerobot_dataset_272_l101", 1.0, "h10w_robot_config"), # 复杂背景另一只手抓着东西 101
        # ("lerobot_dataset_193", 1.0, "h10w_robot_config"), # 暗光条件，复杂背景，简单抓放 47
        # ("lerobot_dataset_246", 1.0, "h10w_robot_config"), # 暗光条件，复杂背景，简单抓放 101
        # ("lerobot_dataset_248", 1.0, "h10w_robot_config"), # 复杂背景简单抓放 50
        ("lerobot_dataset_249", 1.0, "h10w_robot_config"), # 复杂背景简单抓放 248
        ("lerobot_dataset_265", 1.0, "h10w_robot_config"), # 复杂背景简单抓放，桌边 97
        ("lerobot_dataset_268", 1.0, "h10w_robot_config"), # 半复杂背景简单抓放 & 放在盘子 200
        ("lerobot_dataset_263", 1.0, "h10w_robot_config"), # 复杂背景抓放到盘子 250
        ("lerobot_dataset_286", 1.0, "h10w_robot_config"), # tv 299
        # right arm
        # ("lerobot_dataset_186_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_270_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_271_r", 1.0, "h10w_robot_config"),
        # ("lerobot_dataset_267_r", 1.0, "h10w_robot_config"),
        # ("lerobot_dataset_275_r", 1.0, "h10w_robot_config"),
        # ("lerobot_dataset_242_r", 1.0, "h10w_robot_config"),
        # ("lerobot_dataset_274_r", 1.0, "h10w_robot_config"),
        # ("lerobot_dataset_261_r", 1.0, "h10w_robot_config"),
        # ("lerobot_dataset_247_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_196_r", 1.0, "h10w_robot_config"), # 45
        ("lerobot_dataset_197_r", 1.0, "h10w_robot_config"), # 194
        # ("lerobot_dataset_276_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_266_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_269_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_264_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_285_r", 1.0, "h10w_robot_config"),
    ],
    
    "data_baseline_lr1400": [
        # left arm
        # ("lerobot_dataset_171", 1.0, "h10w_robot_config"), # 简单背景 338
        # ("lerobot_dataset_172", 1.0, "h10w_robot_config"), # 简单背景 499
        ("lerobot_dataset_177", 1.0, "h10w_robot_config"), # 简单背景 297
        # ("lerobot_dataset_194", 1.0, "h10w_robot_config"), # 复杂背景空间关系 287
        # ("lerobot_dataset_245", 1.0, "h10w_robot_config"), # 复杂背景另一只手抓着东西 100
        # ("lerobot_dataset_273_l98", 1.0, "h10w_robot_config"), # 复杂背景另一只手抓着东西 98
        # ("lerobot_dataset_272_l101", 1.0, "h10w_robot_config"), # 复杂背景另一只手抓着东西 101
        # ("lerobot_dataset_193", 1.0, "h10w_robot_config"), # 暗光条件，复杂背景，简单抓放 47
        # ("lerobot_dataset_246", 1.0, "h10w_robot_config"), # 暗光条件，复杂背景，简单抓放 101
        # ("lerobot_dataset_248", 1.0, "h10w_robot_config"), # 复杂背景简单抓放 50
        ("lerobot_dataset_249", 1.0, "h10w_robot_config"), # 复杂背景简单抓放 248
        ("lerobot_dataset_265", 1.0, "h10w_robot_config"), # 复杂背景简单抓放，桌边 97
        ("lerobot_dataset_268", 1.0, "h10w_robot_config"), # 半复杂背景简单抓放 & 放在盘子 200
        ("lerobot_dataset_263", 1.0, "h10w_robot_config"), # 复杂背景抓放到盘子 250
        ("lerobot_dataset_286", 1.0, "h10w_robot_config"), # tv 299
        # right arm
        # ("lerobot_dataset_186_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_270_r", 1.0, "h10w_robot_config"),
        # ("lerobot_dataset_271_r", 1.0, "h10w_robot_config"),
        # ("lerobot_dataset_267_r", 1.0, "h10w_robot_config"),
        # ("lerobot_dataset_275_r", 1.0, "h10w_robot_config"),
        # ("lerobot_dataset_242_r", 1.0, "h10w_robot_config"),
        # ("lerobot_dataset_274_r", 1.0, "h10w_robot_config"),
        # ("lerobot_dataset_261_r", 1.0, "h10w_robot_config"),
        # ("lerobot_dataset_247_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_196_r", 1.0, "h10w_robot_config"), # 45
        ("lerobot_dataset_197_r", 1.0, "h10w_robot_config"), # 194
        # ("lerobot_dataset_276_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_266_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_269_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_264_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_285_r", 1.0, "h10w_robot_config"),
    ],

    "h10w_18_18": [
        # left arm
        # ("lerobot_dataset_171", 1.0, "h10w_robot_config"), # 简单背景 338
        ("lerobot_dataset_172", 1.0, "h10w_robot_config"), # 简单背景 499
        # ("lerobot_dataset_177", 1.0, "h10w_robot_config"), # 简单背景 297
        # ("lerobot_dataset_194", 1.0, "h10w_robot_config"), # 复杂背景空间关系 287
        ("lerobot_dataset_245", 1.0, "h10w_robot_config"), # 复杂背景另一只手抓着东西 100
        ("lerobot_dataset_273_l98", 1.0, "h10w_robot_config"), # 复杂背景另一只手抓着东西 98
        ("lerobot_dataset_272_l101", 1.0, "h10w_robot_config"), # 复杂背景另一只手抓着东西 101
        ("lerobot_dataset_193", 1.0, "h10w_robot_config"), # 暗光条件，复杂背景，简单抓放 47
        ("lerobot_dataset_246", 1.0, "h10w_robot_config"), # 暗光条件，复杂背景，简单抓放 101
        ("lerobot_dataset_248", 1.0, "h10w_robot_config"), # 复杂背景简单抓放 50
        ("lerobot_dataset_249", 1.0, "h10w_robot_config"), # 复杂背景简单抓放 50
        ("lerobot_dataset_265_l97", 1.0, "h10w_robot_config"), # 复杂背景简单抓放，桌边 97
        ("lerobot_dataset_268_l200", 1.0, "h10w_robot_config"), # 半复杂背景简单抓放 & 放在盘子 200
        ("lerobot_dataset_263_l250", 1.0, "h10w_robot_config"), # 复杂背景抓放到盘子 250
        # right arm
        # ("lerobot_dataset_186_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_270_r303", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_271_r196", 1.0, "h10w_robot_config"),
        # ("lerobot_dataset_267_r171", 1.0, "h10w_robot_config"),
        # ("lerobot_dataset_275_r134", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_242_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_274_r101", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_261_r105", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_247_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_196_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_197_r", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_276_r104", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_266_r105", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_269_r200", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_264_r253", 1.0, "h10w_robot_config"),
    ],

    "data_latest_sofa_v2": [
        # left arm
        ("lerobot_dataset_172", 1.0, "h10w_robot_config"), # 简单背景 499
        ("lerobot_dataset_288", 1.0, "h10w_robot_config"), # 复杂背景简单抓放 298
        ("lerobot_dataset_265", 1.0, "h10w_robot_config"), # 复杂背景简单抓放，桌边 97
        ("lerobot_dataset_68", 1.0, "h10w_robot_config"),  # 沙发v2 # 255
        ("lerobot_dataset_286", 1.0, "h10w_robot_config"), # tv 299
        ("lerobot_dataset_66", 1.0, "h10w_robot_config"),  # 圆桌 301

        # right arm
        ("lerobot_dataset_186_r", 1.0, "h10w_robot_config"), # 简单背景 502
        ("lerobot_dataset_197_r", 1.0, "h10w_robot_config"), 
        ("lerobot_dataset_196_r", 1.0, "h10w_robot_config"), 
        ("lerobot_dataset_266_r", 1.0, "h10w_robot_config"),  
        ("lerobot_dataset_67_r", 1.0, "h10w_robot_config"), 
        ("lerobot_dataset_285_r", 1.0, "h10w_robot_config"),  
        ("lerobot_dataset_65_r", 1.0, "h10w_robot_config"),  
    ],

    "data_latest_white_desk_v2": [
        # left arm
        ("lerobot_dataset_69", 1.0, "h10w_robot_config"), 
        ("lerobot_dataset_70", 1.0, "h10w_robot_config"), 
        ("lerobot_dataset_45", 1.0, "h10w_robot_config"), 
        ("lerobot_dataset_286", 1.0, "h10w_robot_config"), # tv 299
        ("lerobot_dataset_66", 1.0, "h10w_robot_config"),  # 圆桌 301

        # right arm
        ("lerobot_dataset_71_r", 1.0, "h10w_robot_config"), 
        ("lerobot_dataset_46_r", 1.0, "h10w_robot_config"), 
        ("lerobot_dataset_285_r", 1.0, "h10w_robot_config"),  
        ("lerobot_dataset_65_r", 1.0, "h10w_robot_config"),  
    ],

    "data_latest_white_desk_v3": [
        # left arm
        ("lerobot_dataset_69", 1.0, "h10w_robot_config"), 
        ("lerobot_dataset_70", 1.0, "h10w_robot_config"), 
        ("lerobot_dataset_45", 1.0, "h10w_robot_config"), 
        ("lerobot_dataset_286", 1.0, "h10w_robot_config"), # tv 299
        ("lerobot_dataset_66", 1.0, "h10w_robot_config"),  # 圆桌 301

        # right arm
        ("lerobot_dataset_74_r", 1.0, "h10w_robot_config"), 
        ("lerobot_dataset_46_r", 1.0, "h10w_robot_config"), 
        ("lerobot_dataset_285_r", 1.0, "h10w_robot_config"),  
        ("lerobot_dataset_65_r", 1.0, "h10w_robot_config"),  
    ],

    "data_latest_sofa_round_v3": [
        # left arm
        ("lerobot_dataset_69", 1.0, "h10w_robot_config"), 
        ("lerobot_dataset_70", 1.0, "h10w_robot_config"), 
        ("lerobot_dataset_45", 1.0, "h10w_robot_config"), 
        ("lerobot_dataset_286", 1.0, "h10w_robot_config"), # tv 299
        ("lerobot_dataset_66", 1.0, "h10w_robot_config"),  # 圆桌 301
        ("lerobot_dataset_75", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_76", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_77", 1.0, "h10w_robot_config"),
        ("lerobot_dataset_79", 1.0, "h10w_robot_config"),

        # right arm
        ("lerobot_dataset_74_r", 1.0, "h10w_robot_config"), 
        ("lerobot_dataset_46_r", 1.0, "h10w_robot_config"), 
        ("lerobot_dataset_285_r", 1.0, "h10w_robot_config"),  
        ("lerobot_dataset_65_r", 1.0, "h10w_robot_config"),  
        ("lerobot_dataset_78_r", 1.0, "h10w_robot_config"),  
        ("lerobot_dataset_80_r", 1.0, "h10w_robot_config"),  
    ],

    "data_latest_sofa_round_v3_chunk32": [
        # left arm
        ("lerobot_dataset_69", 1.0, "h10w_robot_config_chunk32"), 
        ("lerobot_dataset_70", 1.0, "h10w_robot_config_chunk32"), 
        ("lerobot_dataset_45", 1.0, "h10w_robot_config_chunk32"), 
        ("lerobot_dataset_286", 1.0, "h10w_robot_config_chunk32"), # tv 299
        ("lerobot_dataset_66", 1.0, "h10w_robot_config_chunk32"),  # 圆桌 301
        ("lerobot_dataset_75", 1.0, "h10w_robot_config_chunk32"),
        ("lerobot_dataset_76", 1.0, "h10w_robot_config_chunk32"),
        ("lerobot_dataset_77", 1.0, "h10w_robot_config_chunk32"),
        ("lerobot_dataset_79", 1.0, "h10w_robot_config_chunk32"),

        # right arm
        ("lerobot_dataset_74_r", 1.0, "h10w_robot_config_chunk32"), 
        ("lerobot_dataset_46_r", 1.0, "h10w_robot_config_chunk32"), 
        ("lerobot_dataset_285_r", 1.0, "h10w_robot_config_chunk32"),  
        ("lerobot_dataset_65_r", 1.0, "h10w_robot_config_chunk32"),  
        ("lerobot_dataset_78_r", 1.0, "h10w_robot_config_chunk32"),  
        ("lerobot_dataset_80_r", 1.0, "h10w_robot_config_chunk32"),  
    ],

}
