---
title: ModuleDescriptor.Builder.provides()
permalink: Java/ModuleDescriptor/Builder/provides
date: 2021-01-04
key: JavaJava.M.ModuleDescriptor.Builder
category: java
tags: ['java se', 'java.lang.module', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleDescriptor.Builder.metodos valor="provides" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ModuleDescriptor.Builder provides(ModuleDescriptor.Provides p)
public ModuleDescriptor.Builder provides(String service, List<String> providers)
~~~

## Parámetros
* **ModuleDescriptor.Provides p**,  {% include w3api/param_description.html metodo=_data parametro="ModuleDescriptor.Provides p" %}
* **List&lt;String&gt; providers**,  {% include w3api/param_description.html metodo=_data parametro="List<String> providers" %}
* **String service**,  {% include w3api/param_description.html metodo=_data parametro="String service" %}

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
