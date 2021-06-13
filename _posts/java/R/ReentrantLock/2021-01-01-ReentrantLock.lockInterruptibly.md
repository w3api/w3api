---
title: ReentrantLock.lockInterruptibly()
permalink: Java/ReentrantLock/lockInterruptibly
date: 2021-01-11
key: Java.R.ReentrantLock
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ReentrantLock.metodos valor="lockInterruptibly" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void lockInterruptibly() throws InterruptedException
~~~

## Excepciones
[InterruptedException](/Java/InterruptedException/)

## Clase Padre
[ReentrantLock](/Java/ReentrantLock/)

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
