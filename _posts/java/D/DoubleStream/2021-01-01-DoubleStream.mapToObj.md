---
title: DoubleStream.mapToObj()
permalink: /Java/DoubleStream/mapToObj/
date: 2021-01-11
key: Java.D.DoubleStream
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleStream.metodos valor="mapToObj" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<U> Stream<U> mapToObj(DoubleFunction<? extends U> mapper)
~~~

## Parámetros
* **DoubleFunction&lt;? extends U&gt; mapper**,  {% include w3api/param_description.html metodo=_dato parametro="DoubleFunction<? extends U> mapper" %}

## Clase Padre
[DoubleStream](/Java/DoubleStream/)

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
