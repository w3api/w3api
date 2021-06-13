---
title: SynthGraphicsUtils.layoutText()
permalink: /Java/SynthGraphicsUtils/layoutText/
date: 2021-01-11
key: Java.S.SynthGraphicsUtils
category: Java
tags: ['java se', 'javax.swing.plaf.synth', 'java.desktop', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SynthGraphicsUtils.metodos valor="layoutText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String layoutText(SynthContext ss, FontMetrics fm, String text, Icon icon, int hAlign, int vAlign, int hTextPosition, int vTextPosition, Rectangle viewR, Rectangle iconR, Rectangle textR, int iconTextGap)
~~~

## Parámetros
* **int iconTextGap**,  {% include w3api/param_description.html metodo=_dato parametro="int iconTextGap" %}
* **Rectangle iconR**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle iconR" %}
* **int vTextPosition**,  {% include w3api/param_description.html metodo=_dato parametro="int vTextPosition" %}
* **FontMetrics fm**,  {% include w3api/param_description.html metodo=_dato parametro="FontMetrics fm" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_dato parametro="Icon icon" %}
* **Rectangle textR**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle textR" %}
* **int vAlign**,  {% include w3api/param_description.html metodo=_dato parametro="int vAlign" %}
* **String text**,  {% include w3api/param_description.html metodo=_dato parametro="String text" %}
* **Rectangle viewR**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle viewR" %}
* **int hAlign**,  {% include w3api/param_description.html metodo=_dato parametro="int hAlign" %}
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
