---
title: ModuleTree.ModuleKind.valueOf()
permalink: Java/ModuleTree/ModuleKind/valueOf
date: 2021-01-11
key: JavaJava.M.ModuleTree.ModuleKind
category: Java
tags: ['java se', 'com.sun.source.tree', 'jdk.compiler', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleTree.ModuleKind.metodos valor="valueOf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ModuleTree.ModuleKind valueOf(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ModuleTree.ModuleKind](/Java/ModuleTree/ModuleKind/)

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
