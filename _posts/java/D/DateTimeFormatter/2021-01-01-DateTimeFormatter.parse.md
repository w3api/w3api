---
title: DateTimeFormatter.parse()
permalink: Java/DateTimeFormatter/parse
date: 2021-01-11
key: JavaJava.D.DateTimeFormatter
category: java
tags: ['java se', 'java.time.format', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeFormatter.metodos valor="parse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TemporalAccessor parse(CharSequence text)
public TemporalAccessor parse(CharSequence text, ParsePosition position)
<T> T parse(CharSequence text, TemporalQuery<T> query)
~~~

## Parámetros
* **CharSequence text**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence text" %}
* **ParsePosition position**,  {% include w3api/param_description.html metodo=_dato parametro="ParsePosition position" %}
* **TemporalQuery&lt;T&gt; query**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalQuery<T> query" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [DateTimeParseException](/Java/DateTimeParseException/)

## Clase Padre
[DateTimeFormatter](/Java/DateTimeFormatter/)

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
