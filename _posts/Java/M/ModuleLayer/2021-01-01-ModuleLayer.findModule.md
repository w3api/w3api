---
title: ModuleLayer.findModule()
permalink: /Java/ModuleLayer/findModule/
date: 2021-01-11
key: Java.M.ModuleLayer
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleLayer.metodos valor="findModule" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Optional<Module> findModule(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

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
