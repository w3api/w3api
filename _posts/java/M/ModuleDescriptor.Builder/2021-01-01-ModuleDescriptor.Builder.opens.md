---
title: ModuleDescriptor.Builder.opens()
permalink: Java/ModuleDescriptor/Builder/opens
date: 2021-01-11
key: JavaJava.M.ModuleDescriptor.Builder
category: java
tags: ['java se', 'java.lang.module', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleDescriptor.Builder.metodos valor="opens" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ModuleDescriptor.Builder opens(ModuleDescriptor.Opens obj)
public ModuleDescriptor.Builder opens(String pn)
public ModuleDescriptor.Builder opens(String pn, Set<String> targets)
public ModuleDescriptor.Builder opens(Set<ModuleDescriptor.Opens.Modifier> ms, String pn)
public ModuleDescriptor.Builder opens(Set<ModuleDescriptor.Opens.Modifier> ms, String pn, Set<String> targets)
~~~

## Parámetros
* **ModuleDescriptor.Opens obj**,  {% include w3api/param_description.html metodo=_dato parametro="ModuleDescriptor.Opens obj" %}
* **Set&lt;ModuleDescriptor.Opens.Modifier&gt; ms**,  {% include w3api/param_description.html metodo=_dato parametro="Set<ModuleDescriptor.Opens.Modifier> ms" %}
* **String pn**,  {% include w3api/param_description.html metodo=_dato parametro="String pn" %}
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
