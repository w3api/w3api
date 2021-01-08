---
title: BiConsumer.andThen()
permalink: Java/BiConsumer/andThen
date: 2021-01-04
key: JavaJava.B.BiConsumer
category: java
tags: ['java se', 'java.util.function', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BiConsumer.metodos valor="andThen" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default BiConsumer<T,U> andThen(BiConsumer<? super T,? super U> after)
~~~

## Parámetros
* **? super U&gt; after**,  {% include w3api/param_description.html metodo=_data parametro="? super U> after" %}
* **BiConsumer&lt;? super T**,  {% include w3api/param_description.html metodo=_data parametro="BiConsumer<? super T" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[BiConsumer](/Java/BiConsumer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BiConsumer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
