---
title: ChronoLocalDate.isSupported()
permalink: Java/ChronoLocalDate/isSupported
date: 2021-01-04
key: JavaJava.C.ChronoLocalDate
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChronoLocalDate.metodos valor="isSupported" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default boolean isSupported(TemporalField field)
default boolean isSupported(TemporalUnit unit)
~~~

## Parámetros
* **TemporalUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TemporalUnit unit" %}
* **TemporalField field**,  {% include w3api/param_description.html metodo=_data parametro="TemporalField field" %}

## Clase Padre
[ChronoLocalDate](/Java/ChronoLocalDate/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ChronoLocalDate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
