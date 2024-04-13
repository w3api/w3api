---
title: DoubleStream.peek()
permalink: /Java/DoubleStream/peek/
date: 2021-01-11
key: Java.D.DoubleStream
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleStream.metodos valor="peek" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
DoubleStream peek(DoubleConsumer action)
~~~

## Parámetros
* **DoubleConsumer action**,  {% include w3api/param_description.html metodo=_dato parametro="DoubleConsumer action" %}

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
