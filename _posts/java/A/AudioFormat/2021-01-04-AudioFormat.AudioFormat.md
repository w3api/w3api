---
title: AudioFormat.AudioFormat()
permalink: Java/AudioFormat/AudioFormat
date: 2021-01-04
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
* **boolean signed**,  {% include w3api/param_description.html metodo=_data parametro="boolean signed" %}
* **int frameSize**,  {% include w3api/param_description.html metodo=_data parametro="int frameSize" %}
* **float frameRate**,  {% include w3api/param_description.html metodo=_data parametro="float frameRate" %}
* **Object&gt; properties**,  {% include w3api/param_description.html metodo=_data parametro="Object> properties" %}
* **float sampleRate**,  {% include w3api/param_description.html metodo=_data parametro="float sampleRate" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **int sampleSizeInBits**,  {% include w3api/param_description.html metodo=_data parametro="int sampleSizeInBits" %}
* **AudioFormat.Encoding encoding**,  {% include w3api/param_description.html metodo=_data parametro="AudioFormat.Encoding encoding" %}
* **int channels**,  {% include w3api/param_description.html metodo=_data parametro="int channels" %}
* **boolean bigEndian**,  {% include w3api/param_description.html metodo=_data parametro="boolean bigEndian" %}

## Clase Padre
[AudioFormat](/Java/AudioFormat/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AudioFormat.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
