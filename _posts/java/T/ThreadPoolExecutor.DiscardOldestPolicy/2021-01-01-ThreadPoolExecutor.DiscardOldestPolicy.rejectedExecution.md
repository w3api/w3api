---
title: ThreadPoolExecutor.DiscardOldestPolicy.rejectedExecution()
permalink: Java/ThreadPoolExecutor/DiscardOldestPolicy/rejectedExecution
date: 2021-01-11
key: JavaJava.T.ThreadPoolExecutor.DiscardOldestPolicy
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadPoolExecutor.DiscardOldestPolicy.metodos valor="rejectedExecution" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void rejectedExecution(Runnable r, ThreadPoolExecutor e)
~~~

## Parámetros
* **Runnable r**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable r" %}
* **ThreadPoolExecutor e**,  {% include w3api/param_description.html metodo=_dato parametro="ThreadPoolExecutor e" %}

## Clase Padre
[ThreadPoolExecutor.DiscardOldestPolicy](/Java/ThreadPoolExecutor/DiscardOldestPolicy/)

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
