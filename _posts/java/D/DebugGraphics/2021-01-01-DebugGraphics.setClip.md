---
title: DebugGraphics.setClip()
permalink: Java/DebugGraphics/setClip
date: 2021-01-11
key: JavaJava.D.DebugGraphics
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DebugGraphics.metodos valor="setClip" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setClip(int x, int y, int width, int height)
public void setClip(Shape clip)
~~~

## Parámetros
* **Shape clip**,  {% include w3api/param_description.html metodo=_dato parametro="Shape clip" %}
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}

## Clase Padre
[DebugGraphics](/Java/DebugGraphics/)

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
