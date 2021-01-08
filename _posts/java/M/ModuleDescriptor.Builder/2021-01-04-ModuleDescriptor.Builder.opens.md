---
title: ModuleDescriptor.Builder.opens()
permalink: Java/ModuleDescriptor/Builder/opens
date: 2021-01-04
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
* **ModuleDescriptor.Opens obj**,  {% include w3api/param_description.html metodo=_data parametro="ModuleDescriptor.Opens obj" %}
* **Set&lt;ModuleDescriptor.Opens.Modifier&gt; ms**,  {% include w3api/param_description.html metodo=_data parametro="Set<ModuleDescriptor.Opens.Modifier> ms" %}
* **Set&lt;String&gt; targets**,  {% include w3api/param_description.html metodo=_data parametro="Set<String> targets" %}
* **String pn**,  {% include w3api/param_description.html metodo=_data parametro="String pn" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ModuleDescriptor.Builder](/Java/ModuleDescriptor/Builder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.ModuleDescriptor.Builder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
