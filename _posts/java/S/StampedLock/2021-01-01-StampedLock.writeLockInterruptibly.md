---
title: StampedLock.writeLockInterruptibly()
permalink: Java/StampedLock/writeLockInterruptibly
date: 2021-01-11
key: JavaJava.S.StampedLock
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StampedLock.metodos valor="writeLockInterruptibly" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long writeLockInterruptibly() throws InterruptedException
~~~

## Excepciones
[InterruptedException](/Java/InterruptedException/)

## Clase Padre
[StampedLock](/Java/StampedLock/)

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
