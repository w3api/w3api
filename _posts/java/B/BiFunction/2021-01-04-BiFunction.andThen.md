---
title: BiFunction.andThen()
permalink: Java/BiFunction/andThen
date: 2021-01-04
key: JavaJava.B.BiFunction
category: java
tags: ['java se', 'java.util.function', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BiFunction.metodos valor="andThen" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default <V> BiFunction<T,U,V> andThen(Function<? super R,? extends V> after)
~~~

## Parámetros
* **Function&lt;? super R**,  {% include w3api/param_description.html metodo=_data parametro="Function<? super R" %}
* **? extends V&gt; after**,  {% include w3api/param_description.html metodo=_data parametro="? extends V> after" %}

## Clase Padre
[BiFunction](/Java/BiFunction/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BiFunction.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
