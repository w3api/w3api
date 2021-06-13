---
title: GeneralPath.GeneralPath()
permalink: /Java/GeneralPath/GeneralPath/
date: 2021-01-11
key: Java.G.GeneralPath
category: Java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GeneralPath.constructores valor="GeneralPath" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public GeneralPath()
public GeneralPath(int rule)
public GeneralPath(int rule, int initialCapacity)
public GeneralPath(Shape s)
~~~

## Parámetros
* **int initialCapacity**,  {% include w3api/param_description.html metodo=_dato parametro="int initialCapacity" %}
* **Shape s**,  {% include w3api/param_description.html metodo=_dato parametro="Shape s" %}
* **int rule**,  {% include w3api/param_description.html metodo=_dato parametro="int rule" %}

## Clase Padre
[GeneralPath](/Java/GeneralPath/)

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
