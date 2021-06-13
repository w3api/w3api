---
title: ModuleDescriptor.newModule()
permalink: Java/ModuleDescriptor/newModule
date: 2021-01-11
key: JavaJava.M.ModuleDescriptor
category: Java
tags: ['java se', 'java.lang.module', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleDescriptor.metodos valor="newModule" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ModuleDescriptor.Builder newModule(String name)
public static ModuleDescriptor.Builder newModule(String name, Set<ModuleDescriptor.Modifier> ms)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Set&lt;ModuleDescriptor.Modifier&gt; ms**,  {% include w3api/param_description.html metodo=_dato parametro="Set<ModuleDescriptor.Modifier> ms" %}

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
