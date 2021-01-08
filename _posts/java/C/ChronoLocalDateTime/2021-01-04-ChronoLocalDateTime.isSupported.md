---
title: ChronoLocalDateTime.isSupported()
permalink: Java/ChronoLocalDateTime/isSupported
date: 2021-01-04
key: JavaJava.C.ChronoLocalDateTime
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChronoLocalDateTime.metodos valor="isSupported" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean isSupported(TemporalField field)
default boolean isSupported(TemporalUnit unit)
~~~

## Parámetros
* **TemporalUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TemporalUnit unit" %}
* **TemporalField field**,  {% include w3api/param_description.html metodo=_data parametro="TemporalField field" %}

## Clase Padre
[ChronoLocalDateTime](/Java/ChronoLocalDateTime/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ChronoLocalDateTime.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
