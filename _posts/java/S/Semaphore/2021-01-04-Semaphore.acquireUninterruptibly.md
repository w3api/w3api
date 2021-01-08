---
title: Semaphore.acquireUninterruptibly()
permalink: Java/Semaphore/acquireUninterruptibly
date: 2021-01-04
key: JavaJava.S.Semaphore
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Semaphore.metodos valor="acquireUninterruptibly" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void acquireUninterruptibly()
public void acquireUninterruptibly(int permits)
~~~

## Parámetros
* **int permits**,  {% include w3api/param_description.html metodo=_data parametro="int permits" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Semaphore](/Java/Semaphore/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.Semaphore.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
