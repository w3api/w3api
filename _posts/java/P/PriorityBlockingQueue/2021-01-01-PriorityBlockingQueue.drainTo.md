---
title: PriorityBlockingQueue.drainTo()
permalink: /Java/PriorityBlockingQueue/drainTo/
date: 2021-01-11
key: Java.P.PriorityBlockingQueue
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PriorityBlockingQueue.metodos valor="drainTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int drainTo(Collection<? super E> c)
public int drainTo(Collection<? super E> c, int maxElements)
~~~

## Parámetros
* **int maxElements**,  {% include w3api/param_description.html metodo=_dato parametro="int maxElements" %}
* **Collection&lt;? super E&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<? super E> c" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [ClassCastException](/Java/ClassCastException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[PriorityBlockingQueue](/Java/PriorityBlockingQueue/)

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
