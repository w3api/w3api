---
title: AudioFileWriter.isFileTypeSupported()
permalink: Java/AudioFileWriter/isFileTypeSupported
date: 2021-01-04
key: JavaJava.A.AudioFileWriter
category: java
tags: ['java se', 'javax.sound.sampled.spi', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioFileWriter.metodos valor="isFileTypeSupported" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean isFileTypeSupported(AudioFileFormat.Type fileType)
public boolean isFileTypeSupported(AudioFileFormat.Type fileType, AudioInputStream stream)
~~~

## Parámetros
* **AudioInputStream stream**,  {% include w3api/param_description.html metodo=_data parametro="AudioInputStream stream" %}
* **AudioFileFormat.Type fileType**,  {% include w3api/param_description.html metodo=_data parametro="AudioFileFormat.Type fileType" %}

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
{%- for _ldc in site.data.Java.A.AudioFileWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
