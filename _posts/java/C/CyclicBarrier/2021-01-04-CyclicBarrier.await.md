---
title: CyclicBarrier.await()
permalink: Java/CyclicBarrier/await
date: 2021-01-04
key: JavaJava.C.CyclicBarrier
category: java
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
* **long timeout**,  {% include w3api/param_description.html metodo=_data parametro="long timeout" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TimeUnit unit" %}

## Excepciones
[TimeoutException](/Java/TimeoutException/), [InterruptedException](/Java/InterruptedException/), [BrokenBarrierException](/Java/BrokenBarrierException/)

## Clase Padre
[CyclicBarrier](/Java/CyclicBarrier/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CyclicBarrier.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
