---
title: TargetDataLine.open()
permalink: Java/TargetDataLine/open
date: 2021-01-04
key: JavaJava.T.TargetDataLine
category: java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TargetDataLine.metodos valor="open" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void open(AudioFormat format) throws LineUnavailableException
void open(AudioFormat format, int bufferSize) throws LineUnavailableException
~~~

## Parámetros
* **AudioFormat format**,  {% include w3api/param_description.html metodo=_data parametro="AudioFormat format" %}
* **int bufferSize**,  {% include w3api/param_description.html metodo=_data parametro="int bufferSize" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalStateException](/Java/IllegalStateException/), [LineUnavailableException](/Java/LineUnavailableException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[TargetDataLine](/Java/TargetDataLine/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TargetDataLine.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
