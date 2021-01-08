---
title: LocalDateTime.minusMinutes()
permalink: Java/LocalDateTime/minusMinutes
date: 2021-01-04
key: JavaJava.L.LocalDateTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDateTime.metodos valor="minusMinutes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LocalDateTime minusMinutes(long minutes)
~~~

## Parámetros
* **long minutes**,  {% include w3api/param_description.html metodo=_data parametro="long minutes" %}

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
