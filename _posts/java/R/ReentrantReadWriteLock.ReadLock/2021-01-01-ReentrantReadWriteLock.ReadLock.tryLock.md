---
title: ReentrantReadWriteLock.ReadLock.tryLock()
permalink: Java/ReentrantReadWriteLock/ReadLock/tryLock
date: 2021-01-11
key: Java.R.ReentrantReadWriteLock.ReadLock
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ReentrantReadWriteLock.ReadLock.metodos valor="tryLock" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean tryLock()
public boolean tryLock(long timeout, TimeUnit unit) throws InterruptedException
~~~

## Parámetros
* **long timeout**,  {% include w3api/param_description.html metodo=_dato parametro="long timeout" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ReentrantReadWriteLock.ReadLock](/Java/ReentrantReadWriteLock/ReadLock/)

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
