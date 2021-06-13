---
title: ModuleLayer.findLoader()
permalink: Java/ModuleLayer/findLoader
date: 2021-01-11
key: JavaJava.M.ModuleLayer
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleLayer.metodos valor="findLoader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ClassLoader findLoader(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ModuleLayer](/Java/ModuleLayer/)

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
