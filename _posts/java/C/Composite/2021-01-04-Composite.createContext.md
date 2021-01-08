---
title: Composite.createContext()
permalink: Java/Composite/createContext
date: 2021-01-04
key: JavaJava.C.Composite
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Composite.metodos valor="createContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
CompositeContext createContext(ColorModel srcColorModel, ColorModel dstColorModel, RenderingHints hints)
~~~

## Parámetros
* **ColorModel dstColorModel**,  {% include w3api/param_description.html metodo=_data parametro="ColorModel dstColorModel" %}
* **RenderingHints hints**,  {% include w3api/param_description.html metodo=_data parametro="RenderingHints hints" %}
* **ColorModel srcColorModel**,  {% include w3api/param_description.html metodo=_data parametro="ColorModel srcColorModel" %}

## Clase Padre
[Composite](/Java/Composite/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Composite.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
