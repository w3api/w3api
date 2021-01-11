---
title: AudioFormat.AudioFormat()
permalink: Java/AudioFormat/AudioFormat
date: 2021-01-11
key: JavaJava.A.AudioFormat
category: java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioFormat.constructores valor="AudioFormat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AudioFormat(float sampleRate, int sampleSizeInBits, int channels, boolean signed, boolean bigEndian)
public AudioFormat(AudioFormat.Encoding encoding, float sampleRate, int sampleSizeInBits, int channels, int frameSize, float frameRate, boolean bigEndian)
public AudioFormat(AudioFormat.Encoding encoding, float sampleRate, int sampleSizeInBits, int channels, int frameSize, float frameRate, boolean bigEndian, Map<String,Object> properties)
~~~

## Parámetros
* **float frameRate**,  {% include w3api/param_description.html metodo=_dato parametro="float frameRate" %}
* **int channels**,  {% include w3api/param_description.html metodo=_dato parametro="int channels" %}
* **boolean signed**,  {% include w3api/param_description.html metodo=_dato parametro="boolean signed" %}
* **int frameSize**,  {% include w3api/param_description.html metodo=_dato parametro="int frameSize" %}
* **float sampleRate**,  {% include w3api/param_description.html metodo=_dato parametro="float sampleRate" %}
* **AudioFormat.Encoding encoding**,  {% include w3api/param_description.html metodo=_dato parametro="AudioFormat.Encoding encoding" %}
* **Object&gt; properties**,  {% include w3api/param_description.html metodo=_dato parametro="Object> properties" %}
* **boolean bigEndian**,  {% include w3api/param_description.html metodo=_dato parametro="boolean bigEndian" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **int sampleSizeInBits**,  {% include w3api/param_description.html metodo=_dato parametro="int sampleSizeInBits" %}

## Clase Padre
[AudioFormat](/Java/AudioFormat/)

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
