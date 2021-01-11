---
title: ModuleDescriptor.Builder.uses()
permalink: Java/ModuleDescriptor/Builder/uses
date: 2021-01-11
key: JavaJava.M.ModuleDescriptor.Builder
category: java
tags: ['java se', 'java.lang.module', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleDescriptor.Builder.metodos valor="uses" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ModuleDescriptor.Builder uses(String service)
~~~

## Parámetros
* **String service**,  {% include w3api/param_description.html metodo=_dato parametro="String service" %}

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
