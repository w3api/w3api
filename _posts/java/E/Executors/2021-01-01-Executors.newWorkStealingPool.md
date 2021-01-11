---
title: Executors.newWorkStealingPool()
permalink: Java/Executors/newWorkStealingPool
date: 2021-01-11
key: JavaJava.E.Executors
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.Executors.metodos valor="newWorkStealingPool" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ExecutorService newWorkStealingPool()
public static ExecutorService newWorkStealingPool(int parallelism)
~~~

## Parámetros
* **int parallelism**,  {% include w3api/param_description.html metodo=_dato parametro="int parallelism" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
