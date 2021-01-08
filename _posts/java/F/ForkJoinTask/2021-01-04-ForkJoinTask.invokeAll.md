---
title: ForkJoinTask.invokeAll()
permalink: Java/ForkJoinTask/invokeAll
date: 2021-01-04
key: JavaJava.F.ForkJoinTask
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.ForkJoinTask.metodos valor="invokeAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T extends ForkJoinTask<?>>Collection<T> invokeAll(Collection<T> tasks)
public static void invokeAll(ForkJoinTask<?>... tasks)
public static void invokeAll(ForkJoinTask<?> t1, ForkJoinTask<?> t2)
~~~

## Parámetros
* **ForkJoinTask&lt;?&gt; t1**,  {% include w3api/param_description.html metodo=_data parametro="ForkJoinTask<?> t1" %}
* **ForkJoinTask&lt;?&gt;... tasks**,  {% include w3api/param_description.html metodo=_data parametro="ForkJoinTask<?>... tasks" %}
* **ForkJoinTask&lt;?&gt; t2**,  {% include w3api/param_description.html metodo=_data parametro="ForkJoinTask<?> t2" %}
* **Collection&lt;T&gt; tasks**,  {% include w3api/param_description.html metodo=_data parametro="Collection<T> tasks" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ForkJoinTask](/Java/ForkJoinTask/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.ForkJoinTask.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
