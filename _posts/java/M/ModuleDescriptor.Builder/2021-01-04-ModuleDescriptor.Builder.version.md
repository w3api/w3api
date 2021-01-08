---
title: ModuleDescriptor.Builder.version()
permalink: Java/ModuleDescriptor/Builder/version
date: 2021-01-04
key: JavaJava.M.ModuleDescriptor.Builder
category: java
tags: ['java se', 'java.lang.module', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleDescriptor.Builder.metodos valor="version" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ModuleDescriptor.Builder version(ModuleDescriptor.Version v)
public ModuleDescriptor.Builder version(String vs)
~~~

## Parámetros
* **String vs**,  {% include w3api/param_description.html metodo=_data parametro="String vs" %}
* **ModuleDescriptor.Version v**,  {% include w3api/param_description.html metodo=_data parametro="ModuleDescriptor.Version v" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
