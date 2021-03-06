---
title: DateTimeFormatter.parseUnresolved()
permalink: /Java/DateTimeFormatter/parseUnresolved/
date: 2021-01-11
key: Java.D.DateTimeFormatter
category: Java
tags: ['java se', 'java.time.format', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeFormatter.metodos valor="parseUnresolved" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TemporalAccessor parseUnresolved(CharSequence text, ParsePosition position)
~~~

## Parámetros
* **CharSequence text**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence text" %}
* **ParsePosition position**,  {% include w3api/param_description.html metodo=_dato parametro="ParsePosition position" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [DateTimeException](/Java/DateTimeException/)

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
