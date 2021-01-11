---
title: MinguoDate.plus()
permalink: Java/MinguoDate/plus
date: 2021-01-11
key: JavaJava.M.MinguoDate
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MinguoDate.metodos valor="plus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public D plus(long amountToAdd, TemporalUnit unit)
public MinguoDate plus(TemporalAmount amount)
~~~

## Parámetros
* **long amountToAdd**,  {% include w3api/param_description.html metodo=_dato parametro="long amountToAdd" %}
* **TemporalUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalUnit unit" %}
* **TemporalAmount amount**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAmount amount" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[MinguoDate](/Java/MinguoDate/)

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
