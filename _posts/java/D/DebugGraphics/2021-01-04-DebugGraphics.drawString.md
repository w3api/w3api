---
title: DebugGraphics.drawString()
permalink: Java/DebugGraphics/drawString
date: 2021-01-04
key: JavaJava.D.DebugGraphics
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DebugGraphics.metodos valor="drawString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void drawString(String aString, int x, int y)
public void drawString(AttributedCharacterIterator iterator, int x, int y)
~~~

## Parámetros
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **String aString**,  {% include w3api/param_description.html metodo=_data parametro="String aString" %}
* **AttributedCharacterIterator iterator**,  {% include w3api/param_description.html metodo=_data parametro="AttributedCharacterIterator iterator" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Clase Padre
[DebugGraphics](/Java/DebugGraphics/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DebugGraphics.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
