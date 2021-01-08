---
title: BorderFactory.createSoftBevelBorder()
permalink: Java/BorderFactory/createSoftBevelBorder
date: 2021-01-04
key: JavaJava.B.BorderFactory
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
* **int type**,  {% include w3api/param_description.html metodo=_data parametro="int type" %}
* **Color highlightInner**,  {% include w3api/param_description.html metodo=_data parametro="Color highlightInner" %}
* **Color highlight**,  {% include w3api/param_description.html metodo=_data parametro="Color highlight" %}
* **Color shadowOuter**,  {% include w3api/param_description.html metodo=_data parametro="Color shadowOuter" %}
* **Color shadowInner**,  {% include w3api/param_description.html metodo=_data parametro="Color shadowInner" %}
* **Color shadow**,  {% include w3api/param_description.html metodo=_data parametro="Color shadow" %}
* **Color highlightOuter**,  {% include w3api/param_description.html metodo=_data parametro="Color highlightOuter" %}

## Clase Padre
[BorderFactory](/Java/BorderFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BorderFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
