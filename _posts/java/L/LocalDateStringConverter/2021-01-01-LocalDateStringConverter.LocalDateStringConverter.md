---
title: LocalDateStringConverter.LocalDateStringConverter()
permalink: Java/LocalDateStringConverter/LocalDateStringConverter
date: 2021-01-11
key: Java.L.LocalDateStringConverter
category: java
tags: ['java se', 'javafx.util.converter', 'javafx.base', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDateStringConverter.constructores valor="LocalDateStringConverter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LocalDateStringConverter()
public LocalDateStringConverter(DateTimeFormatter formatter, DateTimeFormatter parser)
public LocalDateStringConverter(FormatStyle dateStyle)
public LocalDateStringConverter(FormatStyle dateStyle, Locale locale, Chronology chronology)
~~~

## Parámetros
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}
* **Chronology chronology**,  {% include w3api/param_description.html metodo=_dato parametro="Chronology chronology" %}
* **DateTimeFormatter parser**,  {% include w3api/param_description.html metodo=_dato parametro="DateTimeFormatter parser" %}
* **DateTimeFormatter formatter**,  {% include w3api/param_description.html metodo=_dato parametro="DateTimeFormatter formatter" %}
* **FormatStyle dateStyle**,  {% include w3api/param_description.html metodo=_dato parametro="FormatStyle dateStyle" %}

## Clase Padre
[LocalDateStringConverter](/Java/LocalDateStringConverter/)

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
