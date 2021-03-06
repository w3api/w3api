---
title: ReentrantReadWriteLock.getWaitingThreads()
permalink: /Java/ReentrantReadWriteLock/getWaitingThreads/
date: 2021-01-11
key: Java.R.ReentrantReadWriteLock
category: Java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ReentrantReadWriteLock.metodos valor="getWaitingThreads" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Collection<Thread> getWaitingThreads(Condition condition)
~~~

## Parámetros
* **Condition condition**,  {% include w3api/param_description.html metodo=_dato parametro="Condition condition" %}

## Excepciones
[IllegalMonitorStateException](/Java/IllegalMonitorStateException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ReentrantReadWriteLock](/Java/ReentrantReadWriteLock/)

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
