---
title: DoubleConsumer.andThen()
permalink: Java/DoubleConsumer/andThen
date: 2021-01-04
key: JavaJava.D.DoubleConsumer
category: java
tags: ['java se', 'java.util.function', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleConsumer.metodos valor="andThen" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default DoubleConsumer andThen(DoubleConsumer after)
~~~

## Parámetros
* **DoubleConsumer after**,  {% include w3api/param_description.html metodo=_data parametro="DoubleConsumer after" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DoubleConsumer](/Java/DoubleConsumer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DoubleConsumer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
