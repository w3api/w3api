---
title: InputMethodHighlight.InputMethodHighlight()
permalink: Java/InputMethodHighlight-java-awt-im/InputMethodHighlight
date: 2021-01-04
key: JavaJava.I.InputMethodHighlight-java-awt-im
category: java
tags: ['java se', 'java.awt.im', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InputMethodHighlight-java-awt-im.constructores valor="InputMethodHighlight" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InputMethodHighlight(boolean selected, int state)
public InputMethodHighlight(boolean selected, int state, int variation)
public InputMethodHighlight(boolean selected, int state, int variation, Map<TextAttribute,?> style)
~~~

## Parámetros
* **int state**,  {% include w3api/param_description.html metodo=_data parametro="int state" %}
* **?&gt; style**,  {% include w3api/param_description.html metodo=_data parametro="?> style" %}
* **boolean selected**,  {% include w3api/param_description.html metodo=_data parametro="boolean selected" %}
* **int variation**,  {% include w3api/param_description.html metodo=_data parametro="int variation" %}
* **Map&lt;TextAttribute**,  {% include w3api/param_description.html metodo=_data parametro="Map<TextAttribute" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[InputMethodHighlight](/Java/InputMethodHighlight-java-awt-im/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InputMethodHighlight-java-awt-im.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
