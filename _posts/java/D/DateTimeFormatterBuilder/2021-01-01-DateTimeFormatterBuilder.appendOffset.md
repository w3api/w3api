---
title: DateTimeFormatterBuilder.appendOffset()
permalink: Java/DateTimeFormatterBuilder/appendOffset
date: 2021-01-11
key: JavaJava.D.DateTimeFormatterBuilder
category: java
tags: ['java se', 'java.time.format', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeFormatterBuilder.metodos valor="appendOffset" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DateTimeFormatterBuilder appendOffset(String pattern, String noOffsetText)
~~~

## Parámetros
* **String noOffsetText**,  {% include w3api/param_description.html metodo=_dato parametro="String noOffsetText" %}
* **String pattern**,  {% include w3api/param_description.html metodo=_dato parametro="String pattern" %}

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
