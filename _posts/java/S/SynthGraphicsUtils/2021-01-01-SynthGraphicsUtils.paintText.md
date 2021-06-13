---
title: SynthGraphicsUtils.paintText()
permalink: /Java/SynthGraphicsUtils/paintText/
date: 2021-01-11
key: Java.S.SynthGraphicsUtils
category: Java
tags: ['java se', 'javax.swing.plaf.synth', 'java.desktop', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SynthGraphicsUtils.metodos valor="paintText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void paintText(SynthContext ss, Graphics g, String text, int x, int y, int mnemonicIndex)
public void paintText(SynthContext ss, Graphics g, String text, Rectangle bounds, int mnemonicIndex)
public void paintText(SynthContext ss, Graphics g, String text, Icon icon, int hAlign, int vAlign, int hTextPosition, int vTextPosition, int iconTextGap, int mnemonicIndex, int textOffset)
~~~

## Parámetros
* **int iconTextGap**,  {% include w3api/param_description.html metodo=_dato parametro="int iconTextGap" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}
* **int vTextPosition**,  {% include w3api/param_description.html metodo=_dato parametro="int vTextPosition" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_dato parametro="Icon icon" %}
* **int vAlign**,  {% include w3api/param_description.html metodo=_dato parametro="int vAlign" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int mnemonicIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int mnemonicIndex" %}
* **int textOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int textOffset" %}
* **String text**,  {% include w3api/param_description.html metodo=_dato parametro="String text" %}
* **Rectangle bounds**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle bounds" %}
* **int hAlign**,  {% include w3api/param_description.html metodo=_dato parametro="int hAlign" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **SynthContext ss**,  {% include w3api/param_description.html metodo=_dato parametro="SynthContext ss" %}
* **int hTextPosition**,  {% include w3api/param_description.html metodo=_dato parametro="int hTextPosition" %}

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
