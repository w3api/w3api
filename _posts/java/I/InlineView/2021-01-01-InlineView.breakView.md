---
title: InlineView.breakView()
permalink: /Java/InlineView/breakView/
date: 2021-01-11
key: Java.I.InlineView
category: Java
tags: ['java se', 'javax.swing.text.html', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InlineView.metodos valor="breakView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public View breakView(int axis, int offset, float pos, float len)
~~~

## Parámetros
* **int axis**,  {% include w3api/param_description.html metodo=_dato parametro="int axis" %}
* **float len**,  {% include w3api/param_description.html metodo=_dato parametro="float len" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **float pos**,  {% include w3api/param_description.html metodo=_dato parametro="float pos" %}

## Clase Padre
[InlineView](/Java/InlineView/)

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
