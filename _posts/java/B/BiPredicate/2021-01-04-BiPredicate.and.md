---
title: BiPredicate.and()
permalink: Java/BiPredicate/and
date: 2021-01-04
key: JavaJava.B.BiPredicate
category: java
tags: ['java se', 'java.util.function', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BiPredicate.metodos valor="and" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default BiPredicate<T,U> and(BiPredicate<? super T,? super U> other)
~~~

## Parámetros
* **? super U&gt; other**,  {% include w3api/param_description.html metodo=_data parametro="? super U> other" %}
* **BiPredicate&lt;? super T**,  {% include w3api/param_description.html metodo=_data parametro="BiPredicate<? super T" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[BiPredicate](/Java/BiPredicate/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BiPredicate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
