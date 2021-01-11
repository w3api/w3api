---
title: IntStream.forEachOrdered()
permalink: Java/IntStream/forEachOrdered
date: 2021-01-11
key: JavaJava.I.IntStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntStream.metodos valor="forEachOrdered" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void forEachOrdered(IntConsumer action)
~~~

## Parámetros
* **IntConsumer action**,  {% include w3api/param_description.html metodo=_dato parametro="IntConsumer action" %}

## Clase Padre
[IntStream](/Java/IntStream/)

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