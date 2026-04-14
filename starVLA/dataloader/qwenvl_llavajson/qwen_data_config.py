import re

from pathlib import Path

# You can add multimodal datasets here and register a short nickname to ${data_dict}.
# The data format should follow the general multimodal VLM format, for example:
# https://github.com/QwenLM/Qwen2.5-VL/blob/main/qwen-vl-finetune/README.md

# json_root = f"./playground/Datasets/LLaVA-OneVision-COCO/llava_jsons"
# image_root = f"./playground/Datasets/LLaVA-OneVision-COCO/images"
# json_root = f"./playground/Datasets/vlm_datasets_expo/"
# image_root = f"./playground/Datasets/vlm_datasets_expo/images"
#root = f"/home/worker/vlm_datasets"
#
## SHAREGPT4V_COCO = {
##     "annotation_path": f"{json_root}/sharegpt4v_coco.json",
##     "data_path": f"{image_root}/",
## }
#
#vlm_datasets_captionimage_expo = {
#    "annotation_path": f"{root}/vlm_datasets_captionimage_expo/vlm_dataset.json",
#    "data_path": f"{root}/vlm_datasets_captionimage_expo/images/",
#}
#
#vlm_datasets_coco_grounding = {
#    "annotation_path": f"{root}/vlm_datasets_coco_grounding/coco_val2017_qwenvl.json",
#    "data_path": f"{root}/vlm_datasets_coco_grounding/images/",
#}
#
#vlm_datasets_expo = {
#    "annotation_path": f"{root}/vlm_datasets_expo/vlm_dataset.json",
#    "data_path": f"{root}/vlm_datasets_expo/images/",
#}
#
#vlm_datasets_RefCOCO = {
#    "annotation_path": f"{root}/vlm_datasets_RefCOCO/qwen_vl_full.json",
#    "data_path": f"{root}/vlm_datasets_RefCOCO/images/",
#}
#
#vlm_datasets_RefSpatial_choice = {
#    "annotation_path": f"{root}/vlm_datasets_RefSpatial/choice_qa.json",
#    "data_path": f"{root}/vlm_datasets_RefSpatial/images/",
#}
#
#vlm_datasets_RefSpatial_qa = {
#    "annotation_path": f"{root}/vlm_datasets_RefSpatial/reasoning_template_qa.json",
#    "data_path": f"{root}/vlm_datasets_RefSpatial/images/",
#}
#
#vlm_datasets_video_expo = {
#    "annotation_path": f"{root}/vlm_datasets_video_expo/vlm_dataset.json",
#    "data_path": f"{root}/vlm_datasets_video_expo/images/",
#}
#
#vlm_datasets_video_expo_20251226 = {
#    "annotation_path": f"{root}/vlm_datasets_video_expo_20251226/vlm_dataset.json",
#    "data_path": f"{root}/vlm_datasets_video_expo_20251226/images/",
#}
#
#vlm_datasets_VSI_Bentch = {
#    "annotation_path": f"{root}/vlm_datasets_VSI-Bentch/vlm_dataset.json",
#    "data_path": f"{root}/vlm_datasets_VSI-Bentch/videos/",
#}
#
#data_dict = {
#    # "sharegpt4v_coco": SHAREGPT4V_COCO,
#    "vlm_datasets_captionimage_expo": vlm_datasets_captionimage_expo,
#    "vlm_datasets_coco_grounding": vlm_datasets_coco_grounding,
#    "vlm_datasets_RefCOCO": vlm_datasets_RefCOCO,
#    "vlm_datasets_RefSpatial_choice": vlm_datasets_RefSpatial_choice,
#    "vlm_datasets_RefSpatial_qa": vlm_datasets_RefSpatial_qa,
#    "vlm_datasets_video_expo": vlm_datasets_video_expo,
#    "vlm_datasets_video_expo_20251226": vlm_datasets_video_expo_20251226,
#    "vlm_datasets_VSI-Bentch": vlm_datasets_VSI_Bentch,
#    "vlm_datasets_expo": vlm_datasets_expo
#}

json_root = f"/home/worker/vlm_datasets/data/"

# Individual dataset definitions

share_captioner_coco_lcs_sam_1246k_1107 = {
    "annotation_path": f"{json_root}/share-captioner_coco_lcs_sam_1246k_1107.json",
    "data_path": f"/",
}

sharegpt4v_mix665k_cap23k_coco_ap9k_lcs3k_sam9k_div2k = {
    "annotation_path": f"{json_root}/sharegpt4v_mix665k_cap23k_coco-ap9k_lcs3k_sam9k_div2k.json",
    "data_path": f"/",
}

sharegpt4v_instruct_gpt4_vision_cap100k = {
    "annotation_path": f"{json_root}/sharegpt4v_instruct_gpt4-vision_cap100k.json",
    "data_path": f"/",
}

vlm_dataset_AS_V2_region_captioning_63k = {
    "annotation_path": f"{json_root}/vlm_dataset_AS_V2_region_captioning_63k.json",
    "data_path": f"/",
}

vlm_dataset_TallyQA = {
    "annotation_path": f"{json_root}/vlm_dataset_TallyQA.json",
    "data_path": f"/",
}

vlm_dataset_AS_V2_conversation_22k = {
    "annotation_path": f"{json_root}/vlm_dataset_AS_V2_conversation_22k.json",
    "data_path": f"/",
}

vlm_dataset_ok_vqa = {
    "annotation_path": f"{json_root}/vlm_dataset_ok_vqa.json",
    "data_path": f"/",
}

vlm_dataset_the_cauldron = {
    "annotation_path": f"{json_root}/vlm_dataset_the_cauldron.json",
    "data_path": f"/",
}

vlm_dataset_AS_V2_detailed_description_42k = {
    "annotation_path": f"{json_root}/vlm_dataset_AS_V2_detailed_description_42k.json",
    "data_path": f"/",
}

vlm_dataset_sharegpt4v_long_captions = {
    "annotation_path": f"{json_root}/vlm_dataset_sharegpt4v-long-captions.json",
    "data_path": f"/",
}

vlm_dataset_vqav2 = {
    "annotation_path": f"{json_root}/vlm_dataset_vqav2.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_261_r105 = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_261_r105.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_263_l250 = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_263_l250.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_264_r253 = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_264_r253.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_265_l97 = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_265_l97.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_266_r105 = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_266_r105.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_267_r171 = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_267_r171.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_268_l200 = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_268_l200.json",
    "data_path": f"/",
}

smoltalk_chinese = {
    "annotation_path": f"{json_root}/smoltalk-chinese.json",
    "data_path": f"/",
}

identity = {
    "annotation_path": f"{json_root}/identity.json",
    "data_path": f"/",
}

# Add these dataset definitions (place them after the existing H10W datasets):

vlm_dataset_H10W_real_data_1112_BlackTable_Right = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_BlackTable_Right.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_BlackTable_Righthand = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_BlackTable_Righthand.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_Sofa_Lefthand = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_Sofa_Lefthand.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_Sofa_Righthand = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_Sofa_Righthand.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_Whitetable_Lefthand = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_Whitetable_Lefthand.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_Whitetable_Righthand = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_Whitetable_Righthand.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_2_BlackTable_Dina_Left = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_2_BlackTable_Dina_Left.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_2_BlackTable_Dinasour_Right = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_2_BlackTable_Dinasour_Right.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_2_BlackTable_Dog_Left = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_2_BlackTable_Dog_Left.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_2_BlackTable_Dog_Right = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_2_BlackTable_Dog_Right.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_2_BlackTable_Duck_Left = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_2_BlackTable_Duck_Left.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_2_BlackTable_Duck_Right = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_2_BlackTable_Duck_Right.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_2_BlackTable_Frombox = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_2_BlackTable_Frombox.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_2_BlackTable_Left = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_2_BlackTable_Left.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_2_BlackTable_Lefthand = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_2_BlackTable_Lefthand.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_2_BlackTable_Lion_Left = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_2_BlackTable_Lion_Left.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_2_BlackTable_Lion_Right = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_2_BlackTable_Lion_Right.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_2_BlackTable_Mixed2_Right = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_2_BlackTable_Mixed2_Right.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_2_BlackTable_Mixed_Left = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_2_BlackTable_Mixed_Left.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_2_BlackTable_Mixed_Right = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_2_BlackTable_Mixed_Right.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_3_BlackTable_ClosedGripper = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_3_BlackTable_ClosedGripper.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_3_BlackTable_Left = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_3_BlackTable_Left.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_3_BlackTable_Left_Clean = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_3_BlackTable_Left_Clean.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_3_BlackTable_Left_White = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_3_BlackTable_Left_White.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_3_BlackTable_Long_Left = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_3_BlackTable_Long_Left.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_3_BlackTable_Long_Right = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_3_BlackTable_Long_Right.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_3_BlackTable_Long_RightPlace = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_3_BlackTable_Long_RightPlace.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_3_BlackTable_NoAction = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_3_BlackTable_NoAction.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_3_BlackTable_Right = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_3_BlackTable_Right.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_3_BlackTable_Right_Clean = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_3_BlackTable_Right_Clean.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_3_BlackTable_Right_White = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_3_BlackTable_Right_White.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_4_BlackTable_Water = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_4_BlackTable_Water.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_4_Give_Righthand_Roundtable = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_4_Give_Righthand_Roundtable.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_4_Roundtable_Clean = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_4_Roundtable_Clean.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_4_Roundtable_Lefthand = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_4_Roundtable_Lefthand.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_4_Roundtable_Leftthand_Place = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_4_Roundtable_Leftthand_Place.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_4_Roundtable_Righthand = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_4_Roundtable_Righthand.json",
    "data_path": f"/",
}

vlm_dataset_H10W_real_data_1112_4_Roundtable_Righthand_Place = {
    "annotation_path": f"{json_root}/vlm_dataset_H10W_real_data_1112_4_Roundtable_Righthand_Place.json",
    "data_path": f"/",
}

# New lerobot datasets
vlm_dataset_lerobot_dataset_242_r = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_242_r.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_245 = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_245.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_246 = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_246.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_247_r = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_247_r.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_248 = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_248.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_249 = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_249.json",
    "data_path": f"/",
}

vlm_dataset_Agibot_World_beta = {
    "annotation_path": f"{json_root}/vlm_dataset_Agibot_World_beta.json",
    "data_path": f"/",
}

vlm_dataset_captionimage_expo = {
    "annotation_path": f"{json_root}/vlm_dataset_captionimage_expo.json",
    "data_path": f"/",
}

vlm_dataset_coco_grounding = {
    "annotation_path": f"{json_root}/vlm_dataset_coco_grounding.json",
    "data_path": f"/",
}

vlm_dataset_expo_video_20251226 = {
    "annotation_path": f"{json_root}/vlm_dataset_expo_video_20251226.json",
    "data_path": f"/",
}

vlm_dataset_expo_video_20251225 = {
    "annotation_path": f"{json_root}/vlm_dataset_expo_video_20251225.json",
    "data_path": f"/",
}

vlm_dataset_expo = {
    "annotation_path": f"{json_root}/vlm_dataset_expo.json",
    "data_path": f"/",
}

vlm_dataset_verification = {
    "annotation_path": f"{json_root}/vlm_dataset_verification.json",
    "data_path": f"/",
}

vlm_dataset_RefSpatial_reasoning_template_qa = {
    "annotation_path": f"{json_root}/vlm_dataset_RefSpatial_reasoning_template_qa.json",
    "data_path": f"/",
}

vlm_dataset_RefSpatial_choice_qa = {
    "annotation_path": f"{json_root}/vlm_dataset_RefSpatial_choice_qa.json",
    "data_path": f"/",
}

vlm_dataset_RefCOCO = {
    "annotation_path": f"{json_root}/vlm_dataset_RefCOCO.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_battery_b = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_battery_b.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_battery_storage_c = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_battery_storage_c.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_box_storage_b = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_box_storage_b.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_box_storage_c = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_box_storage_c.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_box_storage_cardboard_box_a = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_box_storage_cardboard_box_a.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_box_storage_cardboard_box_b = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_box_storage_cardboard_box_b.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_box_storage_cardboard_box_c = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_box_storage_cardboard_box_c.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_box_storage_e = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_box_storage_e.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_box_storage_tool = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_box_storage_tool.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_left_capture_part = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_left_capture_part.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_mobile_accessory_storage_box_a = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_mobile_accessory_storage_box_a.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_mobile_accessory_storage_box_c = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_mobile_accessory_storage_box_c.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_mobile_accessory_storage_box_d = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_mobile_accessory_storage_box_d.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_mobile_accessory_storage_box_e = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_mobile_accessory_storage_box_e.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_mobile_accessory_storage_box_f = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_mobile_accessory_storage_box_f.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_pick_up_battery = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_pick_up_battery.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_picks_up_battery_a = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_picks_up_battery_a.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_picks_up_battery_b = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_picks_up_battery_b.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_picks_up_cardboard_box = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_picks_up_cardboard_box.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_picks_up_parts_a = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_picks_up_parts_a.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_picks_up_parts_b = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_picks_up_parts_b.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_remove_the_accessory = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_remove_the_accessory.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_robotic_arm_picks_up_battery = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_robotic_arm_picks_up_battery.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_robotic_arm_picks_up_parts = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_robotic_arm_picks_up_parts.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_storage_item_b = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_storage_item_b.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_storage_item_d = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_storage_item_d.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_storage_item_e = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_storage_item_e.json",
    "data_path": f"/",
}

vlm_dataset_agibot_go1_tool_storage = {
    "annotation_path": f"{json_root}/vlm_dataset_agibot_go1_tool_storage.json",
    "data_path": f"/",
}

vlm_dataset_galbot_go1_fold_clothe_b = {
    "annotation_path": f"{json_root}/vlm_dataset_galbot_go1_fold_clothe_b.json",
    "data_path": f"/",
}

vlm_dataset_galbot_go1_fold_clothe_c = {
    "annotation_path": f"{json_root}/vlm_dataset_galbot_go1_fold_clothe_c.json",
    "data_path": f"/",
}

vlm_dataset_galbot_go1_fold_clothe_e = {
    "annotation_path": f"{json_root}/vlm_dataset_galbot_go1_fold_clothe_e.json",
    "data_path": f"/",
}

vlm_dataset_galbot_go1_steamer_storage_baozi_a = {
    "annotation_path": f"{json_root}/vlm_dataset_galbot_go1_steamer_storage_baozi_a.json",
    "data_path": f"/",
}

vlm_dataset_galbot_go1_steamer_storage_baozi_b = {
    "annotation_path": f"{json_root}/vlm_dataset_galbot_go1_steamer_storage_baozi_b.json",
    "data_path": f"/",
}

vlm_dataset_galbot_go1_steamer_storage_baozi_c = {
    "annotation_path": f"{json_root}/vlm_dataset_galbot_go1_steamer_storage_baozi_c.json",
    "data_path": f"/",
}

vlm_dataset_galbot_go1_steamer_storage_baozi_d = {
    "annotation_path": f"{json_root}/vlm_dataset_galbot_go1_steamer_storage_baozi_d.json",
    "data_path": f"/",
}

vlm_dataset_galbot_go1_steamer_storage_baozi_e = {
    "annotation_path": f"{json_root}/vlm_dataset_galbot_go1_steamer_storage_baozi_e.json",
    "data_path": f"/",
}

vlm_dataset_galbot_go1_steamer_storage_baozi_f = {
    "annotation_path": f"{json_root}/vlm_dataset_galbot_go1_steamer_storage_baozi_f.json",
    "data_path": f"/",
}

vlm_dataset_galbot_go1_steamer_storage_baozi_g = {
    "annotation_path": f"{json_root}/vlm_dataset_galbot_go1_steamer_storage_baozi_g.json",
    "data_path": f"/",
}

vlm_dataset_galbot_go1_steamer_storage_baozi_h = {
    "annotation_path": f"{json_root}/vlm_dataset_galbot_go1_steamer_storage_baozi_h.json",
    "data_path": f"/",
}

vlm_dataset_galbot_go1_steamer_storage_baozi_i = {
    "annotation_path": f"{json_root}/vlm_dataset_galbot_go1_steamer_storage_baozi_i.json",
    "data_path": f"/",
}

vlm_dataset_galbot_go1_steamer_storage_baozi_j = {
    "annotation_path": f"{json_root}/vlm_dataset_galbot_go1_steamer_storage_baozi_j.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_basket_storage_banana = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_basket_storage_banana.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_basket_storage_egg_yolk_pastry = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_basket_storage_egg_yolk_pastry.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_basket_storage_long_bread = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_basket_storage_long_bread.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_basket_storage_orange = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_basket_storage_orange.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_basket_storage_peach = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_basket_storage_peach.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_box_up_down = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_box_up_down.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_desktop_organization = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_desktop_organization.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_fold_shirt = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_fold_shirt.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_fold_shorts = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_fold_shorts.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_fold_towel = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_fold_towel.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_food_packaging = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_food_packaging.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_food_storage = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_food_storage.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_fruit_storage = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_fruit_storage.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_get_water = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_get_water.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_glasses_storage = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_glasses_storage.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_organise_the_document_bag = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_organise_the_document_bag.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_place_test_tube = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_place_test_tube.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_place_the_fruits_repeatedly = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_place_the_fruits_repeatedly.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_place_towel = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_place_towel.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_plate_storage = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_plate_storage.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_pour_coffee_beans = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_pour_coffee_beans.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_pour_rice = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_pour_rice.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_pour_tea = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_pour_tea.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_pull_open_bag = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_pull_open_bag.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_stack_baskets = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_stack_baskets.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_stir_coffee = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_stir_coffee.json",
    "data_path": f"/",
}

vlm_dataset_rmc_aida_l_storage_bin_storage = {
    "annotation_path": f"{json_root}/vlm_dataset_rmc_aida_l_storage_bin_storage.json",
    "data_path": f"/",
}

vlm_dataset_tianqin_a2_box_storage_part = {
    "annotation_path": f"{json_root}/vlm_dataset_tianqin_a2_box_storage_part.json",
    "data_path": f"/",
}

vlm_dataset_tianqin_a2_container_storage_graphics_card = {
    "annotation_path": f"{json_root}/vlm_dataset_tianqin_a2_container_storage_graphics_card.json",
    "data_path": f"/",
}

vlm_dataset_tianqin_a2_place_the_paper_box = {
    "annotation_path": f"{json_root}/vlm_dataset_tianqin_a2_place_the_paper_box.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_167 = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_167.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_171 = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_171.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_172 = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_172.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_174 = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_174.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_177 = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_177.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_186_r = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_186_r.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_194 = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_194.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_195_r = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_195_r.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_196_r = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_196_r.json",
    "data_path": f"/",
}

vlm_dataset_lerobot_dataset_197_r = {
    "annotation_path": f"{json_root}/vlm_dataset_lerobot_dataset_197_r.json",
    "data_path": f"/",
}

# Data dictionary mapping
data_dict = {
    "identity": identity,
    "share_captioner_coco_lcs_sam_1246k_1107": share_captioner_coco_lcs_sam_1246k_1107,
    "sharegpt4v_mix665k_cap23k_coco_ap9k_lcs3k_sam9k_div2k": sharegpt4v_mix665k_cap23k_coco_ap9k_lcs3k_sam9k_div2k,
    "sharegpt4v_instruct_gpt4_vision_cap100k": sharegpt4v_instruct_gpt4_vision_cap100k,
    "vlm_dataset_AS_V2_region_captioning_63k": vlm_dataset_AS_V2_region_captioning_63k,
    "vlm_dataset_TallyQA": vlm_dataset_TallyQA,
    "vlm_dataset_AS_V2_conversation_22k": vlm_dataset_AS_V2_conversation_22k,
    "vlm_dataset_ok_vqa": vlm_dataset_ok_vqa,
    "vlm_dataset_the_cauldron": vlm_dataset_the_cauldron,
    "vlm_dataset_AS_V2_detailed_description_42k": vlm_dataset_AS_V2_detailed_description_42k,
    "vlm_dataset_sharegpt4v_long_captions": vlm_dataset_sharegpt4v_long_captions,
    "vlm_dataset_vqav2": vlm_dataset_vqav2,
    "vlm_dataset_lerobot_dataset_261_r105": vlm_dataset_lerobot_dataset_261_r105,
    "vlm_dataset_lerobot_dataset_263_l250": vlm_dataset_lerobot_dataset_263_l250,
    "vlm_dataset_lerobot_dataset_264_r253": vlm_dataset_lerobot_dataset_264_r253,
    "vlm_dataset_lerobot_dataset_265_l97": vlm_dataset_lerobot_dataset_265_l97,
    "vlm_dataset_lerobot_dataset_266_r105": vlm_dataset_lerobot_dataset_266_r105,
    "vlm_dataset_lerobot_dataset_267_r171": vlm_dataset_lerobot_dataset_267_r171,
    "vlm_dataset_lerobot_dataset_268_l200": vlm_dataset_lerobot_dataset_268_l200,
    "smoltalk-chinese": smoltalk_chinese,
    "vlm_dataset_H10W_real_data_1112_BlackTable_Right": vlm_dataset_H10W_real_data_1112_BlackTable_Right,
    "vlm_dataset_H10W_real_data_1112_BlackTable_Righthand": vlm_dataset_H10W_real_data_1112_BlackTable_Righthand,
    "vlm_dataset_H10W_real_data_1112_Sofa_Lefthand": vlm_dataset_H10W_real_data_1112_Sofa_Lefthand,
    "vlm_dataset_H10W_real_data_1112_Sofa_Righthand": vlm_dataset_H10W_real_data_1112_Sofa_Righthand,
    "vlm_dataset_H10W_real_data_1112_Whitetable_Lefthand": vlm_dataset_H10W_real_data_1112_Whitetable_Lefthand,
    "vlm_dataset_H10W_real_data_1112_Whitetable_Righthand": vlm_dataset_H10W_real_data_1112_Whitetable_Righthand,
    "vlm_dataset_H10W_real_data_1112_2_BlackTable_Dina_Left": vlm_dataset_H10W_real_data_1112_2_BlackTable_Dina_Left,
    "vlm_dataset_H10W_real_data_1112_2_BlackTable_Dinasour_Right": vlm_dataset_H10W_real_data_1112_2_BlackTable_Dinasour_Right,
    "vlm_dataset_H10W_real_data_1112_2_BlackTable_Dog_Left": vlm_dataset_H10W_real_data_1112_2_BlackTable_Dog_Left,
    "vlm_dataset_H10W_real_data_1112_2_BlackTable_Dog_Right": vlm_dataset_H10W_real_data_1112_2_BlackTable_Dog_Right,
    "vlm_dataset_H10W_real_data_1112_2_BlackTable_Duck_Left": vlm_dataset_H10W_real_data_1112_2_BlackTable_Duck_Left,
    "vlm_dataset_H10W_real_data_1112_2_BlackTable_Duck_Right": vlm_dataset_H10W_real_data_1112_2_BlackTable_Duck_Right,
    "vlm_dataset_H10W_real_data_1112_2_BlackTable_Frombox": vlm_dataset_H10W_real_data_1112_2_BlackTable_Frombox,
    "vlm_dataset_H10W_real_data_1112_2_BlackTable_Left": vlm_dataset_H10W_real_data_1112_2_BlackTable_Left,
    "vlm_dataset_H10W_real_data_1112_2_BlackTable_Lefthand": vlm_dataset_H10W_real_data_1112_2_BlackTable_Lefthand,
    "vlm_dataset_H10W_real_data_1112_2_BlackTable_Lion_Left": vlm_dataset_H10W_real_data_1112_2_BlackTable_Lion_Left,
    "vlm_dataset_H10W_real_data_1112_2_BlackTable_Lion_Right": vlm_dataset_H10W_real_data_1112_2_BlackTable_Lion_Right,
    "vlm_dataset_H10W_real_data_1112_2_BlackTable_Mixed2_Right": vlm_dataset_H10W_real_data_1112_2_BlackTable_Mixed2_Right,
    "vlm_dataset_H10W_real_data_1112_2_BlackTable_Mixed_Left": vlm_dataset_H10W_real_data_1112_2_BlackTable_Mixed_Left,
    "vlm_dataset_H10W_real_data_1112_2_BlackTable_Mixed_Right": vlm_dataset_H10W_real_data_1112_2_BlackTable_Mixed_Right,
    "vlm_dataset_H10W_real_data_1112_3_BlackTable_ClosedGripper": vlm_dataset_H10W_real_data_1112_3_BlackTable_ClosedGripper,
    "vlm_dataset_H10W_real_data_1112_3_BlackTable_Left": vlm_dataset_H10W_real_data_1112_3_BlackTable_Left,
    "vlm_dataset_H10W_real_data_1112_3_BlackTable_Left_Clean": vlm_dataset_H10W_real_data_1112_3_BlackTable_Left_Clean,
    "vlm_dataset_H10W_real_data_1112_3_BlackTable_Left_White": vlm_dataset_H10W_real_data_1112_3_BlackTable_Left_White,
    "vlm_dataset_H10W_real_data_1112_3_BlackTable_Long_Left": vlm_dataset_H10W_real_data_1112_3_BlackTable_Long_Left,
    "vlm_dataset_H10W_real_data_1112_3_BlackTable_Long_Right": vlm_dataset_H10W_real_data_1112_3_BlackTable_Long_Right,
    "vlm_dataset_H10W_real_data_1112_3_BlackTable_Long_RightPlace": vlm_dataset_H10W_real_data_1112_3_BlackTable_Long_RightPlace,
    "vlm_dataset_H10W_real_data_1112_3_BlackTable_NoAction": vlm_dataset_H10W_real_data_1112_3_BlackTable_NoAction,
    "vlm_dataset_H10W_real_data_1112_3_BlackTable_Right": vlm_dataset_H10W_real_data_1112_3_BlackTable_Right,
    "vlm_dataset_H10W_real_data_1112_3_BlackTable_Right_Clean": vlm_dataset_H10W_real_data_1112_3_BlackTable_Right_Clean,
    "vlm_dataset_H10W_real_data_1112_3_BlackTable_Right_White": vlm_dataset_H10W_real_data_1112_3_BlackTable_Right_White,
    "vlm_dataset_H10W_real_data_1112_4_BlackTable_Water": vlm_dataset_H10W_real_data_1112_4_BlackTable_Water,
    "vlm_dataset_H10W_real_data_1112_4_Give_Righthand_Roundtable": vlm_dataset_H10W_real_data_1112_4_Give_Righthand_Roundtable,
    "vlm_dataset_H10W_real_data_1112_4_Roundtable_Clean": vlm_dataset_H10W_real_data_1112_4_Roundtable_Clean,
    "vlm_dataset_H10W_real_data_1112_4_Roundtable_Lefthand": vlm_dataset_H10W_real_data_1112_4_Roundtable_Lefthand,
    "vlm_dataset_H10W_real_data_1112_4_Roundtable_Leftthand_Place": vlm_dataset_H10W_real_data_1112_4_Roundtable_Leftthand_Place,
    "vlm_dataset_H10W_real_data_1112_4_Roundtable_Righthand": vlm_dataset_H10W_real_data_1112_4_Roundtable_Righthand,
    "vlm_dataset_H10W_real_data_1112_4_Roundtable_Righthand_Place": vlm_dataset_H10W_real_data_1112_4_Roundtable_Righthand_Place,
    "vlm_dataset_lerobot_dataset_242_r": vlm_dataset_lerobot_dataset_242_r,
    "vlm_dataset_lerobot_dataset_245": vlm_dataset_lerobot_dataset_245,
    "vlm_dataset_lerobot_dataset_246": vlm_dataset_lerobot_dataset_246,
    "vlm_dataset_lerobot_dataset_247_r": vlm_dataset_lerobot_dataset_247_r,
    "vlm_dataset_lerobot_dataset_248": vlm_dataset_lerobot_dataset_248,
    "vlm_dataset_lerobot_dataset_249": vlm_dataset_lerobot_dataset_249,
    "vlm_dataset_Agibot_World_beta": vlm_dataset_Agibot_World_beta,
    "vlm_dataset_captionimage_expo": vlm_dataset_captionimage_expo,
    "vlm_dataset_coco_grounding": vlm_dataset_coco_grounding,
    "vlm_dataset_expo_video_20251226": vlm_dataset_expo_video_20251226,
    "vlm_dataset_expo_video_20251225": vlm_dataset_expo_video_20251225,
    "vlm_dataset_expo": vlm_dataset_expo,
    "vlm_dataset_verification": vlm_dataset_verification,
    "vlm_dataset_RefSpatial_reasoning_template_qa": vlm_dataset_RefSpatial_reasoning_template_qa,
    "vlm_dataset_RefSpatial_choice_qa": vlm_dataset_RefSpatial_choice_qa,
    "vlm_dataset_RefCOCO": vlm_dataset_RefCOCO,
    "vlm_dataset_agibot_go1_battery_b": vlm_dataset_agibot_go1_battery_b,
    "vlm_dataset_agibot_go1_battery_storage_c": vlm_dataset_agibot_go1_battery_storage_c,
    "vlm_dataset_agibot_go1_box_storage_b": vlm_dataset_agibot_go1_box_storage_b,
    "vlm_dataset_agibot_go1_box_storage_c": vlm_dataset_agibot_go1_box_storage_c,
    "vlm_dataset_agibot_go1_box_storage_cardboard_box_a": vlm_dataset_agibot_go1_box_storage_cardboard_box_a,
    "vlm_dataset_agibot_go1_box_storage_cardboard_box_b": vlm_dataset_agibot_go1_box_storage_cardboard_box_b,
    "vlm_dataset_agibot_go1_box_storage_cardboard_box_c": vlm_dataset_agibot_go1_box_storage_cardboard_box_c,
    "vlm_dataset_agibot_go1_box_storage_e": vlm_dataset_agibot_go1_box_storage_e,
    "vlm_dataset_agibot_go1_box_storage_tool": vlm_dataset_agibot_go1_box_storage_tool,
    "vlm_dataset_agibot_go1_left_capture_part": vlm_dataset_agibot_go1_left_capture_part,
    "vlm_dataset_agibot_go1_mobile_accessory_storage_box_a": vlm_dataset_agibot_go1_mobile_accessory_storage_box_a,
    "vlm_dataset_agibot_go1_mobile_accessory_storage_box_c": vlm_dataset_agibot_go1_mobile_accessory_storage_box_c,
    "vlm_dataset_agibot_go1_mobile_accessory_storage_box_d": vlm_dataset_agibot_go1_mobile_accessory_storage_box_d,
    "vlm_dataset_agibot_go1_mobile_accessory_storage_box_e": vlm_dataset_agibot_go1_mobile_accessory_storage_box_e,
    "vlm_dataset_agibot_go1_mobile_accessory_storage_box_f": vlm_dataset_agibot_go1_mobile_accessory_storage_box_f,
    "vlm_dataset_agibot_go1_pick_up_battery": vlm_dataset_agibot_go1_pick_up_battery,
    "vlm_dataset_agibot_go1_picks_up_battery_a": vlm_dataset_agibot_go1_picks_up_battery_a,
    "vlm_dataset_agibot_go1_picks_up_battery_b": vlm_dataset_agibot_go1_picks_up_battery_b,
    "vlm_dataset_agibot_go1_picks_up_cardboard_box": vlm_dataset_agibot_go1_picks_up_cardboard_box,
    "vlm_dataset_agibot_go1_picks_up_parts_a": vlm_dataset_agibot_go1_picks_up_parts_a,
    "vlm_dataset_agibot_go1_picks_up_parts_b": vlm_dataset_agibot_go1_picks_up_parts_b,
    "vlm_dataset_agibot_go1_remove_the_accessory": vlm_dataset_agibot_go1_remove_the_accessory,
    "vlm_dataset_agibot_go1_robotic_arm_picks_up_battery": vlm_dataset_agibot_go1_robotic_arm_picks_up_battery,
    "vlm_dataset_agibot_go1_robotic_arm_picks_up_parts": vlm_dataset_agibot_go1_robotic_arm_picks_up_parts,
    "vlm_dataset_agibot_go1_storage_item_b": vlm_dataset_agibot_go1_storage_item_b,
    "vlm_dataset_agibot_go1_storage_item_d": vlm_dataset_agibot_go1_storage_item_d,
    "vlm_dataset_agibot_go1_storage_item_e": vlm_dataset_agibot_go1_storage_item_e,
    "vlm_dataset_agibot_go1_tool_storage": vlm_dataset_agibot_go1_tool_storage,
    "vlm_dataset_galbot_go1_fold_clothe_b": vlm_dataset_galbot_go1_fold_clothe_b,
    "vlm_dataset_galbot_go1_fold_clothe_c": vlm_dataset_galbot_go1_fold_clothe_c,
    "vlm_dataset_galbot_go1_fold_clothe_e": vlm_dataset_galbot_go1_fold_clothe_e,
    "vlm_dataset_galbot_go1_steamer_storage_baozi_a": vlm_dataset_galbot_go1_steamer_storage_baozi_a,
    "vlm_dataset_galbot_go1_steamer_storage_baozi_b": vlm_dataset_galbot_go1_steamer_storage_baozi_b,
    "vlm_dataset_galbot_go1_steamer_storage_baozi_c": vlm_dataset_galbot_go1_steamer_storage_baozi_c,
    "vlm_dataset_galbot_go1_steamer_storage_baozi_d": vlm_dataset_galbot_go1_steamer_storage_baozi_d,
    "vlm_dataset_galbot_go1_steamer_storage_baozi_e": vlm_dataset_galbot_go1_steamer_storage_baozi_e,
    "vlm_dataset_galbot_go1_steamer_storage_baozi_f": vlm_dataset_galbot_go1_steamer_storage_baozi_f,
    "vlm_dataset_galbot_go1_steamer_storage_baozi_g": vlm_dataset_galbot_go1_steamer_storage_baozi_g,
    "vlm_dataset_galbot_go1_steamer_storage_baozi_h": vlm_dataset_galbot_go1_steamer_storage_baozi_h,
    "vlm_dataset_galbot_go1_steamer_storage_baozi_i": vlm_dataset_galbot_go1_steamer_storage_baozi_i,
    "vlm_dataset_galbot_go1_steamer_storage_baozi_j": vlm_dataset_galbot_go1_steamer_storage_baozi_j,
    "vlm_dataset_rmc_aida_l_basket_storage_banana": vlm_dataset_rmc_aida_l_basket_storage_banana,
    "vlm_dataset_rmc_aida_l_basket_storage_egg_yolk_pastry": vlm_dataset_rmc_aida_l_basket_storage_egg_yolk_pastry,
    "vlm_dataset_rmc_aida_l_basket_storage_long_bread": vlm_dataset_rmc_aida_l_basket_storage_long_bread,
    "vlm_dataset_rmc_aida_l_basket_storage_orange": vlm_dataset_rmc_aida_l_basket_storage_orange,
    "vlm_dataset_rmc_aida_l_basket_storage_peach": vlm_dataset_rmc_aida_l_basket_storage_peach,
    "vlm_dataset_rmc_aida_l_box_up_down": vlm_dataset_rmc_aida_l_box_up_down,
    "vlm_dataset_rmc_aida_l_desktop_organization": vlm_dataset_rmc_aida_l_desktop_organization,
    "vlm_dataset_rmc_aida_l_fold_shirt": vlm_dataset_rmc_aida_l_fold_shirt,
    "vlm_dataset_rmc_aida_l_fold_shorts": vlm_dataset_rmc_aida_l_fold_shorts,
    "vlm_dataset_rmc_aida_l_fold_towel": vlm_dataset_rmc_aida_l_fold_towel,
    "vlm_dataset_rmc_aida_l_food_packaging": vlm_dataset_rmc_aida_l_food_packaging,
    "vlm_dataset_rmc_aida_l_food_storage": vlm_dataset_rmc_aida_l_food_storage,
    "vlm_dataset_rmc_aida_l_fruit_storage": vlm_dataset_rmc_aida_l_fruit_storage,
    "vlm_dataset_rmc_aida_l_get_water": vlm_dataset_rmc_aida_l_get_water,
    "vlm_dataset_rmc_aida_l_glasses_storage": vlm_dataset_rmc_aida_l_glasses_storage,
    "vlm_dataset_rmc_aida_l_organise_the_document_bag": vlm_dataset_rmc_aida_l_organise_the_document_bag,
    "vlm_dataset_rmc_aida_l_place_test_tube": vlm_dataset_rmc_aida_l_place_test_tube,
    "vlm_dataset_rmc_aida_l_place_the_fruits_repeatedly": vlm_dataset_rmc_aida_l_place_the_fruits_repeatedly,
    "vlm_dataset_rmc_aida_l_place_towel": vlm_dataset_rmc_aida_l_place_towel,
    "vlm_dataset_rmc_aida_l_plate_storage": vlm_dataset_rmc_aida_l_plate_storage,
    "vlm_dataset_rmc_aida_l_pour_coffee_beans": vlm_dataset_rmc_aida_l_pour_coffee_beans,
    "vlm_dataset_rmc_aida_l_pour_rice": vlm_dataset_rmc_aida_l_pour_rice,
    "vlm_dataset_rmc_aida_l_pour_tea": vlm_dataset_rmc_aida_l_pour_tea,
    "vlm_dataset_rmc_aida_l_pull_open_bag": vlm_dataset_rmc_aida_l_pull_open_bag,
    "vlm_dataset_rmc_aida_l_stack_baskets": vlm_dataset_rmc_aida_l_stack_baskets,
    "vlm_dataset_rmc_aida_l_stir_coffee": vlm_dataset_rmc_aida_l_stir_coffee,
    "vlm_dataset_rmc_aida_l_storage_bin_storage": vlm_dataset_rmc_aida_l_storage_bin_storage,
    "vlm_dataset_tianqin_a2_box_storage_part": vlm_dataset_tianqin_a2_box_storage_part,
    "vlm_dataset_tianqin_a2_container_storage_graphics_card": vlm_dataset_tianqin_a2_container_storage_graphics_card,
    "vlm_dataset_tianqin_a2_place_the_paper_box": vlm_dataset_tianqin_a2_place_the_paper_box,
    "vlm_dataset_lerobot_dataset_167": vlm_dataset_lerobot_dataset_167,
    "vlm_dataset_lerobot_dataset_171": vlm_dataset_lerobot_dataset_171,
    "vlm_dataset_lerobot_dataset_172": vlm_dataset_lerobot_dataset_172,
    "vlm_dataset_lerobot_dataset_174": vlm_dataset_lerobot_dataset_174,
    "vlm_dataset_lerobot_dataset_177": vlm_dataset_lerobot_dataset_177,
    "vlm_dataset_lerobot_dataset_186_r": vlm_dataset_lerobot_dataset_186_r,
    "vlm_dataset_lerobot_dataset_194": vlm_dataset_lerobot_dataset_194,
    "vlm_dataset_lerobot_dataset_195_r": vlm_dataset_lerobot_dataset_195_r,
    "vlm_dataset_lerobot_dataset_196_r": vlm_dataset_lerobot_dataset_196_r,
    "vlm_dataset_lerobot_dataset_197_r": vlm_dataset_lerobot_dataset_197_r,
}

def parse_sampling_rate(dataset_name):
    match = re.search(r"%(\d+)$", dataset_name)
    if match:
        return int(match.group(1)) / 100.0
    return 1.0

def data_list(dataset_names):
    if dataset_names == ["all"]:
        dataset_names = list(data_dict.keys())
    config_list = []
    for dataset_name in dataset_names:
        sampling_rate = parse_sampling_rate(dataset_name)
        dataset_name = re.sub(r"%(\d+)$", "", dataset_name)
        if dataset_name in data_dict.keys():
            config = data_dict[dataset_name].copy()
            config["sampling_rate"] = sampling_rate
            config_list.append(config)
        else:
            raise ValueError(f"do not find {dataset_name}")
    return config_list

if __name__ == "__main__":
    print(data_list)
    
