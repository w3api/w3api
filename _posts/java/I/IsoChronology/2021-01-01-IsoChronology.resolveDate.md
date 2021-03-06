---
title: IsoChronology.resolveDate()
permalink: /Java/IsoChronology/resolveDate/
date: 2021-01-11
key: Java.I.IsoChronology
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IsoChronology.metodos valor="resolveDate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LocalDate resolveDate(Map<TemporalField,Long> fieldValues, ResolverStyle resolverStyle)
~~~

## Parámetros
* **ResolverStyle resolverStyle**,  {% include w3api/param_description.html metodo=_dato parametro="ResolverStyle resolverStyle" %}
* **Map&lt;TemporalField**,  {% include w3api/param_description.html metodo=_dato parametro="Map<TemporalField" %}
* **Long&gt; fieldValues**,  {% include w3api/param_description.html metodo=_dato parametro="Long> fieldValues" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[IsoChronology](/Java/IsoChronology/)

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
