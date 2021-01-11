---
title: LocalTime.ofNanoOfDay()
permalink: Java/LocalTime/ofNanoOfDay
date: 2021-01-11
key: JavaJava.L.LocalTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalTime.metodos valor="ofNanoOfDay" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static LocalTime ofNanoOfDay(long nanoOfDay)
~~~

## Parámetros
* **long nanoOfDay**,  {% include w3api/param_description.html metodo=_dato parametro="long nanoOfDay" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[LocalTime](/Java/LocalTime/)

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
