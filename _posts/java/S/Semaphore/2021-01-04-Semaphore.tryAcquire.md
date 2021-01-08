---
title: Semaphore.tryAcquire()
permalink: Java/Semaphore/tryAcquire
date: 2021-01-04
key: JavaJava.S.Semaphore
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Semaphore.metodos valor="tryAcquire" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean tryAcquire()
public boolean tryAcquire(int permits)
public boolean tryAcquire(int permits, long timeout, TimeUnit unit) throws InterruptedException
public boolean tryAcquire(long timeout, TimeUnit unit) throws InterruptedException
~~~

## Parámetros
* **int permits**,  {% include w3api/param_description.html metodo=_data parametro="int permits" %}
* **long timeout**,  {% include w3api/param_description.html metodo=_data parametro="long timeout" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TimeUnit unit" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Semaphore](/Java/Semaphore/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.Semaphore.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
