---
title: LocalDateTime.withSecond()
permalink: /Java/LocalDateTime/withSecond/
date: 2021-01-11
key: Java.L.LocalDateTime
category: Java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDateTime.metodos valor="withSecond" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LocalDateTime withSecond(int second)
~~~

## Parámetros
* **int second**,  {% include w3api/param_description.html metodo=_dato parametro="int second" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
