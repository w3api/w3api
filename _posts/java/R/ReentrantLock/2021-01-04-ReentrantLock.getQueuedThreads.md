---
title: ReentrantLock.getQueuedThreads()
permalink: Java/ReentrantLock/getQueuedThreads
date: 2021-01-04
key: JavaJava.R.ReentrantLock
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ReentrantLock.metodos valor="getQueuedThreads" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Collection<Thread> getQueuedThreads()
~~~

## Clase Padre
[ReentrantLock](/Java/ReentrantLock/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ReentrantLock.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
