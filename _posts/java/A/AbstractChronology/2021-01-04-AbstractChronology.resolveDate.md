---
title: AbstractChronology.resolveDate()
permalink: Java/AbstractChronology/resolveDate
date: 2021-01-04
key: JavaJava.A.AbstractChronology
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractChronology.metodos valor="resolveDate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ChronoLocalDate resolveDate(Map<TemporalField,Long> fieldValues, ResolverStyle resolverStyle)
~~~

## Parámetros
* **Long&gt; fieldValues**,  {% include w3api/param_description.html metodo=_data parametro="Long> fieldValues" %}
* **ResolverStyle resolverStyle**,  {% include w3api/param_description.html metodo=_data parametro="ResolverStyle resolverStyle" %}
* **Map&lt;TemporalField**,  {% include w3api/param_description.html metodo=_data parametro="Map<TemporalField" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[AbstractChronology](/Java/AbstractChronology/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractChronology.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
