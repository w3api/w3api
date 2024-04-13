---
title: AudioInputStream.AudioInputStream()
permalink: /Java/AudioInputStream/AudioInputStream/
date: 2021-01-11
key: Java.A.AudioInputStream
category: Java
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
* **TargetDataLine line**,  {% include w3api/param_description.html metodo=_dato parametro="TargetDataLine line" %}
* **long length**,  {% include w3api/param_description.html metodo=_dato parametro="long length" %}
* **AudioFormat format**,  {% include w3api/param_description.html metodo=_dato parametro="AudioFormat format" %}
* **InputStream stream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream stream" %}

## Clase Padre
[AudioInputStream](/Java/AudioInputStream/)

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
