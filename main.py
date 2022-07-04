try:
    import random, os, threading, time, requests, sys
    from pystyle import *
except Exception as e:
    print(f'ERROR [{e}]')


class Main():
    try:
        def download(url, author):
            """
            Téléchargemement des vidéos
            :param url:
            :param author:
            :return:
            """
            global x, videocount

            try:
                with open(f'./video/@{author}/{random.randint(1000, 9999)}.mp4', 'wb') as out_file:
                    videobytes = requests.get(f'{url}.mp4', stream=True)
                    out_file.write(videobytes.content)
                    x += 1
                    os.system(f"title TikTok Downloader ^| TKLT_CatChef#9825 ^| Téléchargé: {x} ^| Dossier: ./video/@{author}")
            except:
                pass


        def start():
            global x
            """
            main function
            """

            os.system('cls' if os.name == 'nt' else "clear")
            os.system(f"title TikTok Downloader ^| TKLT_CatChef#9825 ^| STATUS: LOADING")

            banner = """
                ZZZZZZZZZZZZZZZZZZZZZ
              ZZZZZ______________ZZZZZZ
            ZZZZZ____________________ZZZZ
          ZZZZZ_______________________ZZZZZ
        ZZZZZ___________________________ZZZZ
       ZZZZ______________________________ZZZZ
      ZZZ__________________________________ZZZ
     ZZZ____________________________________ZZZ
    ZZZZ____________________________________ZZZ
    ZZZ_____________________________________ZZZ
    ZZZ_____________________________________ZZZ
    ZZZ_____________________________________ZZZ
    ZZZ_____________________________ZZ______ZZZ
    ZZZ___________________________ZZZZZ_____ZZZ
    ZZZ________________________ZZZZZZZZZ__ZZZZZ
    ZZZZ____ZZZ______________ZZZZZZZZZZZZ_ZZZZ
    ZZZZ___ZZZZZZ___________ZZZZZZZZZZZZZ_ZZZ
    ZZZZ__ZZZZZZZZZZ_______ZZZZZZZZZZZZZ__ZZ
    ZZZZ__ZZZZZZZZZZZ______ZZZZZZZZZZZZ___ZZ
     ZZZ___ZZZZZZZZZZZ______ZZZZZZZZZZ____ZZ
     ZZZ____ZZZZZZZZZ_ZZZZZ___ZZZZZZ____ZZZZ
      ZZZ____ZZZZZZZ__ZZZZZZ___________ZZZZ
       ZZZZZ__________Z__ZZZ_____ZZZZZZZZZ
        ZZZZZZZZ__________ZZ____ZZZZZZZZ
         ZZZZZZZZ_____________ZZZZZ
              ZZZ__Z___Z___Z__ZZZ
              ZZZ_ZZZ_ZZZ_ZZZ_ZZZ
              ZZZ_ZZZ_ZZZ_ZZZ_ZZZ
              ZZZ_ZZZ_ZZZ_ZZZ_ZZZ
               ZZZZZZZZZZZZZZZZZ
                  ZZZZZZZZZZZ                                 
            """
            TikTokDownloaderBanner = """

####### *        #######                  #######                                                                                                                                   
   #      #    #    #     ####  #    #    #     #  ####  #    # #    # #       ####    ##   #####  ###### #####  
   #    # #   #     #    #    # #   #     #     # #    # #    # ##   # #      #    #  #  #  #    # #      #    # 
   #    # ####      #    #    # ####      #     # #    # #    # # #  # #      #    # #    # #    # #####  #    # 
   #    # #  #      #    #    # #  #      #     # #    # # ## # #  # # #      #    # ###### #    # #      #####  
   #    # #   #     #    #    # #   #     #     # #    # ##  ## #   ## #      #    # #    # #    # #      #   #  
   #    # #    #    #     ####  #    #    ######   ####  #    # #    # ######  ####  #    # #####  ###### #    # 
                                                                                                                 

            """
            MyBanner= """

                ######                   ####### #    # #       #######   
                #     #   ##   #####        #    #   #  #          #      
                #     #  #  #  #    #       #    #  #   #          #      
                ######  #    # #    #       #    ###    #          #      
                #       ###### #####        #    #  #   #          #      
                #       #    # #   #        #    #   #  #          #      
                #       #    # #    #       #    #    # #######    #      
                ####################################################                                                 
                                  TKLT_CatChef#9825           

            """
            Anime.Fade(Center.Center(banner), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=3)
            Anime.Fade(Center.Center(TikTokDownloaderBanner), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=3)
            Anime.Fade(Center.Center(MyBanner), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=3)
            Anime.Fade(Center.Center("L'id est l'id d'une vidéo du compte dont vous voulez téléchargé les vidéos."), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=5)

            user = Write.Input(Center.Center("id > "), Colors.blue_to_red, interval=0)

            os.system('cls' if os.name == 'nt' else "clear")
            print(Colorate.Vertical(Colors.blue_to_red, Center.Center("Téléchargement...")))
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
            }
            author = requests.get(f"https://api.tiktokv.com/aweme/v1/multi/aweme/detail/?aweme_ids=%5B{user}%5D", headers=headers).json()['aweme_details'][0]["author"]['unique_id']
            if not os.path.exists(f'video'):
                os.makedirs(f'video')
            if not os.path.exists(f'video/@{author}'):
                os.makedirs(f'video/@{author}')
            

            secUid = requests.get(f"https://api.tiktokv.com/aweme/v1/multi/aweme/detail/?aweme_ids=%5B{user}%5D", headers=headers).json()['aweme_details'][0]["author"]["sec_uid"]
            max_cursor = "0"
            x = 0

            while True:
                try:


                    url = f"https://api16-core-c-useast1a.tiktokv.com/aweme/v1/aweme/post/?sec_user_id={secUid}&count=33&device_id=9999999999999999999&max_cursor={max_cursor}&aid=1180"
                    headers = {
                        "accept-encoding": "gzip",
                        "user-agent": "com.ss.android.ugc.trill/240303 (Linux; U; Android 12; en_US; Pixel 6 Pro; Build/SP2A.220405.004;tt-ok/3.10.0.2)",
                        "x-gorgon": "0"
                    }
                    response = requests.request("GET", url, headers=headers)
                    try:
                        if response.json()["status_msg"] == "No more videos":
                            break
                    except:
                        try:
                            max_cursor = response.json()["max_cursor"]
                        except:
                            break

                    videos = response.json()["aweme_list"]

                    for vid in videos:
                        
                        url = vid["video"]["play_addr"]["url_list"][0]
                        threading.Thread(target=Main.download, args=(url, author,)).start()
                except:
                    print(Colorate.Vertical(Colors.blue_to_red, Center.Center("FINISHED...")))
                    break

    except Exception as e:
        os.system('cls' if os.name == 'nt' else "clear")
        print(f'ERROR {e}')
        input()
        sys.exit()


if __name__ == '__main__':
    Main.start()
