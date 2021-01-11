---
title: ModuleFinder.compose()
permalink: Java/ModuleFinder/compose
date: 2021-01-11
key: JavaJava.M.ModuleFinder
category: java
tags: ['java se', 'java.lang.module', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleFinder.metodos valor="compose" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static ModuleFinder compose(ModuleFinder... finders)
~~~

## Parámetros
* **ModuleFinder... finders**,  {% include w3api/param_description.html metodo=_dato parametro="ModuleFinder... finders" %}

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
