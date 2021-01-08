---
title: ModuleFinder.find()
permalink: Java/ModuleFinder/find
date: 2021-01-04
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
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[FindException](/Java/FindException/), [SecurityException](/Java/SecurityException/)

## Clase Padre
[ModuleFinder](/Java/ModuleFinder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.ModuleFinder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
