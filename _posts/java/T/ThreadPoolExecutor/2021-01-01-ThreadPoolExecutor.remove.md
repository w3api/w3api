---
title: ThreadPoolExecutor.remove()
permalink: Java/ThreadPoolExecutor/remove
date: 2021-01-11
key: JavaJava.T.ThreadPoolExecutor
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadPoolExecutor.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean remove(Runnable task)
~~~

## Parámetros
* **Runnable task**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable task" %}

## Clase Padre
[ThreadPoolExecutor](/Java/ThreadPoolExecutor/)

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
