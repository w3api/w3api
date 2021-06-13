---
title: OffsetTime.of()
permalink: /Java/OffsetTime/of/
date: 2021-01-11
key: JavaJava.O.OffsetTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OffsetTime.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static OffsetTime of(int hour, int minute, int second, int nanoOfSecond, ZoneOffset offset)
public static OffsetTime of(LocalTime time, ZoneOffset offset)
~~~

## Parámetros
* **ZoneOffset offset**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneOffset offset" %}
* **int second**,  {% include w3api/param_description.html metodo=_dato parametro="int second" %}
* **int minute**,  {% include w3api/param_description.html metodo=_dato parametro="int minute" %}
* **int nanoOfSecond**,  {% include w3api/param_description.html metodo=_dato parametro="int nanoOfSecond" %}
* **LocalTime time**,  {% include w3api/param_description.html metodo=_dato parametro="LocalTime time" %}
* **int hour**,  {% include w3api/param_description.html metodo=_dato parametro="int hour" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[OffsetTime](/Java/OffsetTime/)

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
