---
title: AudioSystem.getAudioInputStream()
permalink: Java/AudioSystem/getAudioInputStream
date: 2021-01-04
key: JavaJava.A.AudioSystem
category: java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioSystem.metodos valor="getAudioInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static AudioInputStream getAudioInputStream(File file) throws UnsupportedAudioFileException, IOException
public static AudioInputStream getAudioInputStream(InputStream stream) throws UnsupportedAudioFileException, IOException
public static AudioInputStream getAudioInputStream(URL url) throws UnsupportedAudioFileException, IOException
public static AudioInputStream getAudioInputStream(AudioFormat.Encoding targetEncoding, AudioInputStream sourceStream)
public static AudioInputStream getAudioInputStream(AudioFormat targetFormat, AudioInputStream sourceStream)
~~~

## Parámetros
* **InputStream stream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream stream" %}
* **AudioFormat targetFormat**,  {% include w3api/param_description.html metodo=_data parametro="AudioFormat targetFormat" %}
* **URL url**,  {% include w3api/param_description.html metodo=_data parametro="URL url" %}
* **AudioFormat.Encoding targetEncoding**,  {% include w3api/param_description.html metodo=_data parametro="AudioFormat.Encoding targetEncoding" %}
* **AudioInputStream sourceStream**,  {% include w3api/param_description.html metodo=_data parametro="AudioInputStream sourceStream" %}
* **File file**,  {% include w3api/param_description.html metodo=_data parametro="File file" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedAudioFileException](/Java/UnsupportedAudioFileException/), [IOException](/Java/IOException/)

## Clase Padre
[AudioSystem](/Java/AudioSystem/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AudioSystem.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
