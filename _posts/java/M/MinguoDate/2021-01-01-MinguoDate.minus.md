---
title: MinguoDate.minus()
permalink: /Java/MinguoDate/minus/
date: 2021-01-11
key: Java.M.MinguoDate
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MinguoDate.metodos valor="minus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public D minus(long amountToSubtract, TemporalUnit unit)
public MinguoDate minus(TemporalAmount amount)
~~~

## Parámetros
* **TemporalUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalUnit unit" %}
* **long amountToSubtract**,  {% include w3api/param_description.html metodo=_dato parametro="long amountToSubtract" %}
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
