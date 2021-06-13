---
title: ModuleDescriptor.Builder.exports()
permalink: Java/ModuleDescriptor/Builder/exports
date: 2021-01-11
key: JavaJava.M.ModuleDescriptor.Builder
category: Java
tags: ['java se', 'java.lang.module', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleDescriptor.Builder.metodos valor="exports" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ModuleDescriptor.Builder exports(ModuleDescriptor.Exports e)
public ModuleDescriptor.Builder exports(String pn)
public ModuleDescriptor.Builder exports(String pn, Set<String> targets)
public ModuleDescriptor.Builder exports(Set<ModuleDescriptor.Exports.Modifier> ms, String pn)
public ModuleDescriptor.Builder exports(Set<ModuleDescriptor.Exports.Modifier> ms, String pn, Set<String> targets)
~~~

## Parámetros
* **ModuleDescriptor.Exports e**,  {% include w3api/param_description.html metodo=_dato parametro="ModuleDescriptor.Exports e" %}
* **String pn**,  {% include w3api/param_description.html metodo=_dato parametro="String pn" %}
* **Set&lt;ModuleDescriptor.Exports.Modifier&gt; ms**,  {% include w3api/param_description.html metodo=_dato parametro="Set<ModuleDescriptor.Exports.Modifier> ms" %}
* **Set&lt;String&gt; targets**,  {% include w3api/param_description.html metodo=_dato parametro="Set<String> targets" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[ModuleDescriptor.Builder](/Java/ModuleDescriptor/Builder/)

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
