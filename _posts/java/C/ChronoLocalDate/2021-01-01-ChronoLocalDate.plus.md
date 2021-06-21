---
title: ChronoLocalDate.plus()
permalink: /Java/ChronoLocalDate/plus/
date: 2021-01-11
key: Java.C.ChronoLocalDate
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChronoLocalDate.metodos valor="plus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default ChronoLocalDate plus(long amountToAdd, TemporalUnit unit)
default ChronoLocalDate plus(TemporalAmount amount)
~~~

## Parámetros
* **long amountToAdd**,  {% include w3api/param_description.html metodo=_dato parametro="long amountToAdd" %}
* **TemporalUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalUnit unit" %}
* **TemporalAmount amount**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAmount amount" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[ChronoLocalDate](/Java/ChronoLocalDate/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
