---
title: ThaiBuddhistDate.minus()
permalink: Java/ThaiBuddhistDate/minus
date: 2021-01-04
key: JavaJava.T.ThaiBuddhistDate
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThaiBuddhistDate.metodos valor="minus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public D minus(long amountToSubtract, TemporalUnit unit)
public ThaiBuddhistDate minus(TemporalAmount amount)
~~~

## Parámetros
* **TemporalUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TemporalUnit unit" %}
* **TemporalAmount amount**,  {% include w3api/param_description.html metodo=_data parametro="TemporalAmount amount" %}
* **long amountToSubtract**,  {% include w3api/param_description.html metodo=_data parametro="long amountToSubtract" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[ThaiBuddhistDate](/Java/ThaiBuddhistDate/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThaiBuddhistDate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
