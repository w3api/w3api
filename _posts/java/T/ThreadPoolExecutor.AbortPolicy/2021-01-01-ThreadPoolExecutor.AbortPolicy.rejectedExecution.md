---
title: ThreadPoolExecutor.AbortPolicy.rejectedExecution()
permalink: /Java/ThreadPoolExecutor/AbortPolicy/rejectedExecution/
date: 2021-01-11
key: Java.T.ThreadPoolExecutor.AbortPolicy
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadPoolExecutor.AbortPolicy.metodos valor="rejectedExecution" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void rejectedExecution(Runnable r, ThreadPoolExecutor e)
~~~

## Parámetros
* **Runnable r**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable r" %}
* **ThreadPoolExecutor e**,  {% include w3api/param_description.html metodo=_dato parametro="ThreadPoolExecutor e" %}

## Excepciones
[RejectedExecutionException](/Java/RejectedExecutionException/)

## Clase Padre
[ThreadPoolExecutor.AbortPolicy](/Java/ThreadPoolExecutor/AbortPolicy/)

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
