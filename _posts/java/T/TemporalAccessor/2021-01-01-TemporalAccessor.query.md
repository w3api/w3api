---
title: TemporalAccessor.query()
permalink: /Java/TemporalAccessor/query/
date: 2021-01-11
key: Java.T.TemporalAccessor
category: Java
tags: ['java se', 'java.time.temporal', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TemporalAccessor.metodos valor="query" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default <R> R query(TemporalQuery<R> query)
~~~

## Parámetros
* **TemporalQuery&lt;R&gt; query**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalQuery<R> query" %}

## Clase Padre
[TemporalAccessor](/Java/TemporalAccessor/)

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
