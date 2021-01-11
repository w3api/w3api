---
title: DateTimeFormatterBuilder.getLocalizedDateTimePattern()
permalink: Java/DateTimeFormatterBuilder/getLocalizedDateTimePattern
date: 2021-01-11
key: JavaJava.D.DateTimeFormatterBuilder
category: java
tags: ['java se', 'java.time.format', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeFormatterBuilder.metodos valor="getLocalizedDateTimePattern" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static String getLocalizedDateTimePattern(FormatStyle dateStyle, FormatStyle timeStyle, Chronology chrono, Locale locale)
~~~

## Parámetros
* **FormatStyle timeStyle**,  {% include w3api/param_description.html metodo=_dato parametro="FormatStyle timeStyle" %}
* **FormatStyle dateStyle**,  {% include w3api/param_description.html metodo=_dato parametro="FormatStyle dateStyle" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}
* **Chronology chrono**,  {% include w3api/param_description.html metodo=_dato parametro="Chronology chrono" %}

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
