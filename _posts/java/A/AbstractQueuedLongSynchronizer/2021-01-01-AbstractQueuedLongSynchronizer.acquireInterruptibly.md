---
title: AbstractQueuedLongSynchronizer.acquireInterruptibly()
permalink: /Java/AbstractQueuedLongSynchronizer/acquireInterruptibly/
date: 2021-01-11
key: Java.A.AbstractQueuedLongSynchronizer
category: Java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractQueuedLongSynchronizer.metodos valor="acquireInterruptibly" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void acquireInterruptibly(long arg) throws InterruptedException
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
