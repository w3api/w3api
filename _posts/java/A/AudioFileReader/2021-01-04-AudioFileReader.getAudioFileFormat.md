---
title: AudioFileReader.getAudioFileFormat()
permalink: Java/AudioFileReader/getAudioFileFormat
date: 2021-01-04
key: JavaJava.A.AudioFileReader
category: java
tags: ['java se', 'javax.sound.sampled.spi', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioFileReader.metodos valor="getAudioFileFormat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract AudioFileFormat getAudioFileFormat(File file) throws UnsupportedAudioFileException, IOException
public abstract AudioFileFormat getAudioFileFormat(InputStream stream) throws UnsupportedAudioFileException, IOException
public abstract AudioFileFormat getAudioFileFormat(URL url) throws UnsupportedAudioFileException, IOException
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_data parametro="URL url" %}
* **InputStream stream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream stream" %}
* **File file**,  {% include w3api/param_description.html metodo=_data parametro="File file" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [UnsupportedAudioFileException](/Java/UnsupportedAudioFileException/), [IOException](/Java/IOException/)

## Clase Padre
[AudioFileReader](/Java/AudioFileReader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AudioFileReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
