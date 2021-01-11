---
title: SwingUtilities.layoutCompoundLabel()
permalink: Java/SwingUtilities/layoutCompoundLabel
date: 2021-01-11
key: JavaJava.S.SwingUtilities
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SwingUtilities.metodos valor="layoutCompoundLabel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static String layoutCompoundLabel(FontMetrics fm, String text, Icon icon, int verticalAlignment, int horizontalAlignment, int verticalTextPosition, int horizontalTextPosition, Rectangle viewR, Rectangle iconR, Rectangle textR, int textIconGap)
public static String layoutCompoundLabel(JComponent c, FontMetrics fm, String text, Icon icon, int verticalAlignment, int horizontalAlignment, int verticalTextPosition, int horizontalTextPosition, Rectangle viewR, Rectangle iconR, Rectangle textR, int textIconGap)
~~~

## Parámetros
* **Rectangle iconR**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle iconR" %}
* **FontMetrics fm**,  {% include w3api/param_description.html metodo=_dato parametro="FontMetrics fm" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_dato parametro="Icon icon" %}
* **Rectangle textR**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle textR" %}
* **int horizontalTextPosition**,  {% include w3api/param_description.html metodo=_dato parametro="int horizontalTextPosition" %}
* **JComponent c**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent c" %}
* **String text**,  {% include w3api/param_description.html metodo=_dato parametro="String text" %}
* **Rectangle viewR**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle viewR" %}
* **int horizontalAlignment**,  {% include w3api/param_description.html metodo=_dato parametro="int horizontalAlignment" %}
* **int textIconGap**,  {% include w3api/param_description.html metodo=_dato parametro="int textIconGap" %}
* **int verticalTextPosition**,  {% include w3api/param_description.html metodo=_dato parametro="int verticalTextPosition" %}
* **int verticalAlignment**,  {% include w3api/param_description.html metodo=_dato parametro="int verticalAlignment" %}

## Clase Padre
[SwingUtilities](/Java/SwingUtilities/)

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
