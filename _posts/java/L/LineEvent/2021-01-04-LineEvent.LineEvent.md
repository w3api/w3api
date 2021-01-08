---
title: LineEvent.LineEvent()
permalink: Java/LineEvent/LineEvent
date: 2021-01-04
key: JavaJava.L.LineEvent
category: java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LineEvent.constructores valor="LineEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LineEvent(Line line, LineEvent.Type type, long position)
~~~

## Parámetros
* **long position**,  {% include w3api/param_description.html metodo=_data parametro="long position" %}
* **Line line**,  {% include w3api/param_description.html metodo=_data parametro="Line line" %}
* **LineEvent.Type type**,  {% include w3api/param_description.html metodo=_data parametro="LineEvent.Type type" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[LineEvent](/Java/LineEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LineEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
