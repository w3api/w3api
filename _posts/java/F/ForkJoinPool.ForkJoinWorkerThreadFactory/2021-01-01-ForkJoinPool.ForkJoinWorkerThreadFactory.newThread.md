---
title: ForkJoinPool.ForkJoinWorkerThreadFactory.newThread()
permalink: Java/ForkJoinPool/ForkJoinWorkerThreadFactory/newThread
date: 2021-01-11
key: JavaJava.F.ForkJoinPool.ForkJoinWorkerThreadFactory
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.ForkJoinPool.ForkJoinWorkerThreadFactory.metodos valor="newThread" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ForkJoinWorkerThread newThread(ForkJoinPool pool)
~~~

## Parámetros
* **ForkJoinPool pool**,  {% include w3api/param_description.html metodo=_dato parametro="ForkJoinPool pool" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ForkJoinPool.ForkJoinWorkerThreadFactory](/Java/ForkJoinPool/ForkJoinWorkerThreadFactory/)

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
