---
title: FutureTask.FutureTask()
permalink: Java/FutureTask/FutureTask
date: 2021-01-11
key: JavaJava.F.FutureTask
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FutureTask.constructores valor="FutureTask" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FutureTask(Runnable runnable, V result)
public FutureTask(Callable<V> callable)
~~~

## Parámetros
* **V result**,  {% include w3api/param_description.html metodo=_dato parametro="V result" %}
* **Runnable runnable**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable runnable" %}
* **Callable&lt;V&gt; callable**,  {% include w3api/param_description.html metodo=_dato parametro="Callable<V> callable" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[FutureTask](/Java/FutureTask/)

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
