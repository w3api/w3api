---
title: SwingWorker.get()
permalink: Java/SwingWorker/get
date: 2021-01-11
key: JavaJava.S.SwingWorker
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SwingWorker.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final T get() throws InterruptedException, ExecutionException
public final T get(long timeout, TimeUnit unit) throws InterruptedException, ExecutionException, TimeoutException
~~~

## Parámetros
* **long timeout**,  {% include w3api/param_description.html metodo=_dato parametro="long timeout" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}

## Excepciones
[ExecutionException](/Java/ExecutionException/), [InterruptedException](/Java/InterruptedException/), [TimeoutException](/Java/TimeoutException/)

## Clase Padre
[SwingWorker](/Java/SwingWorker/)

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
