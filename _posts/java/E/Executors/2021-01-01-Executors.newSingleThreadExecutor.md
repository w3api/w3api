---
title: Executors.newSingleThreadExecutor()
permalink: Java/Executors/newSingleThreadExecutor
date: 2021-01-11
key: JavaJava.E.Executors
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.Executors.metodos valor="newSingleThreadExecutor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ExecutorService newSingleThreadExecutor()
public static ExecutorService newSingleThreadExecutor(ThreadFactory threadFactory)
~~~

## Parámetros
* **ThreadFactory threadFactory**,  {% include w3api/param_description.html metodo=_dato parametro="ThreadFactory threadFactory" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
