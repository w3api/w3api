---
title: LocalTime.of()
permalink: Java/LocalTime/of
date: 2021-01-04
key: JavaJava.L.LocalTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalTime.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static LocalTime of(int hour, int minute)
public static LocalTime of(int hour, int minute, int second)
public static LocalTime of(int hour, int minute, int second, int nanoOfSecond)
~~~

## Parámetros
* **int hour**,  {% include w3api/param_description.html metodo=_data parametro="int hour" %}
* **int nanoOfSecond**,  {% include w3api/param_description.html metodo=_data parametro="int nanoOfSecond" %}
* **int second**,  {% include w3api/param_description.html metodo=_data parametro="int second" %}
* **int minute**,  {% include w3api/param_description.html metodo=_data parametro="int minute" %}

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
{%- for _ldc in site.data.Java.L.LocalTime.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
