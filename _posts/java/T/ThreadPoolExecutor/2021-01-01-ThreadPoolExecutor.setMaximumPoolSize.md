---
title: ThreadPoolExecutor.setMaximumPoolSize()
permalink: /Java/ThreadPoolExecutor/setMaximumPoolSize/
date: 2021-01-11
key: Java.T.ThreadPoolExecutor
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadPoolExecutor.metodos valor="setMaximumPoolSize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setMaximumPoolSize(int maximumPoolSize)
~~~

## Parámetros
* **int maximumPoolSize**,  {% include w3api/param_description.html metodo=_dato parametro="int maximumPoolSize" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
