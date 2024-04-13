---
title: Semaphore.Semaphore()
permalink: /Java/Semaphore/Semaphore/
date: 2021-01-11
key: Java.S.Semaphore
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Semaphore.constructores valor="Semaphore" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Semaphore(int permits)
public Semaphore(int permits, boolean fair)
~~~

## Parámetros
* **boolean fair**,  {% include w3api/param_description.html metodo=_dato parametro="boolean fair" %}
* **int permits**,  {% include w3api/param_description.html metodo=_dato parametro="int permits" %}

## Clase Padre
[Semaphore](/Java/Semaphore/)

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
