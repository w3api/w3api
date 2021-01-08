---
title: ModuleFinder.of()
permalink: Java/ModuleFinder/of
date: 2021-01-04
key: JavaJava.M.ModuleFinder
category: java
tags: ['java se', 'java.lang.module', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleFinder.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static ModuleFinder of(Path... entries)
~~~

## Parámetros
* **Path... entries**,  {% include w3api/param_description.html metodo=_data parametro="Path... entries" %}

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
