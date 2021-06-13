---
title: ModuleLayer.defineModulesWithOneLoader()
permalink: Java/ModuleLayer/defineModulesWithOneLoader
date: 2021-01-11
key: JavaJava.M.ModuleLayer
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleLayer.metodos valor="defineModulesWithOneLoader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ModuleLayer defineModulesWithOneLoader(Configuration cf, ClassLoader parentLoader)
public static ModuleLayer.Controller defineModulesWithOneLoader(Configuration cf, List<ModuleLayer> parentLayers, ClassLoader parentLoader)
~~~

## Parámetros
* **ClassLoader parentLoader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader parentLoader" %}
* **Configuration cf**,  {% include w3api/param_description.html metodo=_dato parametro="Configuration cf" %}
* **List&lt;ModuleLayer&gt; parentLayers**,  {% include w3api/param_description.html metodo=_dato parametro="List<ModuleLayer> parentLayers" %}

## Excepciones
[LayerInstantiationException](/Java/LayerInstantiationException/), [SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
