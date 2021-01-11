---
title: AudioFileReader.getAudioInputStream()
permalink: Java/AudioFileReader/getAudioInputStream
date: 2021-01-11
key: JavaJava.A.AudioFileReader
category: java
tags: ['java se', 'javax.sound.sampled.spi', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioFileReader.metodos valor="getAudioInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract AudioInputStream getAudioInputStream(File file) throws UnsupportedAudioFileException, IOException
public abstract AudioInputStream getAudioInputStream(InputStream stream) throws UnsupportedAudioFileException, IOException
public abstract AudioInputStream getAudioInputStream(URL url) throws UnsupportedAudioFileException, IOException
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
* **File file**,  {% include w3api/param_description.html metodo=_dato parametro="File file" %}
* **InputStream stream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream stream" %}

## Excepciones
[UnsupportedAudioFileException](/Java/UnsupportedAudioFileException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[AudioFileReader](/Java/AudioFileReader/)

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
