---
title: SynthPainter.paintTabbedPaneTabBorder()
permalink: /Java/SynthPainter/paintTabbedPaneTabBorder/
date: 2021-01-11
key: Java.S.SynthPainter
category: Java
tags: ['java se', 'javax.swing.plaf.synth', 'java.desktop', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SynthPainter.metodos valor="paintTabbedPaneTabBorder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void paintTabbedPaneTabBorder(SynthContext context, Graphics g, int x, int y, int w, int h, int tabIndex)
public void paintTabbedPaneTabBorder(SynthContext context, Graphics g, int x, int y, int w, int h, int tabIndex, int orientation)
~~~

## Parámetros
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **int orientation**,  {% include w3api/param_description.html metodo=_dato parametro="int orientation" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **SynthContext context**,  {% include w3api/param_description.html metodo=_dato parametro="SynthContext context" %}
* **int tabIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int tabIndex" %}

## Clase Padre
[SynthPainter](/Java/SynthPainter/)

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
