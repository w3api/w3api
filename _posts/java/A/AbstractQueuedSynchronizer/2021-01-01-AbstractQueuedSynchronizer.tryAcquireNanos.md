---
title: AbstractQueuedSynchronizer.tryAcquireNanos()
permalink: Java/AbstractQueuedSynchronizer/tryAcquireNanos
date: 2021-01-11
key: JavaJava.A.AbstractQueuedSynchronizer
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractQueuedSynchronizer.metodos valor="tryAcquireNanos" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final boolean tryAcquireNanos(int arg, long nanosTimeout) throws InterruptedException
~~~

## Parámetros
* **long nanosTimeout**,  {% include w3api/param_description.html metodo=_dato parametro="long nanosTimeout" %}
* **int arg**,  {% include w3api/param_description.html metodo=_dato parametro="int arg" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/)

## Clase Padre
[AbstractQueuedSynchronizer](/Java/AbstractQueuedSynchronizer/)

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
