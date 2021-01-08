---
title: BlockingQueue.drainTo()
permalink: Java/BlockingQueue/drainTo
date: 2021-01-04
key: JavaJava.B.BlockingQueue
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BlockingQueue.metodos valor="drainTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int drainTo(Collection<? super E> c)
int drainTo(Collection<? super E> c, int maxElements)
~~~

## Parámetros
* **Collection&lt;? super E&gt; c**,  {% include w3api/param_description.html metodo=_data parametro="Collection<? super E> c" %}
* **int maxElements**,  {% include w3api/param_description.html metodo=_data parametro="int maxElements" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BlockingQueue](/Java/BlockingQueue/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BlockingQueue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
