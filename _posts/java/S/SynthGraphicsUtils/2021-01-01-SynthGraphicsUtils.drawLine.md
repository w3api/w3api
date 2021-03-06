---
title: SynthGraphicsUtils.drawLine()
permalink: /Java/SynthGraphicsUtils/drawLine/
date: 2021-01-11
key: Java.S.SynthGraphicsUtils
category: Java
tags: ['java se', 'javax.swing.plaf.synth', 'java.desktop', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SynthGraphicsUtils.metodos valor="drawLine" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void drawLine(SynthContext context, Object paintKey, Graphics g, int x1, int y1, int x2, int y2)
public void drawLine(SynthContext context, Object paintKey, Graphics g, int x1, int y1, int x2, int y2, Object styleKey)
~~~

## Parámetros
* **int x1**,  {% include w3api/param_description.html metodo=_dato parametro="int x1" %}
* **int x2**,  {% include w3api/param_description.html metodo=_dato parametro="int x2" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}
* **int y2**,  {% include w3api/param_description.html metodo=_dato parametro="int y2" %}
* **Object styleKey**,  {% include w3api/param_description.html metodo=_dato parametro="Object styleKey" %}
* **Object paintKey**,  {% include w3api/param_description.html metodo=_dato parametro="Object paintKey" %}
* **int y1**,  {% include w3api/param_description.html metodo=_dato parametro="int y1" %}
* **SynthContext context**,  {% include w3api/param_description.html metodo=_dato parametro="SynthContext context" %}

## Clase Padre
[SynthGraphicsUtils](/Java/SynthGraphicsUtils/)

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
