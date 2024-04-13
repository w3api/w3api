---
title: AudioFileWriter.getAudioFileTypes()
permalink: /Java/AudioFileWriter/getAudioFileTypes/
date: 2021-01-11
key: Java.A.AudioFileWriter
category: Java
tags: ['java se', 'javax.sound.sampled.spi', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioFileWriter.metodos valor="getAudioFileTypes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract AudioFileFormat.Type[] getAudioFileTypes()
public abstract AudioFileFormat.Type[] getAudioFileTypes(AudioInputStream stream)
~~~

## Parámetros
* **AudioInputStream stream**,  {% include w3api/param_description.html metodo=_dato parametro="AudioInputStream stream" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AudioFileWriter](/Java/AudioFileWriter/)

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
