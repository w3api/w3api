---
title: ModuleDescriptor.Builder.requires()
permalink: /Java/ModuleDescriptor/Builder/requires/
date: 2021-01-11
key: Java.M.ModuleDescriptor.Builder
category: Java
tags: ['java se', 'java.lang.module', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleDescriptor.Builder.metodos valor="requires" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ModuleDescriptor.Builder requires(ModuleDescriptor.Requires req)
public ModuleDescriptor.Builder requires(String mn)
public ModuleDescriptor.Builder requires(Set<ModuleDescriptor.Requires.Modifier> ms, String mn)
public ModuleDescriptor.Builder requires(Set<ModuleDescriptor.Requires.Modifier> ms, String mn, ModuleDescriptor.Version compiledVersion)
~~~

## Parámetros
* **Set&lt;ModuleDescriptor.Requires.Modifier&gt; ms**,  {% include w3api/param_description.html metodo=_dato parametro="Set<ModuleDescriptor.Requires.Modifier> ms" %}
* **ModuleDescriptor.Requires req**,  {% include w3api/param_description.html metodo=_dato parametro="ModuleDescriptor.Requires req" %}
* **ModuleDescriptor.Version compiledVersion**,  {% include w3api/param_description.html metodo=_dato parametro="ModuleDescriptor.Version compiledVersion" %}
* **String mn**,  {% include w3api/param_description.html metodo=_dato parametro="String mn" %}

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
