---
title: AudioSystem.getAudioFileFormat()
permalink: Java/AudioSystem/getAudioFileFormat
date: 2021-01-04
key: JavaJava.A.AudioSystem
category: java
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
* **URL url**,  {% include w3api/param_description.html metodo=_data parametro="URL url" %}
* **InputStream stream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream stream" %}
* **File file**,  {% include w3api/param_description.html metodo=_data parametro="File file" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [UnsupportedAudioFileException](/Java/UnsupportedAudioFileException/), [IOException](/Java/IOException/)

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
