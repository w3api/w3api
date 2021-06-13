---
title: DateTimeFormatterBuilder.appendValueReduced()
permalink: /Java/DateTimeFormatterBuilder/appendValueReduced/
date: 2021-01-11
key: Java.D.DateTimeFormatterBuilder
category: Java
tags: ['java se', 'java.time.format', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeFormatterBuilder.metodos valor="appendValueReduced" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DateTimeFormatterBuilder appendValueReduced(TemporalField field, int width, int maxWidth, int baseValue)
public DateTimeFormatterBuilder appendValueReduced(TemporalField field, int width, int maxWidth, ChronoLocalDate baseDate)
~~~

## Parámetros
* **ChronoLocalDate baseDate**,  {% include w3api/param_description.html metodo=_dato parametro="ChronoLocalDate baseDate" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}
* **int baseValue**,  {% include w3api/param_description.html metodo=_dato parametro="int baseValue" %}
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
