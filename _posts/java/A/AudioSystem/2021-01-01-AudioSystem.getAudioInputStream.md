---
title: AudioSystem.getAudioInputStream()
permalink: Java/AudioSystem/getAudioInputStream
date: 2021-01-11
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
* **File file**,  {% include w3api/param_description.html metodo=_dato parametro="File file" %}
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
* **InputStream stream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream stream" %}
* **AudioFormat targetFormat**,  {% include w3api/param_description.html metodo=_dato parametro="AudioFormat targetFormat" %}
* **AudioFormat.Encoding targetEncoding**,  {% include w3api/param_description.html metodo=_dato parametro="AudioFormat.Encoding targetEncoding" %}
* **AudioInputStream sourceStream**,  {% include w3api/param_description.html metodo=_dato parametro="AudioInputStream sourceStream" %}

## Excepciones
[UnsupportedAudioFileException](/Java/UnsupportedAudioFileException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[AudioSystem](/Java/AudioSystem/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
