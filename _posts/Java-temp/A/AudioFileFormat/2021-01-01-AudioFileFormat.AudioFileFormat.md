---
title: AudioFileFormat.AudioFileFormat()
permalink: /Java/AudioFileFormat/AudioFileFormat/
date: 2021-01-11
key: Java.A.AudioFileFormat
category: Java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioFileFormat.constructores valor="AudioFileFormat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected AudioFileFormat(AudioFileFormat.Type type, int byteLength, AudioFormat format, int frameLength)
public AudioFileFormat(AudioFileFormat.Type type, AudioFormat format, int frameLength)
public AudioFileFormat(AudioFileFormat.Type type, AudioFormat format, int frameLength, Map<String,Object> properties)
~~~

## Parámetros
* **int byteLength**,  {% include w3api/param_description.html metodo=_dato parametro="int byteLength" %}
* **AudioFileFormat.Type type**,  {% include w3api/param_description.html metodo=_dato parametro="AudioFileFormat.Type type" %}
* **int frameLength**,  {% include w3api/param_description.html metodo=_dato parametro="int frameLength" %}
* **Object&gt; properties**,  {% include w3api/param_description.html metodo=_dato parametro="Object> properties" %}
* **AudioFormat format**,  {% include w3api/param_description.html metodo=_dato parametro="AudioFormat format" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}

## Clase Padre
[AudioFileFormat](/Java/AudioFileFormat/)

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
