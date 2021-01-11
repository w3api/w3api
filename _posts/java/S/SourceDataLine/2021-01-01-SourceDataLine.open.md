---
title: SourceDataLine.open()
permalink: Java/SourceDataLine/open
date: 2021-01-11
key: JavaJava.S.SourceDataLine
category: java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SourceDataLine.metodos valor="open" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void open(AudioFormat format) throws LineUnavailableException
void open(AudioFormat format, int bufferSize) throws LineUnavailableException
~~~

## Parámetros
* **AudioFormat format**,  {% include w3api/param_description.html metodo=_dato parametro="AudioFormat format" %}
* **int bufferSize**,  {% include w3api/param_description.html metodo=_dato parametro="int bufferSize" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [LineUnavailableException](/Java/LineUnavailableException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[SourceDataLine](/Java/SourceDataLine/)

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
