---
title: DateTimeFormatterBuilder.getLocalizedDateTimePattern()
permalink: Java/DateTimeFormatterBuilder/getLocalizedDateTimePattern
date: 2021-01-04
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
* **Chronology chrono**,  {% include w3api/param_description.html metodo=_data parametro="Chronology chrono" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_data parametro="Locale locale" %}
* **FormatStyle dateStyle**,  {% include w3api/param_description.html metodo=_data parametro="FormatStyle dateStyle" %}
* **FormatStyle timeStyle**,  {% include w3api/param_description.html metodo=_data parametro="FormatStyle timeStyle" %}

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
{%- for _ldc in site.data.Java.D.DateTimeFormatterBuilder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
