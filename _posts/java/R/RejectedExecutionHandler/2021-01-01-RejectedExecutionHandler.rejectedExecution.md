---
title: RejectedExecutionHandler.rejectedExecution()
permalink: Java/RejectedExecutionHandler/rejectedExecution
date: 2021-01-11
key: Java.R.RejectedExecutionHandler
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RejectedExecutionHandler.metodos valor="rejectedExecution" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void rejectedExecution(Runnable r, ThreadPoolExecutor executor)
~~~

## Parámetros
* **Runnable r**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable r" %}
* **ThreadPoolExecutor executor**,  {% include w3api/param_description.html metodo=_dato parametro="ThreadPoolExecutor executor" %}

## Excepciones
[RejectedExecutionException](/Java/RejectedExecutionException/)

## Clase Padre
[RejectedExecutionHandler](/Java/RejectedExecutionHandler/)

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
