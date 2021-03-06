---
title: CyclicBarrier.await()
permalink: /Java/CyclicBarrier/await/
date: 2021-01-11
key: Java.C.CyclicBarrier
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CyclicBarrier.metodos valor="await" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int await() throws InterruptedException, BrokenBarrierException
public int await(long timeout, TimeUnit unit) throws InterruptedException, BrokenBarrierException, TimeoutException
~~~

## Parámetros
* **long timeout**,  {% include w3api/param_description.html metodo=_dato parametro="long timeout" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/), [BrokenBarrierException](/Java/BrokenBarrierException/), [TimeoutException](/Java/TimeoutException/)

## Clase Padre
[CyclicBarrier](/Java/CyclicBarrier/)

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
