---
title: ModuleFinder.find()
permalink: Java/ModuleFinder/find
date: 2021-01-11
key: JavaJava.M.ModuleFinder
category: java
tags: ['java se', 'java.lang.module', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleFinder.metodos valor="find" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Optional<ModuleReference> find(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [FindException](/Java/FindException/)

## Clase Padre
[ModuleFinder](/Java/ModuleFinder/)

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
