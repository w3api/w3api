---
title: DateTimeFormatterBuilder.appendValue()
permalink: Java/DateTimeFormatterBuilder/appendValue
date: 2021-01-11
key: JavaJava.D.DateTimeFormatterBuilder
category: java
tags: ['java se', 'java.time.format', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeFormatterBuilder.metodos valor="appendValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DateTimeFormatterBuilder appendValue(TemporalField field)
public DateTimeFormatterBuilder appendValue(TemporalField field, int width)
public DateTimeFormatterBuilder appendValue(TemporalField field, int minWidth, int maxWidth, SignStyle signStyle)
~~~

## Parámetros
* **SignStyle signStyle**,  {% include w3api/param_description.html metodo=_dato parametro="SignStyle signStyle" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}
* **int minWidth**,  {% include w3api/param_description.html metodo=_dato parametro="int minWidth" %}
* **int maxWidth**,  {% include w3api/param_description.html metodo=_dato parametro="int maxWidth" %}
* **TemporalField field**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalField field" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DateTimeFormatterBuilder](/Java/DateTimeFormatterBuilder/)

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
