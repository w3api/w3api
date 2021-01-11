---
title: AlphaComposite.createContext()
permalink: Java/AlphaComposite/createContext
date: 2021-01-11
key: JavaJava.A.AlphaComposite
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AlphaComposite.metodos valor="createContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CompositeContext createContext(ColorModel srcColorModel, ColorModel dstColorModel, RenderingHints hints)
~~~

## Parámetros
* **RenderingHints hints**,  {% include w3api/param_description.html metodo=_dato parametro="RenderingHints hints" %}
* **ColorModel srcColorModel**,  {% include w3api/param_description.html metodo=_dato parametro="ColorModel srcColorModel" %}
* **ColorModel dstColorModel**,  {% include w3api/param_description.html metodo=_dato parametro="ColorModel dstColorModel" %}

## Clase Padre
[AlphaComposite](/Java/AlphaComposite/)

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
