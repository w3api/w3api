---
title: ThreadPoolExecutor.DiscardPolicy.rejectedExecution()
permalink: Java/ThreadPoolExecutor/DiscardPolicy/rejectedExecution
date: 2021-01-04
key: JavaJava.T.ThreadPoolExecutor.DiscardPolicy
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadPoolExecutor.DiscardPolicy.metodos valor="rejectedExecution" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void rejectedExecution(Runnable r, ThreadPoolExecutor e)
~~~

## Parámetros
* **Runnable r**,  {% include w3api/param_description.html metodo=_data parametro="Runnable r" %}
* **ThreadPoolExecutor e**,  {% include w3api/param_description.html metodo=_data parametro="ThreadPoolExecutor e" %}

## Clase Padre
[ThreadPoolExecutor.DiscardPolicy](/Java/ThreadPoolExecutor/DiscardPolicy/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThreadPoolExecutor.DiscardPolicy.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
