---
title: NimbusLookAndFeel.getDerivedColor()
permalink: Java/NimbusLookAndFeel/getDerivedColor
date: 2021-01-11
key: JavaJava.N.NimbusLookAndFeel
category: java
tags: ['java se', 'javax.swing.plaf.nimbus', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NimbusLookAndFeel.metodos valor="getDerivedColor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Color getDerivedColor(Color color1, Color color2, float midPoint)
protected Color getDerivedColor(Color color1, Color color2, float midPoint, boolean uiResource)
public Color getDerivedColor(String uiDefaultParentName, float hOffset, float sOffset, float bOffset, int aOffset, boolean uiResource)
~~~

## Parámetros
* **boolean uiResource**,  {% include w3api/param_description.html metodo=_dato parametro="boolean uiResource" %}
* **int aOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int aOffset" %}
* **float bOffset**,  {% include w3api/param_description.html metodo=_dato parametro="float bOffset" %}
* **Color color1**,  {% include w3api/param_description.html metodo=_dato parametro="Color color1" %}
* **String uiDefaultParentName**,  {% include w3api/param_description.html metodo=_dato parametro="String uiDefaultParentName" %}
* **float hOffset**,  {% include w3api/param_description.html metodo=_dato parametro="float hOffset" %}
* **float midPoint**,  {% include w3api/param_description.html metodo=_dato parametro="float midPoint" %}
* **float sOffset**,  {% include w3api/param_description.html metodo=_dato parametro="float sOffset" %}
* **Color color2**,  {% include w3api/param_description.html metodo=_dato parametro="Color color2" %}

## Clase Padre
[NimbusLookAndFeel](/Java/NimbusLookAndFeel/)

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
