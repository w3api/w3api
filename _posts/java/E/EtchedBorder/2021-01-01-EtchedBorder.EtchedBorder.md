---
title: EtchedBorder.EtchedBorder()
permalink: /Java/EtchedBorder/EtchedBorder/
date: 2021-01-11
key: Java.E.EtchedBorder
category: Java
tags: ['java se', 'javax.swing.border', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EtchedBorder.constructores valor="EtchedBorder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public EtchedBorder()
public EtchedBorder(int etchType)
@ConstructorProperties({"etchType","highlightColor","shadowColor"}) public EtchedBorder(int etchType, Color highlight, Color shadow)
public EtchedBorder(Color highlight, Color shadow)
~~~

## Parámetros
* **Color shadow**,  {% include w3api/param_description.html metodo=_dato parametro="Color shadow" %}
* **Color highlight**,  {% include w3api/param_description.html metodo=_dato parametro="Color highlight" %}
* **int etchType**,  {% include w3api/param_description.html metodo=_dato parametro="int etchType" %}

## Clase Padre
[EtchedBorder](/Java/EtchedBorder/)

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
