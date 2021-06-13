---
title: ForkJoinTask.cancel()
permalink: /Java/ForkJoinTask/cancel/
date: 2021-01-11
key: Java.F.ForkJoinTask
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.ForkJoinTask.metodos valor="cancel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean cancel(boolean mayInterruptIfRunning)
~~~

## Parámetros
* **boolean mayInterruptIfRunning**,  {% include w3api/param_description.html metodo=_dato parametro="boolean mayInterruptIfRunning" %}

## Clase Padre
[ForkJoinTask](/Java/ForkJoinTask/)

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
