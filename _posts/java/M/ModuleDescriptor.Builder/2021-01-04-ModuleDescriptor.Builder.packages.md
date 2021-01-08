---
title: ModuleDescriptor.Builder.packages()
permalink: Java/ModuleDescriptor/Builder/packages
date: 2021-01-04
key: JavaJava.M.ModuleDescriptor.Builder
category: java
tags: ['java se', 'java.lang.module', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleDescriptor.Builder.metodos valor="packages" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ModuleDescriptor.Builder packages(Set<String> pns)
~~~

## Parámetros
* **Set&lt;String&gt; pns**,  {% include w3api/param_description.html metodo=_data parametro="Set<String> pns" %}

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
