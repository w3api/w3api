---
title: SynthGraphicsUtils.paintText()
permalink: Java/SynthGraphicsUtils/paintText
date: 2021-01-04
key: JavaJava.S.SynthGraphicsUtils
category: java
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
* **int mnemonicIndex**,  {% include w3api/param_description.html metodo=_data parametro="int mnemonicIndex" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **int hTextPosition**,  {% include w3api/param_description.html metodo=_data parametro="int hTextPosition" %}
* **Rectangle bounds**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle bounds" %}
* **int vTextPosition**,  {% include w3api/param_description.html metodo=_data parametro="int vTextPosition" %}
* **int vAlign**,  {% include w3api/param_description.html metodo=_data parametro="int vAlign" %}
* **String text**,  {% include w3api/param_description.html metodo=_data parametro="String text" %}
* **int textOffset**,  {% include w3api/param_description.html metodo=_data parametro="int textOffset" %}
* **int iconTextGap**,  {% include w3api/param_description.html metodo=_data parametro="int iconTextGap" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_data parametro="Graphics g" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_data parametro="Icon icon" %}
* **int hAlign**,  {% include w3api/param_description.html metodo=_data parametro="int hAlign" %}
* **SynthContext ss**,  {% include w3api/param_description.html metodo=_data parametro="SynthContext ss" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Clase Padre
[SynthGraphicsUtils](/Java/SynthGraphicsUtils/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SynthGraphicsUtils.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
