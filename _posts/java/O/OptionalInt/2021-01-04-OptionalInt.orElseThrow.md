---
title: OptionalInt.orElseThrow()
permalink: Java/OptionalInt/orElseThrow
date: 2021-01-04
key: JavaJava.O.OptionalInt
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OptionalInt.metodos valor="orElseThrow" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int orElseThrow()
<X extends Throwable>int orElseThrow(Supplier<? extends X> exceptionSupplier)
~~~

## Parámetros
* **Supplier&lt;? extends X&gt; exceptionSupplier**,  {% include w3api/param_description.html metodo=_data parametro="Supplier<? extends X> exceptionSupplier" %}

## Excepciones
[NoSuchElementException](/Java/NoSuchElementException/)

## Clase Padre
[OptionalInt](/Java/OptionalInt/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.OptionalInt.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
