---
title: ModuleDescriptor.read()
permalink: Java/ModuleDescriptor/read
date: 2021-01-04
key: JavaJava.M.ModuleDescriptor
category: java
tags: ['java se', 'java.lang.module', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleDescriptor.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ModuleDescriptor read(InputStream in) throws IOException
public static ModuleDescriptor read(InputStream in, Supplier<Set<String>> packageFinder) throws IOException
public static ModuleDescriptor read(ByteBuffer bb)
public static ModuleDescriptor read(ByteBuffer bb, Supplier<Set<String>> packageFinder)
~~~

## Parámetros
* **ByteBuffer bb**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer bb" %}
* **Supplier&lt;Set&lt;String&gt;&gt; packageFinder**,  {% include w3api/param_description.html metodo=_data parametro="Supplier<Set<String>> packageFinder" %}
* **InputStream in**,  {% include w3api/param_description.html metodo=_data parametro="InputStream in" %}

## Excepciones
[InvalidModuleDescriptorException](/Java/InvalidModuleDescriptorException/), [IOException](/Java/IOException/)

## Clase Padre
[ModuleDescriptor](/Java/ModuleDescriptor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.ModuleDescriptor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
