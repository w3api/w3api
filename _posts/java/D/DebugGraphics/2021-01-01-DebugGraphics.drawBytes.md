---
title: DebugGraphics.drawBytes()
permalink: /Java/DebugGraphics/drawBytes/
date: 2021-01-11
key: Java.D.DebugGraphics
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DebugGraphics.metodos valor="drawBytes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void drawBytes(byte[] data, int offset, int length, int x, int y)
~~~

## Parámetros
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **byte[] data**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] data" %}

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
