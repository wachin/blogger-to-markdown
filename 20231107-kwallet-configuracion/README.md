# Cómo configurar la cartera KWallet en KDE para Kubuntu, y en Sistemas Operativos no KDE para usar KDE Apps como Viper Browser

**Fuente:** https://facilitarelsoftwarelibre.blogspot.com/2023/11/como-configurar-la-cartera-kwallet-de-KDE.html

---

Le puse el título a esta entrada basado en dos circunstancias que me han sucedido:

**1er circunstancia.-** Había instalado [Debian 11 KDE](https://facilitarelsoftwarelibre.blogspot.com/2023/09/donde-descargar-debian-11-bullseye.html.html) y me apareció en un momento \(no recuerdo qué programa quise abrir\) una ventana pidiendome una contraseña del Servicio de cartera de KDE, y les cuento que hace varios años atrás cuando instalé Kubuntu para ver como era, me apareció esa ventana pero no sabía que hacer con ello \(y como no encontré ningún tutorial a la mano en el Sistema Operativo mismo, ni pude encontrar en internet, lo desinstalé e instaré otro Linux\), pero ahora si se que hay que hacer:

**2da. circunstancia.-** Instalé un Sistema Operativo no KDE, llamado MX Linux 21 \(<https://sourceforge.net/projects/mx-linux/files/Old/MX-21.3/Xfce/>\) la versión XFCE e instalé a Viper Browser \(sudo apt install viper-browser\), y al abrirlo me apareció el Servicio de cartera de KDE:

[![](images/image_001.webp)](https://blogger.googleusercontent.com/img/a/AVvXsEh-d5APzhd5AXRPUzNs4YAOpAdYHl28ynjCRuxxQ08VYkTHgygHHH0e6EX_YdwQQ6b9UmIb7pmgLPjO3iOF3X55b9x4iACK_U1KA6E2wUzEWHvCJGaW4WWeb9QHuu89pnJxgfBievaZ4g91LujJmp-H3QasYvXEKybnFrqK2WZZD-5EYIqv2yCrhde_xBA)

  
  


y bueno esta es la:

**Solución para la segunda circunstancia,** entonces tenemos que yo he abierto Viper Browser y apareció ese mensaje que dice:

La aplicación "**Viper-Broser** " ha solicidado crear una nueva carpeta con el nombre "**kdewallet** ". Esto se usa para almacenar información importante de un modo seguro. Escoja el nuevo tipo de cartera abajo, o pulse "Cancelar" si desea denegar la petición de la aplicación.

Elijo la segunda opción:

"Usar cifrado GPG, para una mejor protección"

y dejo esa ventana abierta sabiendo que se creará una nueva carpeta con el nombre "kdewallet", y pongo en la terminal:

  


### Crear GPG Key

Poner en la terminal:
    
    
    gpg --gen-key

aparecerá en la terminal. En la siguiente imagen yo he puesto mi nombre:

[![](images/image_002.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyTEyg31cnc5htmuiQrF_FFUuQiF8r2ynqyMwcsAzQA8_ls7E8NR2vYLT9LgXBwRNtU28NgDWKuS5nFQbQP_99_r9RG7jd2XRKj0MrsB2JriD4eDtsUuNBsR2hiSOq5Xd_OUV-sU28HfJLjkvAQkg8o6BDLCQ7LOJ7-KJf5IU06C0P7eMocIvG4WeEvuM/s827/20231106-193301%20creando%20la%20llave%20GPG,%20pondiendo%20mi%20nombre.png)   


y le doy enter  


luego el correo:

[![](images/image_003.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjTKqzLg1HXusGvVxlxSG40JoQAKPDVhSTZQuVNqjTT2mxudEueD5uaaWVef5gVrejjm8mQ5zhkkPseFqP7pXu_oz4EchSQQOLjl2iZYkR6jivyutcaQ5_Iww09WWxcqyMM9jrMOQswGgOhWrGS1hcz0C3RTtOOTB2Sdeuhpd9QJs8RQJpyhZhPrM0KE-U/s770/20231106-193648%20poniendo%20mi%20correo.png)

  


le digo que vale:

[![](images/image_004.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgeUmt9UEIla1Dmbk2IHqPZH2rqwUhjSy4LOdzGkdPUDVPTmlRiM2ghhXuqcoT04dW3xiSScYyUzu3AwCf7B8Osp3Ei4kmpLwc_VUx0pBkiIebOSPHhMN8zwah4T_oW9kNHIIcK3EgMBnyrXVLF3VnSRoBN1w8MiPPabFhq_RYxwCj-G-oVhmaurO4IvPU/s780/20231106-193930%20Vale.png)

  


luego escribiendo la frase de la contraseña para proteger su nueva clave, hay que escrbir una contraseña, **creela con letras mayusculas y minuscula, numeros \(y algún caracter dificil\)** , ejemplo yo la he creado algo así:

Lubuntu-587903920 

[![](images/image_005.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGsYN3F4G7qIAdi6qj8QwQWGnmj4r73kR2YLUfievEXE2SuiQfrsdLA9UX5AW0619v-yKPHE43FO2nCbdj4cu5omw4ntfnc9qWOYIPtmzzy43_n8ghHBmrhvxuJ6V93LfnPq3fRbRzYegOFlwNEIpV1dCDT0swj8r2lYhO5lq3vIkjRKDLiW8jFesQwzk/s777/20231106-194059%20escribiendo%20la%20frase%20de%20la%20contrase%C3%B1a%20para%20proteger%20su%20nueva%20clave.png)

  
  


pero esta ventana congela las demás ventanas \(sólo podrá usar esa\) así que aconsejo en un cuaderno escribir la contraseña \(o en su celular\) y luego escribirla en la ventana \(porque después se cierra y deberán repetir el proceso desde el inicio\):

y aparecerá así:

[![](images/image_006.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2xnfY8fpa89aK-PIHYUw0FZx2xqpZIWwkHaCglvDazyTWQD9erZC9SF3P24UezscI46AIMTb5oSGCMWgJtufABb94KblEjin1x3mLY036WURocjuDGdsvVmRXyqWIuP8oAksPrSdp9cMdvJQzl4TCQYRmhYOS0kmg40106qiOI3dIi1MPVhNH9bB5OOk/s778/20231106-194450%20la%20llave%20queda%20guardada%20en%20.gnupg.png)

  


Recuerde guardar sus datos. Ahora le doy **Siguiente** a la ventana:

[![](images/image_007.webp)](https://blogger.googleusercontent.com/img/a/AVvXsEiG_zjKogmeyX2p4YVxVzFAfIHXnKxxdlrXihaL08MAlBZ8nF0s65fr-IzxqxSt0X5rawjGjJu58xrAv9bvKK82-0bEFcgripe_qKvXqqkU1w0yOTBQOknfYrzyBUcMQMmsRhkarO0XiEQcMHSBNb4gREVWaBZz1yFrml3gn4D9avB6pFuAoqCAgqYhGGQ)

  
  


y automáticamente aparece seleccionada mi clave GPG:

[![](images/image_008.webp)](https://blogger.googleusercontent.com/img/a/AVvXsEi4RYZ-FRc3wcpJ9gAED-SFcaPkGR3dPtOSCFVIbfNztUstIJjwA1gELtW5m18vmU7q02fTP7JIouh1l6-PXzOXT20RCOfWKWQwdyBssN61ilS9pUuTXKekBoGTlVfN-K_2uUCi8u7m-dYGhm5aFJk5lJvrN-TpHm6aejsDgIF1B0vtPqyT3faO8EGPTSo)

  
  


  
doy clic en finalizar, y voy a buscar a Viper:

[![](images/image_009.webp)](https://blogger.googleusercontent.com/img/a/AVvXsEj1fC1D1yn0LNJtsY5tKeLwsuBZ_QqWh4yAiZcVt0vs9wgFZbIB03xlsBLv1vJ2qThIvFsRWPdjK6mMHHVA6xax-6ZS9_oCFxjDPipl_lwPI5_q5nbT1UyXMPRV7hLpQDs1dkRBThWjuCwKv8KcPmJgmoNfbcNRllTXEMYzH7fZzXBCcGIyH7vZc42rBec)

  
**  
**

**Nota** : Hay un momento en que le pedirá la contraseña de la cartera, parece que es aquí, debe ponerla

  


y al fin abierto:

[![](images/image_010.webp)](https://blogger.googleusercontent.com/img/a/AVvXsEgcb2LtBbmGKAbFEf9YeabspzO9jUfBTUoCFndpWBRt34o0y9StLt2SXHXoYMfNQXxCms3Lq1S9zyLzH-AMKigKNzziv9RguA3L3pAVuUwyYAI65tHaxxeXmIb2jBUW8FiNLy-lIClTpOp75zdhHj_CihJfAgpMgIkQwbSE8uBoLeVOeOGMrVsileRGFsY)

  
  


### Usando KWalletManager

En MX Linux 21 la versión XFCE no está instalado KWalletManager pero se lo puede instalar así:
    
    
    sudo apt install kwalletmanager
    

  


cabe notar que MX Linux tiene una versión KDE \(<https://sourceforge.net/projects/mx-linux/files/>\) y allí si está instalada, además de Kubuntu y otros Linux que usen KDE. Lo abrimos:

[![](images/image_011.webp)](https://blogger.googleusercontent.com/img/a/AVvXsEgzrClP9wUT9rOu4TjWd4xH5f-5zMaa6RGBVWaGoWWTHVyvLJfNiAPiDSmxnhuwGgQZgs5nfuaIs_08DpUvip82sHNnKKgypSTTiVY36onf-hVQqnL-O8FRwDHY81PRMAHzmHVfigR9NtXvJRZdGKrZA0lMDEVZbv7J-1Lcjhz6_S0pUARyFQyCCdwVk5Y)

  
vemos que la cartera se llama:

kdewallet

nombre el cual fue dado automáticamente:

[![](images/image_012.webp)](https://blogger.googleusercontent.com/img/a/AVvXsEgG9ituG1wmEKZxb3TEMavVQ9QL3pMUFJph8Z4Nm8bU5CtI-iaSVtmAHLYABSSx1y_nbdSN2agsIeqcW8pKiw8DniUsOpbL0LVLoGdfn3CEF6TWx5uZPZHFsHP_ixnVHSTyn1siHsAnx9DUs1Ga0IFIog5F7b1FuoHz7BnDWYOixqDg6vjtYN8Z1u_WXMI)

  
  


### Creando otra cartera con otro nombre

Si por alguna razón desea crear otra cartera, debe dar clic en:

Archivo - Nueva cartera

[![](images/image_013.webp)](https://blogger.googleusercontent.com/img/a/AVvXsEiwVev58V-yYnDAnReMiT7IosLYPNkYFPK8Ar1PjAjre4qt0RCFD_WQjwjX6CLP3t6QqFtbkn_mywEhYKh-C_P-LTu2EtocNaeyt3yF07IVuCwQPVlgM2v0OeRleu0RHrAkpRn2LueBedBbKv_A3G0OoyoDVBxxMXPA8FXbFW1bM8FU_2TACjEy5ES96V8)

  
y seguir los pasos

Yo creo que con toda esta información también se puede solucionar lo mismo que puede suceder en un Sistema Operativo Linux KDE, es que ahorita no tengo ninguno a la mano para hacer un tutorial 

Dios les bendiga

  


  


  

