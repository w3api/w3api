---
title: LinkedTransferQueue.drainTo()
permalink: Java/LinkedTransferQueue/drainTo
date: 2021-01-11
key: JavaJava.L.LinkedTransferQueue
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinkedTransferQueue.metodos valor="drainTo" %}

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
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LinkedTransferQueue](/Java/LinkedTransferQueue/)

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
