---
title: JScrollBar.fireAdjustmentValueChanged()
permalink: /Java/JScrollBar/fireAdjustmentValueChanged/
date: 2021-01-11
key: Java.J.JScrollBar
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JScrollBar.metodos valor="fireAdjustmentValueChanged" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void fireAdjustmentValueChanged(int id, int type, int value)
~~~

## Parámetros
* **int value**,  {% include w3api/param_description.html metodo=_dato parametro="int value" %}
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}
* **int type**,  {% include w3api/param_description.html metodo=_dato parametro="int type" %}

## Clase Padre
[JScrollBar](/Java/JScrollBar/)

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
