---
title: ExecutorService.shutdownNow()
permalink: Java/ExecutorService/shutdownNow
date: 2021-01-11
key: JavaJava.E.ExecutorService
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExecutorService.metodos valor="shutdownNow" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
List<Runnable> shutdownNow()
~~~

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[ExecutorService](/Java/ExecutorService/)

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
