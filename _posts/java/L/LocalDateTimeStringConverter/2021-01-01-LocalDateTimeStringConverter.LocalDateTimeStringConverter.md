---
title: LocalDateTimeStringConverter.LocalDateTimeStringConverter()
permalink: Java/LocalDateTimeStringConverter/LocalDateTimeStringConverter
date: 2021-01-11
key: JavaJava.L.LocalDateTimeStringConverter
category: java
tags: ['java se', 'javafx.util.converter', 'javafx.base', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDateTimeStringConverter.constructores valor="LocalDateTimeStringConverter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LocalDateTimeStringConverter()
public LocalDateTimeStringConverter(DateTimeFormatter formatter, DateTimeFormatter parser)
public LocalDateTimeStringConverter(FormatStyle dateStyle, FormatStyle timeStyle)
public LocalDateTimeStringConverter(FormatStyle dateStyle, FormatStyle timeStyle, Locale locale, Chronology chronology)
~~~

## Parámetros
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}
* **Chronology chronology**,  {% include w3api/param_description.html metodo=_dato parametro="Chronology chronology" %}
* **DateTimeFormatter parser**,  {% include w3api/param_description.html metodo=_dato parametro="DateTimeFormatter parser" %}
* **DateTimeFormatter formatter**,  {% include w3api/param_description.html metodo=_dato parametro="DateTimeFormatter formatter" %}
* **FormatStyle timeStyle**,  {% include w3api/param_description.html metodo=_dato parametro="FormatStyle timeStyle" %}
* **FormatStyle dateStyle**,  {% include w3api/param_description.html metodo=_dato parametro="FormatStyle dateStyle" %}

## Clase Padre
[LocalDateTimeStringConverter](/Java/LocalDateTimeStringConverter/)

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
