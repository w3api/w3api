---
title: ModuleDescriptor.newAutomaticModule()
permalink: /Java/ModuleDescriptor/newAutomaticModule/
date: 2021-01-11
key: Java.M.ModuleDescriptor
category: Java
tags: ['java se', 'java.lang.module', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleDescriptor.metodos valor="newAutomaticModule" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ModuleDescriptor.Builder newAutomaticModule(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ModuleDescriptor](/Java/ModuleDescriptor/)

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
