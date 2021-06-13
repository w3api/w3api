---
title: MinguoDate.with()
permalink: Java/MinguoDate/with
date: 2021-01-11
key: JavaJava.M.MinguoDate
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MinguoDate.metodos valor="with" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public D with(TemporalField field, long value)
public MinguoDate with(TemporalAdjuster adjuster)
~~~

## Parámetros
* **long value**,  {% include w3api/param_description.html metodo=_dato parametro="long value" %}
* **TemporalField field**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalField field" %}
* **TemporalAdjuster adjuster**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAdjuster adjuster" %}

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
