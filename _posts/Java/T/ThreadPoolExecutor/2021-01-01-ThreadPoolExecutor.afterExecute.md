---
title: ThreadPoolExecutor.afterExecute()
permalink: /Java/ThreadPoolExecutor/afterExecute/
date: 2021-01-11
key: Java.T.ThreadPoolExecutor
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadPoolExecutor.metodos valor="afterExecute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void afterExecute(Runnable r, Throwable t)
~~~

## Parámetros
* **Runnable r**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable r" %}
* **Throwable t**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable t" %}

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
