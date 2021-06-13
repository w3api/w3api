---
title: ModuleLayer.defineModules()
permalink: /Java/ModuleLayer/defineModules/
date: 2021-01-11
key: Java.M.ModuleLayer
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleLayer.metodos valor="defineModules" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ModuleLayer defineModules(Configuration cf, Function<String,ClassLoader> clf)
public static ModuleLayer.Controller defineModules(Configuration cf, List<ModuleLayer> parentLayers, Function<String,ClassLoader> clf)
~~~

## Parámetros
* **ClassLoader&gt; clf**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader> clf" %}
* **Function&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Function<String" %}
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
