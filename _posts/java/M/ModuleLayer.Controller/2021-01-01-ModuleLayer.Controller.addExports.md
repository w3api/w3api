---
title: ModuleLayer.Controller.addExports()
permalink: Java/ModuleLayer/Controller/addExports
date: 2021-01-11
key: JavaJava.M.ModuleLayer.Controller
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleLayer.Controller.metodos valor="addExports" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ModuleLayer.Controller addExports(Module source, String pn, Module target)
~~~

## Parámetros
* **Module target**,  {% include w3api/param_description.html metodo=_dato parametro="Module target" %}
* **String pn**,  {% include w3api/param_description.html metodo=_dato parametro="String pn" %}
* **Module source**,  {% include w3api/param_description.html metodo=_dato parametro="Module source" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ModuleLayer.Controller](/Java/ModuleLayer/Controller/)

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
