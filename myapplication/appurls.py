from xml.dom import ValidationErr

from django.conf import settings
from django.urls import path, include
from . import  views
urlpatterns = [
    path('home_load/',views.home_load),
    path('login_load/', views.login_load),
    path('adm_index_load/',views.adm_index_load),
    path('adm_addplce_load/',views.adm_addplce_load),
    path('adm_Bussines_load/', views.adm_Bussines_load),
    path('adm_ChngePaswrd_load/', views.adm_ChngePaswrd_load),
    path('adm_editplce_load/<str:id>',views.adm_editplce_load),
    path('adm_fedbck_load/', views.adm_fedbck_load),
    path('adm_rtingandview_load/', views.adm_rtingandview_load),
    path('adm_sndrply_load/<str:cid>',views.adm_sndrply_load),
    path('adm_usrview_load/', views.adm_usrview_load),
    path('adm_viewapprvdbusns_load/',views.adm_viewapprvdbusns_load),
    path('adm_blk_bussiness/<str:cid>',views.adm_blk_bussiness),
    path('adm_viewcmpnlt_load/', views.adm_viewcmpnlt_load),
    path('adm_search_load/',views.adm_search_load),

    path('adm_viewtourstplce_load/',views.adm_viewtourstplce_load),
    path('adm_delete_touristplace/<str:cid>',views.adm_delete_touristplace),
    path('adm_aprovd_bussiness/<str:cid>',views.adm_aprovd_bussiness),
    path('adm_rejct_bussiness/<str:cid>',views.adm_rejct_bussiness),

    ######      admin post
    path('login_post/', views.login_post),
    path('adm_addplce_post/',views.adm_addplce_post),
    path('adm_editplce_post/',views.adm_editplce_post),
    # path('adm_Bussines_post/', views.adm_Bussines_post),
    path('adm_ChngePaswrd_post/', views.adm_ChngePaswrd_post),
    # path('adm_fedbck_post/', views.adm_fedbck_post),
    # path('adm_rtingandview_post/', views.adm_rtingandview_post),
    path('adm_sndrply_post/', views.adm_sndrply_post),
    # path('adm_usrview_post/', views.adm_usrview_post),
    # path('adm_viewapprvdbusns_post/',views.adm_viewapprvdbusns_post),
    # path('adm_viewcmpnlt_post/', views.adm_viewcmpnlt_post),
    # path('adm_viewtourstplce_post/', views.adm_viewtourstplce_post),



    #...............bussness load.........

    path('busns_ChngePaswrd_load/',views.busns_ChngePaswrd_load),
    path('busns_index_load/',views.busns_index_load),
    path('busns_signup1_load/',views.busns_signup1_load),
    path('busns_usrtble_load/<bid>/<pid>',views.busns_usrtble_load),
    path('busns_addofr_load/',views.busns_addofr_load),
    path('busns_addsrvc_load/', views.busns_addsrvc_load),
    path('busns_pckmngnt_load/', views.busns_pckmngnt_load),
    path('busns_srvcmngmnt_load/', views.busns_srvcmngmnt_load),
    path('busns_delete_srvcmngmnt/<str:cid>',views.busns_delete_srvcmngmnt),
    path('busns_editsrvcmngmnt_load/<str:id>',views.busns_editsrvcmngmnt_load),
    # path('busns_signup_load/', views.busns_signup_load),
    path('busns_vwpckg_load/',views.busns_vwpckg_load),
    path('busns_editpkge_load/<id>',views.busns_editpkge_load),
    path('busns_add_sub_package_load',views.busns_add_sub_package_load),
    path('busns_vwprfle_load/', views.busns_vwprfle_load),
    path('busns_vwcstmrpkg_load/',views.busns_vwcstmrpkg_load),
    path('busns_sendintrest/<cpid>',views.busns_sendintrest),
    path('busns_vwcmtdpkg_load/',views.busns_vwcmtdpkg_load),
    path('busns_vwpkgtbl_load/<pid>',views.busns_vwpkgtbl_load),
    path('busns_vwpndgbkg_load/',views.busns_vwpndgbkg_load),
    path('busns_vwusrtg_load/',views.busns_vwusrtg_load),
    path('busns_signup_post/', views.busns_signup_post),
    path('busns_vwpckgdel_load/<str:cid>',views.busns_vwpckgdel_load),
    path('busns_vwapprbkg_load/', views.busns_vwapprgbkg_load),
    path('busns_vwapprgbkg_loadpost/', views.busns_vwapprgbkg_loadpost),

    path('busns_app_usrtble_load/<bid>/<pid>', views.busns_app_usrtble_load),
    path('busns_offerdelet_load/<str:cid>',views.busns_offerdelet_load),
    path('busns_view_send_intrest/',views.busns_view_send_intrest),
    path('busns_fedbck_load/',views.busns_fedbck_load),
    path('busns_viewcmpnlt_load/',views.busns_viewcmpnlt_load),





    ##############        bussiness post
    path('busns_ChngePaswrd_post/', views.busns_ChngePaswrd_post),
    path('busns_addsrvc_post/', views.busns_addsrvc_post),
    path('busns_pckmngnt_post/', views.busns_pckmngnt_post),
    path('busns_editpkge_post/',views.busns_editpkge_post),
    # path('busns_srvcmngmnt_post/', views.busns_srvcmngmnt_post),
    path('busns_editsrvcmngmnt_post/',views.busns_editsrvcmngmnt_post),
    path('busns_signup_post/', views.busns_signup_post),
    # path('busns_vwpckg_post/', views.busns_vwpckg_post),
    path('busns_vwpkgtbl_post/',views.busns_vwpkgtbl_post),
    path('busns_subpackage_del/<str:psid>/<pid>',views.busns_subpackage_del),
    path('busns_vwprfle_post/', views.busns_vwprfle_post),
    path('busns_addofr_post/',views.busns_addofr_post),
    path('busns_add_sub_package_post/',views.busns_add_sub_package_post),
    path('busns_sendintrest_post/',views.busns_sendintrest_post),
    path('busns_vwpndgaccpt_post/',views.busns_vwpndgaccpt_post),
    path('busns_vwpndg_post/',views.busns_vwpndgbkg_post),
    path('busns_vwapprbkg_post/',views.busns_vwapprbkg_post),
    path('busns_chat_load/',views.busns_chat_load),
    path('busnsviewmsg/<receiverid>',views.busnsviewmsg),
    path('chatview/',views.chatview),
    path('bussiness_insert_chat/<receiverid>/<msg>',views.bussiness_insert_chat),




#..............................user load................................

    path('user_ChngePaswrd_load/',views.user_ChngePaswrd_load),
    path('user_signup_load/',views.user_signup_load),
    path('user_home_load/',views.user_home_load),
    path('user_viewtourstplce_load/',views.user_viewtourstplce_load),
    path('user_Bussines_load/',views.user_Bussines_load),
    path('user_feedback_load/',views.user_feedback_load),
    path('user_complaint_load/',views.user_complaint_load),
    path('user_offer_load/',views.user_offer_load),
    path('user_view_package_load/<str:id>',views.user_view_package_load),
    path('user_view_service/<str:id>',views.user_view_service),
    path('user_view_complaint_load/',views.user_view_complaint_load),
    path('user_view_profile/',views.user_view_profile),
    path('user_booking_load/<str:id>',views.user_booking_load),
    path('user_sendcustom_package_load/',views.user_sendcustom_package_load),
    path('user_view_custm_package_load/',views.user_view_custm_package_load),
    path('user_view_intrest_load/<cpid>',views.user_view_intrest_load),
    path('user_accept_intrest_load/<intrest_id>/<cpid>',views.user_accept_intrest_load),
    path('user_reject_intrest_load/<intrest_id>/<cpid>',views.user_reject_intrest_load),
    path('user_more_package_load/<str:id>',views.user_more_package_load),
    path('user_view_history_load/',views.user_view_history_load),
    path('user_add_rating_load/<int:id>',views.user_add_rating_load),
    path('user_view_rating_load/',views.user_view_rating_load),

#...........................user post................
    path('user_ChngePaswrd_post/',views.user_ChngePaswrd_post),
    path('user_signup_post/',views.user_signup_post),
    path('user_feedback_post/',views. user_feedback_post),
    path('user_complaint_post/',views.user_complaint_post),
    path('user_view_profile_post/',views.user_view_profile_post),
    path('user_sendcustom_package_post/',views.user_sendcustom_package_post),
    path('user_add_rating_post/',views.user_add_rating_post),


    path('user_chat_load/',views.user_chat_load),
    path('userviewmsg/<receiverid>',views.userviewmsg),
    path('userchatview/',views.userchatview),
    path('user_insert_chat/<receiverid>/<msg>',views.user_insert_chat),


#............................public load...............

    path('public_viewtourstplce_load/',views.public_viewtourstplce_load),

    path('public_veiwbussunes_load/',views.public_veiwbussunes_load),
    path('public_veiwservc_load/',views.public_veiwservc_load),
    path('public_viewratg_load/',views.public_viewratg_load),
    path('public_mainhome_load/',views.public_mainhome_load),

#..................................public post..........................................


    path('public_searching_post/',views.public_searching_post),



    ]
