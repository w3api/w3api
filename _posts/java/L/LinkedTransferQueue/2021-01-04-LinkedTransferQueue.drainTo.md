---
title: LinkedTransferQueue.drainTo()
permalink: Java/LinkedTransferQueue/drainTo
date: 2021-01-04
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
* **Collection&lt;? super E&gt; c**,  {% include w3api/param_description.html metodo=_data parametro="Collection<? super E> c" %}
* **int maxElements**,  {% include w3api/param_description.html metodo=_data parametro="int maxElements" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[LinkedTransferQueue](/Java/LinkedTransferQueue/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LinkedTransferQueue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
