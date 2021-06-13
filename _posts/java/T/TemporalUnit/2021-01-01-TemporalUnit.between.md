---
title: TemporalUnit.between()
permalink: /Java/TemporalUnit/between/
date: 2021-01-11
key: Java.T.TemporalUnit
category: Java
tags: ['java se', 'java.time.temporal', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TemporalUnit.metodos valor="between" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long between(Temporal temporal1Inclusive, Temporal temporal2Exclusive)
~~~

## Parámetros
* **Temporal temporal2Exclusive**,  {% include w3api/param_description.html metodo=_dato parametro="Temporal temporal2Exclusive" %}
* **Temporal temporal1Inclusive**,  {% include w3api/param_description.html metodo=_dato parametro="Temporal temporal1Inclusive" %}

## Excepciones
[UnsupportedTemporalTypeException](/Java/UnsupportedTemporalTypeException/), [DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[TemporalUnit](/Java/TemporalUnit/)

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
