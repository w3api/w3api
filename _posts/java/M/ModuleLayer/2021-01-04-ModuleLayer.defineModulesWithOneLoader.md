---
title: ModuleLayer.defineModulesWithOneLoader()
permalink: Java/ModuleLayer/defineModulesWithOneLoader
date: 2021-01-04
key: JavaJava.M.ModuleLayer
category: java
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
* **ClassLoader parentLoader**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader parentLoader" %}
* **List&lt;ModuleLayer&gt; parentLayers**,  {% include w3api/param_description.html metodo=_data parametro="List<ModuleLayer> parentLayers" %}
* **Configuration cf**,  {% include w3api/param_description.html metodo=_data parametro="Configuration cf" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [LayerInstantiationException](/Java/LayerInstantiationException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ModuleLayer](/Java/ModuleLayer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.ModuleLayer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
