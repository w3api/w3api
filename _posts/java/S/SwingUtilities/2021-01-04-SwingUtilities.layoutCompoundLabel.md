---
title: SwingUtilities.layoutCompoundLabel()
permalink: Java/SwingUtilities/layoutCompoundLabel
date: 2021-01-04
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
* **int horizontalAlignment**,  {% include w3api/param_description.html metodo=_data parametro="int horizontalAlignment" %}
* **int textIconGap**,  {% include w3api/param_description.html metodo=_data parametro="int textIconGap" %}
* **String text**,  {% include w3api/param_description.html metodo=_data parametro="String text" %}
* **Rectangle iconR**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle iconR" %}
* **JComponent c**,  {% include w3api/param_description.html metodo=_data parametro="JComponent c" %}
* **Rectangle textR**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle textR" %}
* **FontMetrics fm**,  {% include w3api/param_description.html metodo=_data parametro="FontMetrics fm" %}
* **int verticalTextPosition**,  {% include w3api/param_description.html metodo=_data parametro="int verticalTextPosition" %}
* **int horizontalTextPosition**,  {% include w3api/param_description.html metodo=_data parametro="int horizontalTextPosition" %}
* **Rectangle viewR**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle viewR" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_data parametro="Icon icon" %}
* **int verticalAlignment**,  {% include w3api/param_description.html metodo=_data parametro="int verticalAlignment" %}

## Clase Padre
[SwingUtilities](/Java/SwingUtilities/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SwingUtilities.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
