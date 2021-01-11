---
title: AbstractQueuedLongSynchronizer.acquireSharedInterruptibly()
permalink: Java/AbstractQueuedLongSynchronizer/acquireSharedInterruptibly
date: 2021-01-10
key: JavaJava.A.AbstractQueuedLongSynchronizer
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractQueuedLongSynchronizer.metodos valor="acquireSharedInterruptibly" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void acquireSharedInterruptibly(long arg) throws InterruptedException
~~~

## Parámetros
* **long arg**,  {% include w3api/param_description.html metodo=_dato parametro="long arg" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/)

## Clase Padre
[AbstractQueuedLongSynchronizer](/Java/AbstractQueuedLongSynchronizer/)

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
