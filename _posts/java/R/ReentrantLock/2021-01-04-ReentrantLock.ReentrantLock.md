---
title: ReentrantLock.ReentrantLock()
permalink: Java/ReentrantLock/ReentrantLock
date: 2021-01-04
key: JavaJava.R.ReentrantLock
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ReentrantLock.constructores valor="ReentrantLock" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ReentrantLock()
public ReentrantLock(boolean fair)
~~~

## Parámetros
* **boolean fair**,  {% include w3api/param_description.html metodo=_data parametro="boolean fair" %}

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
