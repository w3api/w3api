---
title: AudioInputStream.AudioInputStream()
permalink: Java/AudioInputStream/AudioInputStream
date: 2021-01-04
key: JavaJava.A.AudioInputStream
category: java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioInputStream.constructores valor="AudioInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AudioInputStream(InputStream stream, AudioFormat format, long length)
public AudioInputStream(TargetDataLine line)
~~~

## Parámetros
* **TargetDataLine line**,  {% include w3api/param_description.html metodo=_data parametro="TargetDataLine line" %}
* **InputStream stream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream stream" %}
* **AudioFormat format**,  {% include w3api/param_description.html metodo=_data parametro="AudioFormat format" %}
* **long length**,  {% include w3api/param_description.html metodo=_data parametro="long length" %}

## Clase Padre
[AudioInputStream](/Java/AudioInputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AudioInputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
