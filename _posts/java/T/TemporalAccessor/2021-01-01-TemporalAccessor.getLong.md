---
title: TemporalAccessor.getLong()
permalink: /Java/TemporalAccessor/getLong/
date: 2021-01-11
key: Java.T.TemporalAccessor
category: Java
tags: ['java se', 'java.time.temporal', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TemporalAccessor.metodos valor="getLong" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long getLong(TemporalField field)
~~~

## Parámetros
* **TemporalField field**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalField field" %}

## Excepciones
[UnsupportedTemporalTypeException](/Java/UnsupportedTemporalTypeException/), [DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[TemporalAccessor](/Java/TemporalAccessor/)

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
