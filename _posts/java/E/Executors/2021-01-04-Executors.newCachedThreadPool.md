---
title: Executors.newCachedThreadPool()
permalink: Java/Executors/newCachedThreadPool
date: 2021-01-04
key: JavaJava.E.Executors
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.Executors.metodos valor="newCachedThreadPool" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ExecutorService newCachedThreadPool()
public static ExecutorService newCachedThreadPool(ThreadFactory threadFactory)
~~~

## Parámetros
* **ThreadFactory threadFactory**,  {% include w3api/param_description.html metodo=_data parametro="ThreadFactory threadFactory" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
