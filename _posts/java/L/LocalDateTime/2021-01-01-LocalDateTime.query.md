---
title: LocalDateTime.query()
permalink: Java/LocalDateTime/query
date: 2021-01-11
key: JavaJava.L.LocalDateTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDateTime.metodos valor="query" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<R> R query(TemporalQuery<R> query)
~~~

## Parámetros
* **TemporalQuery&lt;R&gt; query**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalQuery<R> query" %}

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
