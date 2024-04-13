---
title: AudioFileWriter.write()
permalink: /Java/AudioFileWriter/write/
date: 2021-01-11
key: Java.A.AudioFileWriter
category: Java
tags: ['java se', 'javax.sound.sampled.spi', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioFileWriter.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int write(AudioInputStream stream, AudioFileFormat.Type fileType, File out) throws IOException
public abstract int write(AudioInputStream stream, AudioFileFormat.Type fileType, OutputStream out) throws IOException
~~~

## Parámetros
* **AudioFileFormat.Type fileType**,  {% include w3api/param_description.html metodo=_dato parametro="AudioFileFormat.Type fileType" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream out" %}
* **File out**,  {% include w3api/param_description.html metodo=_dato parametro="File out" %}
* **AudioInputStream stream**,  {% include w3api/param_description.html metodo=_dato parametro="AudioInputStream stream" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

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
