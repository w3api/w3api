---
title: MemoryHandler.MemoryHandler()
permalink: Java/MemoryHandler/MemoryHandler
date: 2021-01-11
key: JavaJava.M.MemoryHandler
category: Java
tags: ['java se', 'java.util.logging', 'java.logging', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MemoryHandler.constructores valor="MemoryHandler" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MemoryHandler()
public MemoryHandler(Handler target, int size, Level pushLevel)
~~~

## Parámetros
* **Handler target**,  {% include w3api/param_description.html metodo=_dato parametro="Handler target" %}
* **int size**,  {% include w3api/param_description.html metodo=_dato parametro="int size" %}
* **Level pushLevel**,  {% include w3api/param_description.html metodo=_dato parametro="Level pushLevel" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MemoryHandler](/Java/MemoryHandler/)

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
