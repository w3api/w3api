---
title: TemporalAmount.subtractFrom()
permalink: /Java/TemporalAmount/subtractFrom/
date: 2021-01-11
key: Java.T.TemporalAmount
category: Java
tags: ['java se', 'java.time.temporal', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TemporalAmount.metodos valor="subtractFrom" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Temporal subtractFrom(Temporal temporal)
~~~

## Parámetros
* **Temporal temporal**,  {% include w3api/param_description.html metodo=_dato parametro="Temporal temporal" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[TemporalAmount](/Java/TemporalAmount/)

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
