---
title: AudioFileFormat.AudioFileFormat()
permalink: Java/AudioFileFormat/AudioFileFormat
date: 2021-01-04
key: JavaJava.A.AudioFileFormat
category: java
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
* **AudioFormat format**,  {% include w3api/param_description.html metodo=_data parametro="AudioFormat format" %}
* **Object&gt; properties**,  {% include w3api/param_description.html metodo=_data parametro="Object> properties" %}
* **int frameLength**,  {% include w3api/param_description.html metodo=_data parametro="int frameLength" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **int byteLength**,  {% include w3api/param_description.html metodo=_data parametro="int byteLength" %}
* **AudioFileFormat.Type type**,  {% include w3api/param_description.html metodo=_data parametro="AudioFileFormat.Type type" %}

## Clase Padre
[AudioFileFormat](/Java/AudioFileFormat/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AudioFileFormat.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
