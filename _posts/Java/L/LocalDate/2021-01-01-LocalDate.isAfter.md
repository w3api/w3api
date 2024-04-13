---
title: LocalDate.isAfter()
permalink: /Java/LocalDate/isAfter/
date: 2021-01-11
key: Java.L.LocalDate
category: Java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDate.metodos valor="isAfter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean isAfter(ChronoLocalDate other)
~~~

## Parámetros
* **ChronoLocalDate other**,  {% include w3api/param_description.html metodo=_dato parametro="ChronoLocalDate other" %}

## Clase Padre
[LocalDate](/Java/LocalDate/)

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
