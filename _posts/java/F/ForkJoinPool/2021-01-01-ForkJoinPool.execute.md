---
title: ForkJoinPool.execute()
permalink: Java/ForkJoinPool/execute
date: 2021-01-11
key: JavaJava.F.ForkJoinPool
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.ForkJoinPool.metodos valor="execute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void execute(Runnable task)
public void execute(ForkJoinTask<?> task)
~~~

## Parámetros
* **ForkJoinTask&lt;?&gt; task**,  {% include w3api/param_description.html metodo=_dato parametro="ForkJoinTask<?> task" %}
* **Runnable task**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable task" %}

## Excepciones
[RejectedExecutionException](/Java/RejectedExecutionException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ForkJoinPool](/Java/ForkJoinPool/)

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
