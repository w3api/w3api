---
title: TemporalQuery.queryFrom()
permalink: /Java/TemporalQuery/queryFrom/
date: 2021-01-11
key: Java.T.TemporalQuery
category: Java
tags: ['java se', 'java.time.temporal', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TemporalQuery.metodos valor="queryFrom" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
R queryFrom(TemporalAccessor temporal)
~~~

## Parámetros
* **TemporalAccessor temporal**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAccessor temporal" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[TemporalQuery](/Java/TemporalQuery/)

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
