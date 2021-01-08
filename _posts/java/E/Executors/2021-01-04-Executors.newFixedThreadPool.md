---
title: Executors.newFixedThreadPool()
permalink: Java/Executors/newFixedThreadPool
date: 2021-01-04
key: JavaJava.E.Executors
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.Executors.metodos valor="newFixedThreadPool" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ExecutorService newFixedThreadPool(int nThreads)
public static ExecutorService newFixedThreadPool(int nThreads, ThreadFactory threadFactory)
~~~

## Parámetros
* **int nThreads**,  {% include w3api/param_description.html metodo=_data parametro="int nThreads" %}
* **ThreadFactory threadFactory**,  {% include w3api/param_description.html metodo=_data parametro="ThreadFactory threadFactory" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Executors](/Java/Executors/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.Executors.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
