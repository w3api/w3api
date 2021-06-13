---
title: ThreadFactory.newThread()
permalink: /Java/ThreadFactory/newThread/
date: 2021-01-11
key: Java.T.ThreadFactory
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadFactory.metodos valor="newThread" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Thread newThread(Runnable r)
~~~

## Parámetros
* **Runnable r**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable r" %}

## Clase Padre
[ThreadFactory](/Java/ThreadFactory/)

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
