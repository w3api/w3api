---
title: LocalDateTime.minusYears()
permalink: Java/LocalDateTime/minusYears
date: 2021-01-04
key: JavaJava.L.LocalDateTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDateTime.metodos valor="minusYears" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LocalDateTime minusYears(long years)
~~~

## Parámetros
* **long years**,  {% include w3api/param_description.html metodo=_data parametro="long years" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[LocalDateTime](/Java/LocalDateTime/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LocalDateTime.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
