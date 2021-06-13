---
title: BorderFactory.createSoftBevelBorder()
permalink: /Java/BorderFactory/createSoftBevelBorder/
date: 2021-01-11
key: Java.B.BorderFactory
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BorderFactory.metodos valor="createSoftBevelBorder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Border createSoftBevelBorder(int type)
public static Border createSoftBevelBorder(int type, Color highlight, Color shadow)
public static Border createSoftBevelBorder(int type, Color highlightOuter, Color highlightInner, Color shadowOuter, Color shadowInner)
~~~

## Parámetros
* **Color shadow**,  {% include w3api/param_description.html metodo=_dato parametro="Color shadow" %}
* **Color highlight**,  {% include w3api/param_description.html metodo=_dato parametro="Color highlight" %}
* **Color highlightInner**,  {% include w3api/param_description.html metodo=_dato parametro="Color highlightInner" %}
* **int type**,  {% include w3api/param_description.html metodo=_dato parametro="int type" %}
* **Color shadowInner**,  {% include w3api/param_description.html metodo=_dato parametro="Color shadowInner" %}
* **Color highlightOuter**,  {% include w3api/param_description.html metodo=_dato parametro="Color highlightOuter" %}
* **Color shadowOuter**,  {% include w3api/param_description.html metodo=_dato parametro="Color shadowOuter" %}

## Clase Padre
[BorderFactory](/Java/BorderFactory/)

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
