---
title: AudioSystem.getLine()
permalink: Java/AudioSystem/getLine
date: 2021-01-04
key: JavaJava.A.AudioSystem
category: java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioSystem.metodos valor="getLine" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Line getLine(Line.Info info) throws LineUnavailableException
~~~

## Parámetros
* **Line.Info info**,  {% include w3api/param_description.html metodo=_data parametro="Line.Info info" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [LineUnavailableException](/Java/LineUnavailableException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AudioSystem](/Java/AudioSystem/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AudioSystem.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
