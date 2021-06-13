---
title: AudioSystem.getAudioFileFormat()
permalink: /Java/AudioSystem/getAudioFileFormat/
date: 2021-01-11
key: Java.A.AudioSystem
category: Java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioSystem.metodos valor="getAudioFileFormat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static AudioFileFormat getAudioFileFormat(File file) throws UnsupportedAudioFileException, IOException
public static AudioFileFormat getAudioFileFormat(InputStream stream) throws UnsupportedAudioFileException, IOException
public static AudioFileFormat getAudioFileFormat(URL url) throws UnsupportedAudioFileException, IOException
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
* **File file**,  {% include w3api/param_description.html metodo=_dato parametro="File file" %}
* **InputStream stream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream stream" %}

## Excepciones
[UnsupportedAudioFileException](/Java/UnsupportedAudioFileException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

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
